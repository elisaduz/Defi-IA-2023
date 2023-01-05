# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 15:36:24 2022

@author: Alex
"""

import pandas as pd
from math import log
import pickle


from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split 
from sklearn.model_selection import GridSearchCV

data_train=pd.read_csv('./Datatrain/data_train_final.csv')
data_train=data_train.drop(['Unnamed: 0'],axis=1)

train_sorted_bis=pd.read_csv('./Datatrain/train_sorted_bis.csv')
train_sorted_bis=train_sorted_bis.drop(['Unnamed: 0'],axis=1)

data_train["log_price"]=data_train["price"].map(lambda x : log(x))

list_avatar_train=data_train['avatar_id'].unique()

data_train['index_request']=0

for avatar in list_avatar_train : 
    test1=data_train[data_train['avatar_id'] ==avatar].copy()
    list_date=test1['date'].unique()
    
    if len(list_date)==1 : 
        ech=test1[test1['date'] ==list_date[0]].copy()
        ech['index_request']=1
        data_train[data_train['avatar_id']==avatar]=ech
        
    else : 
        for i in range(len(list_date)) : 
            ech=test1[test1['date'] ==list_date[i]].copy()
            ech['index_request']=i+1
            test1[test1['date'] ==list_date[i]]=ech
        data_train[data_train['avatar_id']==avatar]=test1


# this function is by Max Halford at the address noted above
def calc_smooth_mean(df, by, on, m, target_df):
    '''Function returns a weighted mean value for the each member of a column.
    Arguments:
    df: The df being used to calculate the means
    by: the column being target encoded
    on: the thing to be encoded; almost always price in this circumstance
    m: weight before moving toward global mean; usually a min # samples
    target_df: the target df for the mean encoding. Could be same as df or different.'''
    # Compute the global mean
    mean = df[on].mean() 

    # Compute the number of values and the mean of each group
    agg = df.groupby(by)[on].agg(['count', 'mean'])  
    counts = agg['count']
    means = agg['mean']

    # Compute the "smoothed" means
    smooth = (counts * means + m * mean) / (counts + m)

    # Replace each value by the according smoothed mean
    return target_df[by].map(smooth)
    #return round(target_df[by].map(smooth), 0) 



# get size of training data
num_of_samples = data_train.shape[0]

# determining minimum number of samples for zip and month to use their
# own mean rather than expanding into the full data set mean 
city_samples = num_of_samples/data_train['city'].unique().shape[0]
group_samples = num_of_samples/data_train['group'].unique().shape[0]
brand_samples = num_of_samples/data_train['brand'].unique().shape[0]
language_samples = num_of_samples/data_train['language'].unique().shape[0]



agg = data_train.groupby('city')['price'].agg(['count', 'mean'])  
counts = agg['count']
means = agg['mean']
mean = data_train['price'].mean()
smooth_city = (counts * means + city_samples * mean) / (counts + city_samples)

agg = data_train.groupby('group')['price'].agg(['count', 'mean'])  
counts = agg['count']
means = agg['mean']
mean = data_train['price'].mean()
smooth_group = (counts * means + group_samples * mean) / (counts + group_samples)

agg = data_train.groupby('brand')['price'].agg(['count', 'mean'])  
counts = agg['count']
means = agg['mean']
mean = data_train['price'].mean()
smooth_brand = (counts * means + brand_samples * mean) / (counts + brand_samples)

agg = data_train.groupby('language')['price'].agg(['count', 'mean'])  
counts = agg['count']
means = agg['mean']
mean = data_train['price'].mean()
smooth_language = (counts * means + language_samples * mean) / (counts + language_samples)


with open("dict_city_encoding.pkl", "wb") as tf:
    pickle.dump(smooth_city.to_dict(),tf)
    
with open("dict_group_encoding.pkl", "wb") as tf:
    pickle.dump(smooth_group.to_dict(),tf)
    
with open("dict_brand_encoding.pkl", "wb") as tf:
    pickle.dump(smooth_brand.to_dict(),tf)
    
with open("dict_language_encoding.pkl", "wb") as tf:
    pickle.dump(smooth_language.to_dict(),tf)


data_train['city'] = calc_smooth_mean(data_train, by='city', on='price', m=city_samples,target_df=data_train)
data_train['group'] = calc_smooth_mean(data_train, by='group', on='price', m=group_samples,target_df=data_train)
data_train['brand'] = calc_smooth_mean(data_train, by='brand', on='price', m=brand_samples,target_df=data_train)
data_train['language'] = calc_smooth_mean(data_train, by='language', on='price', m=language_samples,target_df=data_train)



data_train=data_train.drop(['index'],axis=1)
data_train=data_train.drop(['avatar_id'],axis=1)
data_train=data_train.drop(['price'],axis=1)
data_train=data_train.drop(['index_request'],axis=1)

cols=['city','date','language','mobile','hotel_id','stock','group','brand','parking','pool','children_policy','log_price']

data_train=data_train[cols]
data_train=data_train.iloc[train_sorted_bis.index]

logprice=data_train['log_price']
X_train, X_test, Y_train, Y_test = train_test_split(data_train,logprice,test_size=0.25,random_state=11)
X_train=X_train.drop(['log_price'],axis=1)

param=[{"max_features":list(range(2,10))}]
regrf= GridSearchCV(RandomForestRegressor(),param,cv=5,n_jobs=-1)
regrfOpt=regrf.fit(X_train, Y_train)
# paramètre optimal
print("Meilleur score = %f, Meilleur paramètre = %s" % (regrfOpt.best_score_,regrfOpt.best_params_))

with open("regrfOpt_model.pkl", "wb") as f:
    pickle.dump(regrfOpt, f)  
    