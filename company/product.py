class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def __str__(self):
        return self.name + "(цена: " + str(self.price) + ", количество :" + str(self.quantity) + ")"
  
