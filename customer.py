from order import Order


class Customer:
    def __init__(self, name):
        self.name = name


    def orders(self):
         return [order for order in Order.all_orders if order.customer == self]
    
    def coffees(self):
        return list({order.coffee for order in self.orders()})
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
    def __repr__(self):
        return f"{self.name}"
    
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 15):
            self._name = None
            raise TypeError("Customer Name Must be a string with 1–15 characters")
        self._name = value

    

         