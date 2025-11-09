from company.product import Product
 
class Warehouse:
    def __init__(self):
        self.products = []
        
    def add_product(self, product):
        self.products.append(product)
        print("Товар " + product.name + " был добавлен на склад")
      
    def show_products(self):
       print("Содержимое на складе:")
       if not self.products:
           print("На складе ничего нет!")  
       else:
           for product in self.products:
               print(product)
                  
    def remove_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                print("Товар " + name + " был удален со склада.")
                return
        print("Данного товара нету на складе!")
        
        
