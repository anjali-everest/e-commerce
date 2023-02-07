# main.py

from typing import Optional
import json

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

class Item(BaseModel):
    id: int
    title: str
    description: str
    price: float
    discountPercentage: float
    rating: float
    stock: float
    brand: str
    category: str
    thumbnail: str
    images: List[str]
    price: float
    tax: Optional[float] = None

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/")
async def get_items():
    f = open('data.json')
    data = json.load(f)
    return data
