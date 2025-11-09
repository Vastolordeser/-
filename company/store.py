from company.product import Product

class Store:
        
    def __init__(self, summa):
        self.summa = summa
        self.products = []
        
    def show_summa(self):
        print("Баланс магазина: ", str(self.summa))
        
    def add_product(self, product):
        self.products.append(product)
        print("В магазин был поставлен товар " + product.name)
    
    def show_products(self):
        print("Сейчас в магазине данные товары:")
        if not self.products:
            print("В магазине нету товаров!")
        else:
            for product in self.products:
                print("--", product)
                
    def sell_product(self, name, quantity):
        for product in self.products:
            if product.name == name:
                if product.quantity >= quantity:
                    total = product.price * quantity
                    product.quantity = product.quantity - quantity
                    self.summa += total
                    print("Было продано", quantity, "количество штук", name, "на сумму", total, "!")
                    return
                else:
                    print("Мало товаров на продажу")
                    return
        print("Товар не найден...")
                    
