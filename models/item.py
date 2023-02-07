from typing import List

from pydantic import BaseModel


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
    addedToCart: bool
