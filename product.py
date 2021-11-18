from typing import List


class product:
    def __init__(self, name: str, price: float, description: str, tags: List[str]) -> None:
        self.name = name
        self.price = price
        self.description = description
        self.tags = tags