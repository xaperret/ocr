#!/usr/bin/env python3
"""Main module providing routes and server

"""

from typing import Dict, List, Optional, Set, Tuple
import numpy as np

import tensorflow as tf
import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from starlette.responses import FileResponse

import image_recognition as ir
import image_prediction as ip

__author__ = "Xavier Perret"
__email__ = "xavier.perret@etu.hesge.ch"
__date__ = "12/06/2021"

FOLDER_MODEL: str = 'model'
FILENAME_MODEL: str = 'model.json'

app = FastAPI(title='TP3 de vision numérique')


class Item(BaseModel):
    title: str
    content: List[List[int]]


@app.post('/add')
async def add(item: Item):
    print("main.py => add -> received char ",
          item.title, " and content \n ")
    ir.print_matrix(item.title, item.content)
    features = ir.matrix_2_list(item.content)
    print("main.py => add -> converted to list\n")
    ir.print_list(item.title, features)
    res = ir.unload_image(features, item.title)


@app.post('/train')
def train():
    print("ROUTES => app. post/train")
    print("  -> Training model from images list")
    training_list = ir.load_images()
    labels, features = ip.get_features_labels(training_list)
    labels, features = ip.convert_characters(labels, features)
    model = tf.keras.Sequential()
    ip.train(labels, features, model)
    return


@app.post('/predict')
async def predict(item: Item):
    print("Trying to predict image using model")
    print(item)
    model = ir.load_model()
    if(model == None):
        print("Model wasn't created, initiating model by calling train")
        train()
    features = ir.matrix_2_list(item.content)
    print(len(features))
    features = np.array(features)
    features = np.reshape(features, [1, 400])
    print(features.shape)
    print(features)
    res = model.predict(features)
    for i in res:
        for j, element in enumerate(i):
            print(j, ':', element)
    return item


@app.delete('/deleteModel')
def delete_model():
    print("Deleting models")
    if(ir.delete_model()):
        print("Model successfully deleted")
    else:
        print("Model already deleted or wrong path")


@app.delete('/deleteDatasets')
def delete_dataset():
    print("Deleting dataset")
    if(ir.delete_model()):
        print("Datasets successfully deleted")
    else:
        print("Datasets already deleted or wrong path")


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)
