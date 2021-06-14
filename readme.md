# Laboratoire 3 de vision numérique : OCR

## Général

J'ai choisi de détecter les chiffres (de 0 à 9) et pas les caractères.

## Pré-requis

- Poetry
- Docker-Compose

## Déploiement

### Front-end

Ayant eu des gros problèmes en essayant de faire fonctionner le serveur statique de fastapi.
J'ai décidé d'utiliser docker-compose et de créer un simple fichier de configuration pour
servir le front-end avec docker compose.

Donc pour lancer le front-end

```console
cd ocr/ocr
ls
archive  backend  datasets  docker-compose.yaml  frontend  __init__.py  models.h5
```

Puis, si votre configuration vous permet de ne pas mettre sudo, faites le, mais
je suis personnellement obliger de mettre sudo donc...

```console
sudo docker-compose up
```

Le serveur devrait être lancer. Il suffit après d'accéder à une des deux adresses

- http://localhost:8080/
- http://localhost:8080/index.html

### Back-end

```console
cd ocr/ocr
poetry install
poetry shell
python3 backend/main.py
```

## Notes

### Navigateur

Testé sous Brave Browser(~chromium), Linux.

### Datasets

Les données se trouvent dans le dossier datasets dans un fichier csv nommées datasets, j'ai ajouté un peu plus de 300 dessin (30 par chiffres). Le fichier étant un csv il peut être facilement ouvert et modifiable.  

À chaque fois que l'on appuie sur la touche 'Envoyer' le dessin est envoyer au serveur et ajouté dans ce fichier.  

Si vous voulez supprimer les données il faut le faire à la main.  

### Model

Le modèle est sauvegardé dans le dossier 'ocr/ocr'.  

À chaque fois que l'on appuye sur 'Predict' le modèle est chargé depuis le fichier et fait une prédiction sur les données, le résultat est imprimé dans la console et s'affiche sous la forme d'un graphe sur le frontend.

### Training

Lorsque l'on appuye sur la touche train, le backend charge toutes les données se trouvant dans le fichier csv et entraine le modèle. Il écrase l'ancien modèle et sauvegarde les données dans un fichier.

### Config

Dans le fichier image_prediction.py on peut changer en haut

```python
NEURAL_NUMBER: int = 512 # nombre de neurones
EPOCHS: int = 6  # number of time we train model on our data set
```
