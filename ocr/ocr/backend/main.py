#!/usr/bin/env python3
import os
from typing import Dict, List, Optional, Set, Tuple

import tensorflow as tf
import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from starlette.responses import FileResponse

import image_recognition as ir


app = FastAPI(title='TP de vision numérique')


class Item(BaseModel):
    title: str
    content: List[List[int]]


try:
    os.mkdir('datasets')
    os.mkdir('models')
except FileExistsError:
    print("Dossier déjà créer, l'erreur est ignorable")

try:
    model = ir.load_model('model.json')
except FileNotFoundError:
    print("Le modèle n'a pas été trouvé dans les fichiers")
    print("Ce n'est pas une erreur grave si c'est le premier lancement")


@app.get("/")
async def read_root():
    return FileResponse('frontend/index.html')


@app.post('/add')
async def add(item: Item):
    ir.unload_image(item.content, item.title)

    return item


@app.post('/train')
def train():
    print("Training model from images list")
    return


@app.post('/predict')
async def predict(item: Item):
    print("Trying to predict image using model")
    print(item)
    return item


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)
    app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")
