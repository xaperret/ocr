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


def predict(image_list: List[int], model) -> List[List[float]]:
    """ Guess based on given matrix and model

    Params
    image_list -- 2d list of integer containing the value of the image
    model -- 
    """
    return [[]]


def get_features_labels(images_list: List[Tuple[str, List[int]]]) -> Tuple[List[str], List[int]]:
    """ Return features and labels from given dict

    Params
    images_list -- contains all images and their character they are representing
    """
    features = [i[0] for i in images_list]
    labels = [i[1] for i in images_list]
    return features, labels


def train(features: List[str], labels: List[int], model) -> None:
    """ Train and return current model with given dataset

    Params
    image_list --
    model --
    """
    new_model = tf.keras.Sequential()
    new_model.compile()

    return new_model
