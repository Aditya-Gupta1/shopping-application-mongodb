from seller import seller
from shopping_application import shopping_application
from pymongo import MongoClient

from utils import create_customer, create_product, create_seller

application = shopping_application(MongoClient(), "ShoppingApplication", "customers", "sellers", "products")
# application.reset_application()

# adding customers
customer1 = create_customer("Aditya", "Aditya@gmail.com", "Aditya-address", 12345678)
customer2 = create_customer("Arun", "Arun@gmail.com", "Arun-address", 789101137)
customer3 = create_customer("Gobi", "Gobi@gmail.com", "gobi-address", 12131415)
customer4 = create_customer("Michael", "Michael@gmail.com", "michael-address", 16171819)
customer5 = create_customer("Suresh", "Suresh@gmail.com", "suresh-address", 20212223)

application.add_customer(customer1)
application.add_customer(customer2)
application.add_customer(customer3)
application.add_customer(customer4)
application.add_customer(customer5)

# adding sellers
seller1 = create_seller("seller1", "seller1@gmail.com", 123456)
seller2 = create_seller("seller2", "seller2@gmail.com", 789012)
seller3 = create_seller("seller3", "seller3@gmail.com", 345678)
seller4 = create_seller("seller4", "seller4@gmail.com", 901234)
seller5 = create_seller("seller5", "seller5@gmail.com", 567890)

application.add_seller(seller1)
application.add_seller(seller2)
application.add_seller(seller3)
application.add_seller(seller4)
application.add_seller(seller5)

# adding products
product1 = create_product("Book", 700, "Loreum Ipsum", ["non-fiction", "self-help"])
product2 = create_product("Keyboard", 500, "beyboard with backlight", ["accessories", "hardware", "gadgets"])
product3 = create_product("T-Shirt", 400, "Red coloured t-shirt", ["clothing", "topwear"])
product4 = create_product("Lamp", 1000, "Designer Lamp", ["home-decor", "aesthetic"])
product5 = create_product("Charger", 1100, "A laptop charger", ["accessories", "cables"])
product6 = create_product("Table", 2000, "Work Table", ["Furniture"])

application.add_product(product1)
application.add_product(product2)
application.add_product(product3)
application.add_product(product4)
application.add_product(product5)
application.add_product(product6)

# add products to inventory
application.add_to_inventory("seller1@gmail.com", "Book", 5)
application.add_to_inventory("seller2@gmail.com", "Keyboard", 10)
application.add_to_inventory("seller3@gmail.com", "T-Shirt", 20)
application.add_to_inventory("seller4@gmail.com", "Lamp", 5)
application.add_to_inventory("seller5@gmail.com", "Charger", 100)
application.add_to_inventory("seller1@gmail.com", "Table", 5)

# update customer details
application.update_customer_details("Suresh@gmail.com", address= "Suresh-updated-address-3", phone_no= 563234)

# update seller details
application.update_seller_details("seller1@gmail.com", 987655)

# delete customer details
application.delete_customer("Gobi@gmail.com")

# delete seller details
application.delete_seller("seller1@gmail.com")

# update inventory
application.increment_product_count("seller2@gmail.com", "Keyboard", 1)
application.decrease_product_count("seller2@gmail.com", "Keyboard", 1)

# application.print_application_details()