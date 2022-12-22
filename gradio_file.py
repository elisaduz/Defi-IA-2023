# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 09:53:50 2022

@author: Alex
"""

import gradio as gr
import pickle
import numpy as np



    

def make_prediction(city, date, language, mobile, hotel_id, stock, index_request, group, brand, parking, pool, children_policy):
    with open("regrfOpt_model.pkl", "rb") as f:
        regrfOpt = pickle.load(f)
        city = new_dict_city[city]
        language = new_dict_language[language]
        group = new_dict_group[group]
        brand = new_dict_brand[brand]
        preds = regrfOpt.predict([[city, date, language, mobile, hotel_id, stock, index_request, group, brand, parking, pool, children_policy]])
    
    return str(np.exp(preds))



city_input = gr.Radio(choices = ["amsterdam", "copenhagen", "madrid", "paris", "rome", "sofia", "valletta", "vienna", "vilnius"])


with open("dict_city_encoding.pkl", "rb") as f:
    unpickler = pickle.Unpickler(f)
    new_dict_city = unpickler.load()

date_input = gr.Slider(minimum = 1, maximum = 45, step = 1)

language_input = gr.Radio(choices = ["austrian", "belgian", "bulgarian", "croatian", "cypriot", "czech", "danish", "dutch", "estonian", "finnish", "french", "german", "greek", "hungarian", "irish", "italian", "latvian", "lithuanian", "luxembourgish", "maltese", "polish", "portuguese", "romanian", "slovakian", "slovene", "spanish" ,"swedish"])
with open("dict_language_encoding.pkl", "rb") as f:
    unpickler = pickle.Unpickler(f)
    new_dict_language = unpickler.load()


mobile_input = gr.Radio(choices = [0,1], label= "Enter Mobile Status {1:For mobile order, 0: For computer order}")

hotel_id_input = gr.Radio([161])

stock_input = gr.Radio([50])


index_request_input = gr.Radio([1])

group_input = gr.Radio(["Accar Hotels", "Boss Western", "Chillton Worldwide", "Independant", "Morriott International", "Yin Yang"])
with open("dict_group_encoding.pkl", "rb") as f:
        unpickler = pickle.Unpickler(f)
        new_dict_group = unpickler.load()


brand_input = gr.Radio(["8 Premium", "Ardisson", "Boss Western", "Chill Garden Inn", "Corlton", "CourtYord", "Ibas", "Independant", "J.Halliday Inn", "Marcure", "Morriot", "Navatel", "Quadrupletree", "Royal Lotus", "Safitel", "Tripletree"])
with open("dict_brand_encoding.pkl", "rb") as f:
        unpickler = pickle.Unpickler(f)
        new_dict_brand = unpickler.load()


Parking_input = gr.Radio(choices = [0,1], label= "Enter Parking Status {1:With Parking, 0: Without Parking}")
Pool_input = gr.Radio(choices = [0,1], label= "Enter Pool Status {1:With Pool, 0: Without Pool}")
children_policy_input = gr.Radio(choices = [0,1,2], label= "Enter Children_policy Status {2: si l’hôtel interdit les enfants de moins de 18 ou 21 ans, 1: si l’hôtel interdit les enfants de moins de 12 ans, 0: s’il autorise les enfants sans restrictions}")

# We create the output
output = gr.Textbox()


app = gr.Interface(fn = make_prediction, inputs=[city_input, date_input, language_input, mobile_input, hotel_id_input, stock_input, index_request_input, group_input, brand_input, Parking_input, Pool_input, children_policy_input], outputs=output)
app.launch()
