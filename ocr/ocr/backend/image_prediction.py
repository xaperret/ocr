#!/usr/bin/env python3
"""Does all the ai training and prediction using image_recognition as helper to open/close read/write json files

"""

import numpy as np
import tensorflow as tf
from keras.models import model_from_json
from tensorflow import keras
from tensorflow.keras.applications.imagenet_utils import decode_predictions
import json

import image_recognition as ir
from typing import Optional, List, Set, Dict, Tuple

__author__ = "Xavier Perret"
__email__ = "xavier.perret@etu.hesge.ch"
__date__ = "12/06/2021"

CANVAS_SIZE: int = 400
NEURAL_NUMBER: int = 150
CHAR_NUMBER: int = 10
EPOCHS: int = 3


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
    """
    features = [i[1] for i in images_list]
    labels = [i[0] for i in images_list]
    return labels, features


def convert_characters(labels: List[str]) -> List[int]:
    """ Convert characters into the right coding
    """
    return []


def train(labels: List[str], features: List[List[int]], model: tf.keras.Model) -> tf.keras.Model:
    """ Create and train a model with given dataset and returns it

    Params
    image_list --
    model --
    """
    print("train")
    model.add(Dense(CANVAS_SIZE))
    model.add(Dense(NEURAL_NUMBER, activation='relu'))
    model.add(Dense(CHAR_NUMBER, activation='softmax'))
    model.compile(
        optimizer='rmsprop', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    print("  -> train summary")
    model.summary()
    model.fit(features, labels, epochs=EPOCHS,
              batch_size=len(features))

    return model
