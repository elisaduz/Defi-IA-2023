# Base image from python
FROM python:3.8
# Set up for your local zone an UTC information
ENV TZ=Europe/Paris
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
# Additional librairies
ADD requirements.txt requirements.txt
ADD model.py model.py
ADD gradio_file.py gradio_file.py
ADD Datatrain\TRAIN_requete2_features.csv Datatrain\TRAIN_requete2_features.csv
ADD regrfOpt_model.pkl regrfOpt_model.pkl
ADD dict_city_encoding.pkl dict_city_encoding.pkl
ADD dict_brand_encoding.pkl dict_brand_encoding.pkl
ADD dict_group_encoding.pkl dict_group_encoding.pkl
ADD dict_language_encoding.pkl dict_language_encoding.pkl

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

#CMD ["python3", "model_target.py"]
CMD ["python3", "gradio_file.py"]



