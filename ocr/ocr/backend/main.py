#!/usr/bin/env python3

import uvicorn
from typing import Optional, List, Set, Dict, Tuple
from fastapi import FastAPI
#import tensorflow as tf
import image_recognition as ir

app = FastAPI(title='TP de Vision Numerique')
model = ir.load_model('model.json')


@app.get('/index')
async def read_root():
    return "hello world"


@app.post('/train')
def train():
    return "bim"


@app.post('/predict')
def predict(data):
    """ 

    Params
    data --
    """
    return "bim"


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
