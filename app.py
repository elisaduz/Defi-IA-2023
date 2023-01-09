# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 09:53:50 2022

@author: Alex
"""

import gradio as gr 
import pickle
import numpy as np



    

def make_prediction(city, date, language, mobile, group, brand, parking, pool, children_policy):
    with open("regrfOpt_model.pkl", "rb") as f:
        regrfOpt = pickle.load(f)
        city = new_dict_city[city]
        language = new_dict_language[language]
        group = new_dict_group[group]
        brand = new_dict_brand[brand]
        hotel_id = 161 # Nous fixons arbitrairement cette valeur 
        stock = 50 # Nous fixons arbitrairement cette valeur 
        preds = regrfOpt.predict([[city, date, language, mobile, hotel_id, stock, group, brand, parking, pool, children_policy]])
        price = str(round(np.exp(preds)[0],2))
        phrase = "Le prix de l'hôtel est " + price + "€"
    return phrase



city_input = gr.Radio(choices = ["amsterdam", "copenhagen", "madrid", "paris", "rome", "sofia", "valletta", "vienna", "vilnius"], label= "Entrez la ville où vous souhaitez séjourner :")


with open("dict_city_encoding.pkl", "rb") as f:
    unpickler = pickle.Unpickler(f)
    new_dict_city = unpickler.load()

date_input = gr.Slider(minimum = 1, maximum = 45, step = 1, label= "Entrez dans combien de jours vous voulez partir :")

language_input = gr.Radio(choices = ["austrian", "belgian", "bulgarian", "croatian", "cypriot", "czech", "danish", "dutch", "estonian", "finnish", "french", "german", "greek", "hungarian", "irish", "italian", "latvian", "lithuanian", "luxembourgish", "maltese", "polish", "portuguese", "romanian", "slovakian", "slovene", "spanish" ,"swedish"], label= "Entrez votre langue :")
with open("dict_language_encoding.pkl", "rb") as f:
    unpickler = pickle.Unpickler(f)
    new_dict_language = unpickler.load()


mobile_input = gr.Radio(choices = [0,1], label= "Entrez le statut Mobile {1:Pour une demande à partir d'un mobile, 0: Pour une demande à partir d'un ordinateur}")


group_input = gr.Radio(["Accar Hotels", "Boss Western", "Chillton Worldwide", "Independant", "Morriott International", "Yin Yang"], label= "Entrez le groupe de l'hôtel où vous souhaitez séjourner :")
with open("dict_group_encoding.pkl", "rb") as f:
        unpickler = pickle.Unpickler(f)
        new_dict_group = unpickler.load()


brand_input = gr.Radio(["8 Premium", "Ardisson", "Boss Western", "Chill Garden Inn", "Corlton", "CourtYord", "Ibas", "Independant", "J.Halliday Inn", "Marcure", "Morriot", "Navatel", "Quadrupletree", "Royal Lotus", "Safitel", "Tripletree"], label= "Entrez la marque de l'hôtel où vous souhaitez séjourner :")
with open("dict_brand_encoding.pkl", "rb") as f:
        unpickler = pickle.Unpickler(f)
        new_dict_brand = unpickler.load()


Parking_input = gr.Radio(choices = [0,1], label= "Entrez si vous souhaitez un hôtel avec des places de parking {1:Avec parking, 0: Sans parking}")
Pool_input = gr.Radio(choices = [0,1], label= "Entrez si vous souhaitez un hôtel avec une piscine {1:Avec piscine, 0: Sans piscine}")
children_policy_input = gr.Radio(choices = [0,1,2], label= "Entrez le statut de la politique concernant les enfants dans l'hôtel {2: si l’hôtel interdit les enfants de moins de 18 ou 21 ans, 1: si l’hôtel interdit les enfants de moins de 12 ans, 0: si l'hôtel autorise les enfants sans restriction}")

# We create the output
output = gr.Textbox()


app = gr.Interface(fn = make_prediction, inputs=[city_input, date_input, language_input, mobile_input, group_input, brand_input, Parking_input, Pool_input, children_policy_input], outputs=output)
app.launch(share=True)
