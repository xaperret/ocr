import tensorflow as tf
from tensorflow.keras.applications.imagenet_utils import decode_predictions
from keras.models import model_from_json
from typing import Optional, List, Set, Dict, Tuple
import json
import os

FILEPATH_DATASETS: str = 'datasets'
STEP = 20


def print_matrix(character: str, matrix: List[List[int]]) -> None:
    """ Print character and matrix

    Params 
    character -- character or symbol drawn on canvas
    matrix -- matrix representing the character
    """
    print("Matrice de taille ", len(matrix), " par ", len(
        matrix[0]), " représentant le charactère ", character)
    for i in matrix:
        print(i, ' taille => ', len(i))


def print_list(character: str, list_element: List[int]) -> None:
    """ Print character and list of integer

    Params
    character -- character or symbol drawn on canvas
    l -- list representing the character
    """
    print("Liste de taille ", len(list_element),
          " représantant le charactère ", character)
    for i in range(0, len(list_element), STEP):
        print(list_element[i:i+STEP], ' taille => ', i)


def matrix_2_list(matrix: List[List[int]]) -> List[int]:
    """ Convert 2d matrix into one list and returns it 

    Params
    matrix -- given 2d matrix to convert
    """
    new_list: List[int] = []
    for i in matrix:
        new_list += i
    return new_list


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
          ", dossier ", FILEPATH_DATASETS + filepath)
    filepath = FILEPATH_DATASETS + filepath
    if(model_to_unload is not None):
        with open(filepath, 'w+') as f:
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
          ", situé dans dossier ", FILEPATH_DATASETS + filepath)
    filepath = FILEPATH_DATASETS + filepath
    return [[]]


def unload_image(matrix: List[List[int]], character: str = '0') -> None:
    """ Unload image to a json file

    Params
    matrix --
    character --
    """
    filepath = FILEPATH_DATASETS + '/' + character + '.json'
    if(not os.path.exists(FILEPATH_DATASETS)):
        print("Dossier n'existe pas")
        os.mkdir(FILEPATH_DATASETS)
    if(not os.path.exists(filepath)):
        print("Fichier n'existe pas")
        with open(filepath, mode='w+') as f:
            json.dump([], f)
            f.close()

    print_matrix(character, matrix)
    new_list = matrix_2_list(matrix)
    print_list(character, new_list)
    jsonImages = json.dumps(new_list)
    with open(filepath, 'r+') as new_file:
        previousData = json.load(new_file)
        previousData.append(jsonImages)
        new_file.seek(0)
        json.dump(previousData, new_file)
        new_file.close()


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
