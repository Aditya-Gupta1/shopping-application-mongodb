from typing import List

from bson.objectid import ObjectId
from customer import customer
from product import product
from seller import seller

def create_customer(name: str, email: str, address: str, phone_no: int, orders: List[str] = None) -> customer:
        return customer(name, email, address, phone_no, orders)

def create_seller(name: str, email: str, phone_no: int, inventory: List[dict] = [], rating: int = 0) -> seller:
        return seller(name, email, phone_no, inventory, rating)

def create_product(name: str, price: float, description: str, tags: List[str]) -> product:
        return product(name, price, description, tags)