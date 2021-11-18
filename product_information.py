from product import product

class product_information:
    def __init__(self, product: product, quantity: int) -> None:
        self.product = product
        self.quantity = quantity