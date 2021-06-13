#!/usr/bin/env python3
"""Provide tools to do crud operations on files containing either images or models and provide function to connect backend and keras
"""

import json
import csv
import os
import shutil
from typing import Dict, List, Optional, Set, Tuple

import tensorflow as tf
from keras.models import model_from_json
from tensorflow import keras
from tensorflow.keras.applications.imagenet_utils import decode_predictions

__author__ = "Xavier Perret"
__email__ = "xavier.perret@etu.hesge.ch"
__date__ = "12/06/2021"

FILEPATH_DATASETS: str = 'datasets'
FILEPATH_MODELS: str = 'model'  # don't put precious folder @see delete_model()
FILENAME_MODEL: str = 'model.json'
STEP = 20
CHARACTER_LIST = "0123456789"
HEADER_ROW: List[str] = ["Character"] + [str(i) for i in range(0, 20)]


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


def print_list_tuple(training_material: List[Tuple[str, List[int]]]) -> None:
    """ Print given list of tuples containing the symbol and the data representing
    the symbol

    Params
    training_material -- is the list of tuples
    """
    print("print_list_tuple")
    for i, element in enumerate(training_material):
        print("  -> print_list_tuple element number ", i, " => ", element)


def matrix_2_list(matrix: List[List[int]]) -> List[int]:
    """ Convert 2d matrix into one list and returns it

    Params
    matrix -- given 2d matrix to convert
    """
    print("matrix_2_list")
    new_list: List[int] = []
    for i in matrix:
        new_list += i
    return new_list


def load_model(filepath: str = '') -> None:
    """ Load and return given model

    TODO this shit

    Params
    filepath -- path to the given model to load
    """
    print("load_model")
    filepath = FILEPATH_MODELS + '/' + filepath
    if(not os.path.exists(filepath)):
        print("  -> load_model: model does not exist or path is incorrect")
        return None
    model = keras.models.load_model(filepath)
    return model


def unload_model(model_to_unload, filepath: str = 'model') -> None:
    """ Unload model into given filepath

    TODO this shit

    Params
    model_to_unload -- keras model to save
    filepath -- name of file
    """
    print("unload_model")
    if(not os.path.exists(FILEPATH_MODELS)):
        os.mkdir(FILEPATH_MODELS)
    model_to_unload.save(FILEPATH_MODELS + '/' + filepath)


def load_images() -> List[Tuple[str, List[int]]]:
    """ Return all datasets from datasets according to CHARACTER_LIST

    the name of a file in datasets will be 'a.json' where a is
    the character of the given symbol
    """
    print("load_images")
    training_material: List[Tuple[str, List[int]]] = []
    images_list: List[List[int]]
    filepath: str = ""
    for i, character in enumerate(CHARACTER_LIST):
        filepath = FILEPATH_DATASETS + '/' + character + '.json'  # datatsets/0.json
        images_list = load_image(filepath)  # load list of images of filepath
        for element in images_list:
            if(element):  # list not empty
                training_material.append((character, element))

    return training_material


def load_image(filepath: str = '') -> List[List[int]]:
    """ Load one given images from givenfile

    Params
    filepath -- place to look for the file
    """
    print("load_image")
    drawings_data: List[List[int]] = []
    if(not os.path.exists(filepath)):
        print('error load_image, file does not exist')
        return [[]]
    return drawings_data


def unload_image(drawing: List[int], character: str = '0') -> None:
    """ Unload image to a json file

    Params
    matrix -- 2d list of integer to append to file
    character --
    """
    print("unload_image")
    filepath = FILEPATH_DATASETS + '/' + 'datasets.csv'
    data: List[str] = []
    if(not os.path.exists(FILEPATH_DATASETS)):
        print("Dossier n'existe pas")
        os.mkdir(FILEPATH_DATASETS)
    if(not os.path.exists(filepath)):
        print("Fichier n'existe pas")
        with open(filepath, mode='w+', encoding='UTF-8') as f:
            writer = csv.writer(f)
            writer.writerow(HEADER_ROW)

    with open(filepath, 'a', encoding='UTF-8', newline='')as f:
        writer = csv.writer(f)
        drawing_str = list(map(str, drawing))
        data = [character] + drawing_str
        print("unload_image -> adding data:\n", data)
        writer.writerow(data)


def delete_model() -> bool:
    """ Delete model

    Return
    True on deletion
    """
    print("delete_model")
    if(not os.path.exists(FILEPATH_MODELS)):
        print("  -> delete_model : file already deleted")
        return False
    shutil.rmtree(FILEPATH_MODELS)
    return True


def delete_datasets() -> bool:
    """ Delete datasets

    Return
    True on deletion
    """
    print("delete_datasets")
    if(not os.path.exists(FILEPATH_DATASETS)):
        print("  -> delete_dataset : file already deleted")
        return False
    shutil.rmtree(FILEPATH_DATASETS)
    return True
