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
* features_hotels.csv : fichier contenant des méta-données pour chacun des 999 hôtels
* test_set.csv : fichier contenant le jeu de données de test
* submission.csv : fichier de submission
* requetes.ipynb : fichier permettant de faire des requêtes

Nous avons obtenu, grâce à nos codes et méthodes, un score de 22.25 sur les données de test présentes sur le site Kaggle.

Etapes à suivre pour utiliser et lancer les différents codes développés : 

* Lancer un terminal  
* Cloner le github `git clone https://github.com/elisaduz/Defi-IA-2023.git`
* Aller sur le repertoire : `cd defi ia 2023`
* Télécharger le modèle : `https://drive.google.com/uc?export=download&id=1K0drq_wgzg2vjNhk9ja7zlZp43VYAHMG`
* Faire `docker build -t image1 .`
* Créé un containeur docker dans le dossier où nous avons cloné le github : `docker run -it –-name container1 image1`
* Sortir du container : `exit` 
* Copier le github dans un container : `docker cp . container1:/hotel/`
* Lancer le container : `docker start container1`
* Aller dans le container : `docker attach container1`
* Aller dans le dossier 'hotel' : `cd hotel`

Vous pouvez maintenant lancer les différents programmes que nous avons développé : 

* Faire `python3 app.py` et copier-coller dans un navigateur le lien public qui apparait à la suite de `"Running on public URL"` si vous voulez lancer l'application Gradio pour tester notre modèle en choisissant vous même les paramètres de votre utilisateur
* Faire `python3 train.py` si vous voulez lancer le code d'entrainement de notre modèle (Random Forest)
