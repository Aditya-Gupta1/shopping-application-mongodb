from typing import List
from pymongo import MongoClient
from customer import customer
from product import product
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
        self.customer_coll.insert_one(customer.__dict__)

    def add_seller(self, seller: seller) -> None:
        self.seller_coll.insert_one(seller.__dict__)

    def add_product(self, product: product) -> None:
        self.products_coll.insert_one(product.__dict__)
    
    def create_product_information(self, product_name: str, quantity: int) -> product_information:
        product_id = self.products_coll.find_one({"name": product_name}, {"_id": 1, "name": 0, "price": 0, "description": 0, "tags": 0})
        if not product_id:
            print("Not present")
            return None
        return product_information(product_id, quantity)
        
    def add_to_inventory(self, seller_email: str, product_info: product_information) -> None:
        self.seller_coll.update_one({"email": seller_email}, {"$push": {"inventory": product_info.__dict__}})
        print(f"Product was added successfully to inventory of the Seller[{seller_email}]")

    def print_application_details(self):
        customers = self.customer_coll.find()
        sellers = self.seller_coll.find()
        products = self.products_coll.find()
        print("Customer Details:")
        for cust in customers:
            print(cust)
        print("Seller Details:")
        for sel in sellers:
            print(sel)
        print("Product Details:")
        for prod in products:
            print(prod)

    def reset_application(self) -> None:
        self.seller_coll.drop()
        self.customer_coll.drop()
        self.products_coll.drop()