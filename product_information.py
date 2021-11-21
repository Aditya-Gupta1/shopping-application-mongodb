from bson.objectid import ObjectId
from product import product

class product_information:
    def __init__(self, product_id: ObjectId, quantity: int) -> None:
        self.product_id = product_id
        self.quantity = quantity