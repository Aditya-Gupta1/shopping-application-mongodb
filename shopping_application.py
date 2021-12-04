from collections import OrderedDict
from pymongo import MongoClient
from pymongo.command_cursor import CommandCursor
from pymongo.message import _MODIFIERS
from pymongo.results import UpdateResult
from customer import customer
from product import product
from seller import seller
import json

class shopping_application:

    def __init__(self, client: MongoClient, db_name: str, customer_coll: str, seller_coll: str, products_coll: str) -> None:
        self.client = client
        self.db = client.get_database(db_name)

        # creating a new "customers" collection

        # 1. Drop any existing collection with same name
        self.db.drop_collection(customer_coll)
        # 2. Create a new collection
        self.customer_coll = self.db.create_collection(customer_coll)
        # 3. Load the customer validator
        customer_validator_file = open("validators\customer_validator.json")
        customer_validator = json.load(customer_validator_file)
        customer_validator_file.close()
        # 4. Add the validator to sellers collection
        commands = OrderedDict([("collMod", customer_coll), ("validator", customer_validator), ("validationLevel", "moderate")])
        self.db.command(commands)
        print("Customers Collection Created Successfully.")

        # creating a new "sellers" collection

        # 1. Drop any existing collection with same name
        self.db.drop_collection(seller_coll)
        # 2. Create a new collection
        self.seller_coll = self.db.create_collection(seller_coll)
        # 3. Load the seller validator
        seller_validator_file = open("validators\seller_validator.json")
        seller_validator = json.load(seller_validator_file)
        seller_validator_file.close()
        # 4. Add the validator to sellers collection
        commands = OrderedDict([("collMod", seller_coll), ("validator", seller_validator), ("validationLevel", "moderate")])
        self.db.command(commands)
        print("Sellers Collection Created Successfully.")

        # creating a new "products" collection

        # 1. Drop any existing collection with same name
        self.db.drop_collection(products_coll)
        # 2. Create a new collection
        self.products_coll = self.db.create_collection(products_coll)
        # 3. Load the product validator
        product_validator_file = open("validators\product_validator.json")
        product_validator = json.load(product_validator_file)
        product_validator_file.close()
        # 4. Add the validator to products collection
        commands = OrderedDict([("collMod", products_coll), ("validator", product_validator), ("validationLevel", "moderate")])
        self.db.command(commands)
        print("Products Collection Created Successfully.")

    def add_customer(self, customer: customer) -> None:
        self.customer_coll.insert_one(customer.__dict__)

    def add_seller(self, seller: seller) -> None:
        self.seller_coll.insert_one(seller.__dict__)

    def add_product(self, product: product) -> None:
        self.products_coll.insert_one(product.__dict__)

    def add_to_inventory(self, seller_email: str, product_name: str, quantity: int) -> None:
        product_id = self.get_product_id(product_name)
        self.seller_coll.update_one({"email": seller_email}, {"$push": {"inventory": {"product_id": product_id["_id"], "quantity": quantity}}})

    def get_product_id(self, product_name: str):
        return self.products_coll.find_one({"name": product_name}, {"_id": 1, "name": 0, "price": 0, "description": 0, "tags": 0})

    def update_customer_details(self, customer_email: str, address: str = None, phone_no: int = None) -> None:
        if not address and not phone_no:
            print("Provide either an address or a phone no to update.")
            return
        if address and phone_no:
            result: UpdateResult = self.customer_coll.update_one({"email": customer_email}, {"$set": {"address": address, "phone_no": phone_no}})
        elif address:
            result: UpdateResult = self.customer_coll.update_one({"email": customer_email}, {"$set": {"address": address}})
        else:
            result: UpdateResult = self.customer_coll.update_one({"email": customer_email}, {"$set": {"phone_no": phone_no}})
        
        if result.matched_count == 0:
            print(f"No customer with the email {customer_email} is present in DB.")
        elif result.matched_count == 1 and result.modified_count == 0:
            print("Nothing to modify.")
        elif result.matched_count == 1 and result.modified_count == 1 and result.acknowledged:
            print("Customer Details Updated Successfully.")
        else:
            print("Something went wrong while updating.")
    
    def update_seller_details(self, seller_email: str, phone_no: int) -> None:
        result = self.seller_coll.update_one({"email": seller_email}, {"$set": {"phone_no": phone_no}})
        
        if result.matched_count == 1 and result.modified_count == 1 and result.acknowledged:
            print("Seller details updated Successfully.")
        elif result.matched_count == 1 and result.modified_count == 0:
            print("Nothing to modify.")
        elif result.matched_count == 0:
            print("No seller with given email found!")
        else:
            print("Something went wrong while updating.")
    
    def delete_customer(self, customer_email: str) -> None:
        result = self.customer_coll.delete_one({"email": customer_email})
        if result.acknowledged and result.deleted_count == 1:
            print(f"Customer[{customer_email}] deleted successfully.")
        else:
            print("Something went wrong.")
    
    def delete_seller(self, seller_email: str) -> None:
        result = self.seller_coll.delete_one({"email": seller_email})
        if result.acknowledged and result.deleted_count == 1:
            print(f"Seller[{seller_email}] deleted successfully.")
        else:
            print("Something went wrong.")
    
    def increment_product_count(self, seller_email: str, product_name: str, quantity: int = 1) -> None:
        product_details = self.products_coll.find_one({"name": product_name})
        if not product_details:
            print("No product with the given name found")
            return
        product_id = product_details["_id"]
        seller_possible: UpdateResult = self.seller_coll.update_one({"email": seller_email, "inventory.product_id": product_id}, {"$inc": {"inventory.$.quantity": quantity}})
        if seller_possible.acknowledged and seller_possible.matched_count == 1 and seller_possible.modified_count == 1:
            print("Quantity modified successfully.")
        else:
            print("Something went wrong with the details provided.")
    
    def decrease_product_count(self, seller_email: str, product_name: str, quantity: int = 1) -> None:
        product_details = self.products_coll.find_one({"name": product_name})
        if not product_details:
            print("No product with the given name found")
            return
        product_id = product_details["_id"]
        seller_possible: UpdateResult = self.seller_coll.update_one({"email": seller_email, "inventory.product_id": product_id}, {"$inc": {"inventory.$.quantity": (-1*quantity)}})
        if seller_possible.acknowledged and seller_possible.matched_count == 1 and seller_possible.modified_count == 1:
            print("Quantity modified successfully.")
        else:
            print("Something went wrong with the details provided.")

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