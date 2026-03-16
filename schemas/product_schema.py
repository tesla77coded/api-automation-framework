from pydantic import BaseModel
from typing import Dict

import pydantic


class Product(BaseModel):
    name: str
    price: int
    stock: int


class ProductResponse(BaseModel):
    pydantic.root_model = Dict[int, Product]
