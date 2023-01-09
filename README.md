# Defi-IA-2023
Mettre le lien de download avec .sh
https://sites.google.com/site/gdocs2direct/


Vous pourrez trouver sur ce répertoire l'ensemble de nos résultats dans le cadre du Défi IA 2023 : 1001 Nights ! (https://www.kaggle.com/competitions/defi-ia-2023).

Listes des fichiers présents sur ce répertoire : 
* train.py : code d'entrainement de notre modèle
* app.py : code pour lancer l'application Gradio pour tester notre modèle 
* Analysis.ipynb : notebook contenant les analyses exploratoires que nous avons pu faire sur le jeu de données d'entrainement que nous avons créé et le jeu de données de test ainsi que les résultats d'interprétabilité sur notre modèle
* Dockerfile : fichier Dockerfile qui permet de construire une image docker de notre application
* Log_price_RF.ipynb : fichier où nous faisons une prédiction du logarithme du prix des hotels à l'aide d'un modèle de Random Forest suivi de la partie submission de nos résultats pour connaitre notre score sur Kaggle  
* regrfOpt_model.pkl : fichier contenant les poids et biais de notre modèle Random Forest déjà entrainé
* dict_brand_encoding.pkl : fichier contenant un dictionnaire des valeurs des marques d'hôtel après encodage
* dict_group_encoding.pkl : fichier contenant un dictionnaire des valeurs des groupes d'hôtel après encodage
* dict_language_encoding.pkl : fichier contenant un dictionnaire des valeurs des langues d'utilisateurs après encodage
* dict_city_encoding.pkl : fichier contenant un dictionnaire des valeurs des villes où sont les hôtels après encodage
...

Nous avons obtenu, grâce à nos codes et méthodes, un score de ... sur les données de test présentes sur le site Kaggle.

Etapes à suivre pour utiliser et lancer les différents codes développés : 

* Lancer un terminal  
* Cloner le github `git clone https://github.com/elisaduz/Defi-IA-2023.git`
* Aller sur le repertoire : `cd defi ia 2023`
* Télécharger le modèle : `Mettre modèle`
* Faire `docker build -t image1 .`
* Créé un containeur docker dans le dossier où nous avons cloné le github : `docker run -it –-name container1 image1`
* Sortir du container : `exit` 
* Copier le github dans un container : `docker cp . container1:/hotel/`
* Lancer le container : `docker start container1`
* Aller dans le container : `docker attach container1`
* Aller dans le dossier 'hotel' : `cd hotel`

Vous pouvez maintenant lancer les différents programme que nous avons développé : 

* Faire `python app.py` si vous voulez lancer l'application Gradio pour tester notre modèle en choisissant vous même les paramètres de votre utilisateur
* Faire `python train.py` si vous voulez lancer le code d'entrainement de notre modèle (Random Forest)
