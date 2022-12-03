# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 09:53:50 2022

@author: Alex
"""

import gradio as gr
import pickle
import numpy as np


# import os

# scores = {} # scores is an empty dict already

# if os.path.getsize("dict_group_encoding.pkl") > 0:      
#     with open("dict_group_encoding.pkl", "rb") as f:
#         unpickler = pickle.Unpickler(f)
#         # if file is not empty scores will be equal
#         # to the value unpickled
#         scores = unpickler.load()

# # with open("dict_group_encoding.pkl", "wb") as tf:
# #     new_dict_group = pickle.load(tf)
# print(scores)
    
# def make_prediction(age, employment_status, bank_name, account_balance):
def make_prediction(city, date, language, mobile, hotel_id, stock, index_request, group, brand, parking, pool, children_policy):
    with open("regrfOpt_model.pkl", "rb") as f:
        regrfOpt = pickle.load(f)
        # Ypred_regrf = regrfOpt.predict(data_test)
        # d_test= pd.read_csv("test_set.csv")
        # submission=pd.DataFrame()
        # submission['index']=d_test['index']
        # submission['price']=np.exp(Ypred_regrf)
        city = new_dict_city[city]
        language = new_dict_language[language]
        group = new_dict_group[group]
        brand = new_dict_brand[brand]
        preds = regrfOpt.predict([[city, date, language, mobile, hotel_id, stock, index_request, group, brand, parking, pool, children_policy]])
    
    return str(np.exp(preds))

#Create the input component for Gradio since we are expecting 4 inputs

city_input = gr.Radio(choices = ["amsterdam", "copenhagen", "madrid", "paris", "rome", "sofia", "valletta", "vienna", "vilnius"])
# with open("dict_city_encoding.pkl", "wb") as tf:
#     new_dict_city = pickle.load(tf)
# city_input = new_dict_city[city_input]

with open("dict_city_encoding.pkl", "rb") as f:
    unpickler = pickle.Unpickler(f)
    new_dict_city = unpickler.load()

# city = str(city_input)
# print(city)
# city_input = new_dict_city[city]

date_input = gr.Slider(minimum = 1, maximum = 45, step = 1)

language_input = gr.Radio(choices = ["austrian", "belgian", "bulgarian", "croatian", "cypriot", "czech", "danish", "dutch", "estonian", "finnish", "french", "german", "greek", "hungarian", "irish", "italian", "latvian", "lithuanian", "luxembourgish", "maltese", "polish", "portuguese", "romanian", "slovakian", "slovene", "spanish" ,"swedish"])
with open("dict_language_encoding.pkl", "rb") as f:
    unpickler = pickle.Unpickler(f)
    new_dict_language = unpickler.load()
# language_input = new_dict_language[language_input]

mobile_input = gr.Radio(choices = [0,1], label= "Enter Mobile Status {1:For mobile order, 0: For computer order}")

hotel_id_input = gr.Radio([161])

stock_input = gr.Radio([50])
# stock_input = gr.Textbox()

index_request_input = gr.Radio([1])

group_input = gr.Radio(["Accar Hotels", "Boss Western", "Chillton Worldwide", "Independant", "Morriott International", "Yin Yang"])
with open("dict_group_encoding.pkl", "rb") as f:
        unpickler = pickle.Unpickler(f)
        new_dict_group = unpickler.load()
# group_input = new_dict_group[group_input]

brand_input = gr.Radio(["8 Premium", "Ardisson", "Boss Western", "Chill Garden Inn", "Corlton", "CourtYord", "Ibas", "Independant", "J.Halliday Inn", "Marcure", "Morriot", "Navatel", "Quadrupletree", "Royal Lotus", "Safitel", "Tripletree"])
with open("dict_brand_encoding.pkl", "rb") as f:
        unpickler = pickle.Unpickler(f)
        new_dict_brand = unpickler.load()
# brand_input = new_dict_brand[brand_input]

Parking_input = gr.Radio(choices = [0,1], label= "Enter Parking Status {1:With Parking, 0: Without Parking}")
Pool_input = gr.Radio(choices = [0,1], label= "Enter Pool Status {1:With Pool, 0: Without Pool}")
children_policy_input = gr.Radio(choices = [0,1,2], label= "Enter Children_policy Status {2: si l’hôtel interdit les enfants de moins de 18 ou 21 ans, 1: si l’hôtel interdit les enfants de moins de 12 ans, 0: s’il autorise les enfants sans restrictions}")

# We create the output
output = gr.Textbox()


app = gr.Interface(fn = make_prediction, inputs=[city_input, date_input, language_input, mobile_input, hotel_id_input, stock_input, index_request_input, group_input, brand_input, Parking_input, Pool_input, children_policy_input], outputs=output)
app.launch()