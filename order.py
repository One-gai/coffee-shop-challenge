from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from customer import Customer
    from coffee import Coffee


class Order:

    all_orders = []

    def __init__(self, customer: "Customer", coffee: "Coffee", price: float):
        if customer.__class__.__name__ != "Customer":
            raise TypeError("customer must be a Customer instance")
        self._customer = customer
        
        if coffee.__class__.__name__ != "Coffee":
            raise TypeError("coffee must be a Coffee instance")
        self._coffee = coffee

        if not isinstance(price, float) or not (1.0 <= price <= 10.0):
            raise TypeError("price must be a float between 1.0 and 10.0")
        self._price = price

        Order.all_orders.append(self)

    @property
    def price(self):
            return self._price
        

    @property
    def customer(self):
        return self._customer
    @property
    def coffee(self):
        return self._coffee  
    

   