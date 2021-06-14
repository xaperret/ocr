#!/usr/bin/env python3
"""Main module providing routes and server

"""

from typing import Dict, List, Optional, Set, Tuple
import numpy as np

import tensorflow as tf
import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import image_recognition as ir
import image_prediction as ip
import json

__author__ = "Xavier Perret"
__email__ = "xavier.perret@etu.hesge.ch"
__date__ = "12/06/2021"

FOLDER_MODEL: str = 'model'
FILENAME_MODEL: str = 'model.json'

app = FastAPI(title='TP3 de vision numérique')

origins = [
    "http://localhost",
    "http://localhost:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
    features = np.array(features)
    features = np.reshape(features, [1, 400])
    res = model.predict(features)[0, :]
    tmp: float = -1
    c_tmp: int = -1
    for i, element in enumerate(res):
        print("char:", i, " => ", " prob:", element)
        if(tmp < element):
            tmp = element
            c_tmp = i
    print("Le plus probable est ", c_tmp)

    res = json.dumps(res.tolist())
    return JSONResponse(content=res)


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
