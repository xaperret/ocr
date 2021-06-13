#!/usr/bin/env python3
"""Does all the ai training and prediction using image_recognition as helper to open/close read/write json files

"""

import json
from typing import Dict, List, Optional, Set, Tuple

import numpy as np
import tensorflow as tf
from keras.models import model_from_json
from keras.layers import Activation, Dense
from tensorflow import keras
from tensorflow.keras.applications.imagenet_utils import decode_predictions

import image_recognition as ir

__author__ = "Xavier Perret"
__email__ = "xavier.perret@etu.hesge.ch"
__date__ = "12/06/2021"

MODEL_FILENAME: str = 'wow_much_model'
CANVAS_SIZE: int = 400
NEURAL_NUMBER: int = 150
CHARACTER_NUMBER: int = 10
CHARACTER_LIST = "0123456789"
EPOCHS: int = 3  # number of time we train model on our data set


def predict(image_list: List[int], model) -> List[List[float]]:
    """ Guess based on given matrix and model

    Params
    image_list -- 2d list of integer containing the value of the image
    model --
    """
    return [[]]


def get_features_labels(images_list: List[Tuple[str, List[int]]]) -> Tuple[List[str], List[List[int]]]:
    """ Return features and labels from given list of tuples containing characters and their data

    Params
    images_list -- contains all images and their character they are representing

    Returns
    Tuple(labels:str, features:matrice de int)
    """
    labels: List[str] = []
    features: List[List[int]] = [[]]
    for element in images_list:
        label, feature = element
        labels.append(label)
        features.append(feature)

    labels.pop(0)
    features.pop(0)
    return labels, features


def convert_characters(labels: List[str], features: List[List[int]]) -> Tuple[np.ndarray, np.ndarray]:
    """ Code labels and convert labels and features into np.ndarray and returns them

    Params
    labels -- list of characters to be encoded
    features -- corresponding data to be converted to np.ndarray

    Return
    labels, features as np.ndarray
    """
    print("convert_characters")
    character_coding: np.array = np.zeros(CHARACTER_NUMBER)
    characters_coding: np.ndarray = np.ndarray(
        [CHARACTER_NUMBER, len(labels)])
    index: int = 0
    for i, char in enumerate(labels):
        index = CHARACTER_LIST.find(char)
        character_coding[index] = 1
        for j in range(0, len(character_coding)):
            characters_coding[j, i] = character_coding[j]
        character_coding[index] = 0
    print("  -> convert_characters: result of operation is ", characters_coding)
    return characters_coding, np.array(features)


def train(labels: List[str], features: List[List[int]], model: tf.keras.Model) -> tf.keras.Model:
    """ Create and train a model with given dataset and returns it

    Params
    image_list --
    model --
    """
    print("train")
    model.add(Dense(CANVAS_SIZE))
    model.add(Dense(NEURAL_NUMBER, activation='relu'))
    model.add(Dense(CHARACTER_NUMBER, activation='softmax'))
    model.compile(
        optimizer='rmsprop', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    print("  -> train summary")
    model.fit(features, labels, epochs=EPOCHS,
              batch_size=len(features))
    model.summary()
    ir.unload_model(model, MODEL_FILENAME)

    return model
