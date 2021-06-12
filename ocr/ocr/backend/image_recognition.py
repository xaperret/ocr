import tensorflow as tf
from tensorflow.keras.applications.imagenet_utils import decode_predictions
from keras.models import model_from_json
from typing import Optional, List, Set, Dict, Tuple
import json

filepathDatasets: str = 'datasets/'


def print_matrix(character: str, matrix: List[List[int]]):
    """ Print character and matrix
    """
    print("Ajout de donnée pour le charactère ", character)
    for i in matrix:
        print(i)


def load_model(filepath: str = ''):
    """ Load and return given model

    Params
    filepath -- path to the given model to load
    """
    if(filepath == ''):
        model = tf.keras.applications.MobileNetV2(weights="imagenet")
    else:
        with open(filepath, 'r') as f:
            model = model_from_json(f.read())
    print("Chargement du modèle")
    return model


def unload_model(model_to_unload, filepath: str = 'model.json'):
    """ Unload model into given filepath

    Params
    model_to_unload -- keras model to save
    filepath -- place to save the model
    """
    print("Déchargement du modèle dans fichier ", filepath,
          ", dossier ", filepathDatasets + filepath)
    filepath = filepathDatasets + filepath
    if(model_to_unload is not None):
        with open(filepath, 'w') as f:
            f.write(model_to_unload)
    else:
        print("Problème avec le modèle")


def load_images(filepath: str = '') -> List[List[int]]:
    """ Load images from

    Params
    filepath --
    """
    if(filepath == ''):
        print("Le fichier n'a pas été donnée")
        return [[]]

    print("Chargement du modèle depuis fichier ", filepath,
          ", situé dans dossier ", filepathDatasets + filepath)
    filepath = filepathDatasets + filepath
    return [[]]


def unload_image(matrix: List[List[int]], character: str = '0') -> bool:
    """ Unload image to a file

    Params
    matrix --
    character --
    """
    print_matrix(character, matrix)
    #filepath = filepathDatasets + '/' + character + '.json'
    #jsonImages = json.dumps(matrix)
    # with open(filepath) as f:
    #    f.write(jsonImages)
    return True


def predict(matrix: List[List[int]], model):
    """ Guess based on given matrix and model

    Params
    matrix -- 2d list of integer containing the value of the image
    model -- 
    """
    return ""


def train(matrix: List[List[int]], model):
    """ Train and return current model with given dataset

    Params
    matrix --
    model --
    """
