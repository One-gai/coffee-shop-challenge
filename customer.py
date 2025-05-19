from order import Order


class Customer:
    def __init__(self, name):
        self.name = name


    def orders(self):
         return [order for order in Order.all_orders if order.customer == self]
    
    def coffees(self):
        return list({order.coffee for order in self.orders()})
    
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or (1 <= len(value) <= 15):
            raise TypeError("Must be a string with 1–15 characters")
        self._name = value

    

         