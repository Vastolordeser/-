from company.product import Product
from company.store import Store
from company.warehouse import Warehouse


def warehouse_products():
    iphone = Product("Телефон", 750000, 25)
    laptop = Product("Ноутбук", 120000, 10)
    tablet = Product("Планшет", 50000, 20)
    cable = Product("Кабель", 3000, 50)
    return [iphone, laptop, cable, tablet]
    
def setup_warehouse(warehouse):
    for product in warehouse_products():
        warehouse.add_product(product)

def store_products():
    iphone = Product("Телефон", 90000, 45)
    laptop = Product("Ноутбук", 670000, 15)
    tablet = Product("Планшет", 45000, 23)
    cable = Product("Кабель", 10000, 10)
    return [iphone, laptop, cable, tablet]

def setup_store(store):
    for product in store_products():
        store.add_product(product)

def main():
    warehouse = Warehouse()
    store = Store(summa = 0)
    
    setup_warehouse(warehouse)
    setup_store(store)
    
    print("Товары на складе:")
    warehouse.show_products()
    
    print("Товары в магазине:")
    store.show_products()
    
if __name__ == "__main__":
    main()


