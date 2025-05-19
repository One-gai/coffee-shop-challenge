from order import Order

class Coffee:

    def __init__(self, name):
    
        if isinstance(name, str):
            
            raise TypeError("Name must be a string")
        if len(name) < 3:
            
            raise TypeError("Name must be longer than 3 characters")
        self._name = name

    def orders(self):
         return [order for order in Order.all_orders if order.coffee == self]
    
    def customers(self):
        return list({order.customer for order in self.customers()})



    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise AttributeError("You can not change your order.")




    

