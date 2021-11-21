from seller import seller
from shopping_application import shopping_application
from pymongo import MongoClient

from utils import create_customer, create_seller

application = shopping_application(MongoClient(), "ShoppingApplication", "customers", "sellers", "products")
application.print_application_details()

# adding customers
# customer1 = create_customer("Aditya", "Aditya@gmail.com", "Aditya-address", 12345678)
# customer2 = create_customer("Arun", "Arun@gmail.com", "Arun-address", 789101137)
# customer3 = create_customer("Gobi", "Gobi@gmail.com", "gobi-address", 12131415)
# customer4 = create_customer("Michael", "Michael@gmail.com", "michael-address", 16171819)
# customer5 = create_customer("Suresh", "Suresh@gmail.com", "suresh-address", 20212223)

# application.add_customer(customer1)
# application.add_customer(customer2)
# application.add_customer(customer3)
# application.add_customer(customer4)
# application.add_customer(customer5)

# adding sellers
# seller1 = create_seller("seller1", "seller1@gmail.com", 123456)
# seller2 = create_seller("seller2", "seller2@gmail.com", 789012)
# seller3 = create_seller("seller3", "seller3@gmail.com", 345678)
# seller4 = create_seller("seller4", "seller4@gmail.com", 901234)
# seller5 = create_seller("seller5", "seller5@gmail.com", 567890)

# application.add_seller(seller1)
# application.add_seller(seller2)
# application.add_seller(seller3)
# application.add_seller(seller4)
# application.add_seller(seller5)