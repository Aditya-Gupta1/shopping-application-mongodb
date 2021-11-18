from typing import List
from customer import customer
from seller import seller
from product_information import product_information

def create_customer(name: str, email: str, address: str, phone_no: int, orders: List[str] = None) -> customer:
        return customer(name, email, address, phone_no, orders)

def create_seller(name: str, email: str, phone_no: int, inventory: List[product_information] = None, rating: int = 0) -> seller:
        return seller(name, email, phone_no, inventory, rating)