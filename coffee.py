from order import Order
from customer import Customer

class Coffee:

    def __init__(self, name):
    
        if not isinstance(name, str):
            
            raise TypeError("Name must be a string")
        if len(name) < 3:
            
            raise TypeError("Name must be longer than 3 characters")
        self._name = name

    def orders(self):
         return [order for order in Order.all_orders if order.coffee == self]
    
    def customers(self):
        return list({order.customer for order in self.orders()})
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        prices = [order.price for order in self.orders()]
        return sum(prices) / len(prices) if prices else 0

    def __repr__(self):
        return f"{self.name}"




    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise AttributeError("You can not change your order.")

   


    

