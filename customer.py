class customer:

    def __init__(self, name: str, email: str, address: str, phone_no: int, orders: List[str]) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.phone_no = phone_no
        self.orders = orders