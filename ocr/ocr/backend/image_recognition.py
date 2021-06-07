import tensorflow as tf
from tensorflow.keras.applications.imagenet_utils import decode_predictions
from keras.models import model_from_json
from typing import Optional, List, Set, Dict, Tuple


def load_model(filepath: str = ''):
    """ Load and return given model

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

    model_to_unload -- keras model to save
    filepath -- place to save the model
    """
    print("Déchargement du modèle dans fichier ", filepath)
    if(model_to_unload is not None):
        with open(filepath, 'w') as f:
            f.write(model_to_unload)
    else:
        print("Problème avec le modèle")


def predict(matrix: List[List[int]], model):
    """ Guess based on given matrix and model

    matrix -- 2d list of integer containing the value of the image
    model -- 
    """
    return ""
