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

FILENAME_DATASETS: str = 'datasets.csv'
FILEPATH_DATASETS: str = 'datasets'
FILEPATH_MODELS: str = 'model'  # don't put precious folder @see delete_model()
FILENAME_MODEL: str = 'model'
STEP = 20
CHARACTER_LIST = "0123456789"
HEADER_ROW: List[str] = ["Character"] + [str(i) for i in range(0, 400)]


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


def load_model() -> None:
    """ Load and return given model

    TODO this shit

    Params
    filepath -- path to the given model to load
    """
    print("load_model")
    model = tf.keras.models.load_model('models.h5')
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
    training_material: List[Tuple[str, List[int]]] = []  # output
    image_list: List[int]
    filepath: str = FILEPATH_DATASETS + '/' + FILENAME_DATASETS
    character: str = ""
    with open(filepath, 'r') as f:
        csv_reader = csv.reader(f)
        for i, line in enumerate(csv_reader):
            if(i != 0):
                character = line[0]
                image_list = [int(i) for i in line]
                image_list.pop(0)  # remove character
                training_material.append((character, image_list))

    return training_material


def unload_image(drawing: List[int], character: str = '0') -> None:
    """ Unload given drawing representing character to a csv file inside datasets folder

    If the datasets folder does not exist, it will be created
    If the csv file does not exists it will create it and add HEADER_ROW

    Params
    drawing -- list containing the data of the symbol drawn
    character -- is the symbol the drawing is representing
    """
    print("image_recognition.py => unload_image")
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
