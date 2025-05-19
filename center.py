from customer import Customer
from coffee import Coffee
from order import Order


c1 = Customer("Klyv")
Coffee_order1 = Coffee("Mocha")
Order(c1, Coffee_order1 , 9.5)

c2 = Customer("Bob")
Coffee_order2 = Coffee("Cappocino")
Order(c2, Coffee_order2 , 9.5)

print(f"{c2.coffees()[0].name} is for, {Coffee_order2.customers()[0].name}")    
