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
from category_encoders import TargetEncoder
data_train1=pd.read_csv('./Datatrain/TRAIN_requete2_features.csv')
data_train1=data_train1.drop(['Unnamed: 0'],axis=1)

data_train2=pd.read_csv('./Datatrain/test_requete_features.csv')
data_train2=data_train2.drop(['Unnamed: 0'],axis=1)

data_train2['index_request']=0

data_train=pd.concat([data_train1,data_train2])

data_train=data_train.reset_index()

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
        

city_encoding = data_train.groupby(['city'])['price'].mean().to_dict()
group_encoding=data_train.groupby(['group'])['price'].mean().to_dict()
brand_encoding=data_train.groupby(['brand'])['price'].mean().to_dict()
language_encoding=data_train.groupby(['language'])['price'].mean().to_dict()



with open("dict_city_encoding.pkl", "wb") as tf:
    pickle.dump(city_encoding,tf)
    
with open("dict_group_encoding.pkl", "wb") as tf:
    pickle.dump(group_encoding,tf)
    
with open("dict_brand_encoding.pkl", "wb") as tf:
    pickle.dump(brand_encoding,tf)
    
with open("dict_language_encoding.pkl", "wb") as tf:
    pickle.dump(language_encoding,tf)
    
encoder = TargetEncoder()
data_train['city'] = encoder.fit_transform(data_train['city'], data_train['price'])
data_train['language'] = encoder.fit_transform(data_train['language'], data_train['price'])
data_train['group'] = encoder.fit_transform(data_train['group'], data_train['price'])
data_train['brand'] = encoder.fit_transform(data_train['brand'], data_train['price'])


data_train=data_train.drop(['index'],axis=1)


data_train=data_train.drop(['avatar_id'],axis=1)


data_train=data_train.drop(['price'],axis=1)

logprice=data_train['log_price']
X_train, X_test, Y_train, Y_test = train_test_split(data_train,logprice,test_size=0.25,random_state=11)
X_train=X_train.drop(['log_price'],axis=1)

print("Beginning of Random Forest")
regrf= RandomForestRegressor(bootstrap= True, max_depth= 110, max_features = 9, min_samples_leaf= 3, min_samples_split= 8, n_estimators= 1000)
regrfOpt=regrf.fit(X_train, Y_train)

# If you've fitted the model just type this to save it: Remember to change the file name
with open("regrfOpt_model.pkl", "wb") as f:
    pickle.dump(regrfOpt, f)  
    
