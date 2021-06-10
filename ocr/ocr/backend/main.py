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
    content: List[List[int]]


@app.get("/")
async def read_root():
    return FileResponse('frontend/index.html')


@app.get("/train")
def read_item():
    return {"hello": "world"}


@app.put("/train")
def update_item():
    return {"hello": "world"}


@app.post('/train')
async def train(item: Item):
    print(item)
    return item


@app.post('/predict')
def predict(data):
    return "bim"


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)
    app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")
