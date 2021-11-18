from typing import List
from pymongo import MongoClient
from customer import customer
from product_information import product_information
from seller import seller
import json

class shopping_application:

    def __init__(self, client: MongoClient, db_name: str, customer_coll: str, seller_coll: str, products_coll: str) -> None:
        self.client = client
        self.db = client.get_database(db_name)
        self.customer_coll = self.db.get_collection(customer_coll)
        self.seller_coll = self.db.get_collection(seller_coll)
        self.products_coll = self.db.get_collection(products_coll)

    def add_customer(self, customer: customer) -> None:
        self.customer_coll.insert_one(json.dump(customer.__dict__))

    def add_seller(self, seller: seller) -> None:
        self.seller_coll.insert_one(json.dump(seller.__dict__))

    def create_customer(self, name: str, email: str, address: str, phone_no: int, orders: List[str] = None) -> customer:
        return customer(name, email, address, phone_no, orders)

    def create_seller(self, name: str, email: str, phone_no: int, inventory: List[product_information] = None, rating: int = 0) -> seller:
        return seller(name, email, phone_no, inventory, rating)