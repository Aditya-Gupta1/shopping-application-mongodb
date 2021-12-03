# Shopping Application MongoDB Database

A MongoDB database for a shopping application.

3 collections:
* Customers
* Sellers
* Products

Design can be found in the file `Design.tldr`.

### Features

* Add a customer.
* Add a seller.
* Add a product.
* Add a product to the inventory of a seller.
* Update customer info.
* Update seller info
* Delete a customer.
* Delete a seller.
* Schema validation for customers, sellers and products.

### To-do
* Update seller inventory.
* Add an order to customer.

### Assumptions

1. Every product has a unique name.
2. All sellers and customers have a unique email.
3. Only address and phone no of customers can be edited.
4. Only seller phone no can be edited.