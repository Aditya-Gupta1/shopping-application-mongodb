from typing import List

class seller:
    
    def __init__(self, name: str, email: str, phone_no: int, inventory: List[dict] = None, rating: int = 0) -> None:
        self.name = name
        self.email = email
        self.phone_no = phone_no
        self.rating = rating
        self.inventory = inventory