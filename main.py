import json

from fastapi import FastAPI
from models.item import Item

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/")
async def get_items():
    f = open('data.json')
    data = json.load(f)
    return data
