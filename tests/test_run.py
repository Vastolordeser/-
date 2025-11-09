import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from company.product import Product
from company.warehouse import Warehouse
from company.store import Store

def show_warehouse(warehouse):
    print("\nДобавляем товары на склад")
    warehouse.add_product(Product("Телефон", 750000, 25))
    warehouse.add_product(Product("Ноутбук", 120000, 10))
    warehouse.add_product(Product("Планшет", 50000, 20))
    warehouse.add_product(Product("Кабель", 500, 50))
    
    print("\nСклад")
    warehouse.show_products() 
    
    print("\nУдаляем 'Ноутбук' со склада")
    warehouse.remove_product("Ноутбук")
    warehouse.show_products()


def show_store(store):
    print("\nДобавляем товары в магазин:")
    store.add_product(Product("Телефон", 87903, 5))
    store.add_product(Product("Ноутбук", 90000, 2))
    print("\nМагазин:")
    store.show_products()
    
def sell_products(store):
    print("\nПродажа товаров в магазине:")
    store.sell_product("Телефон", 2)
    store.show_summa()
    store.sell_product("Ноутбук", 5)
    store.sell_product("Планшет", 1)
    
def main():
    warehouse = Warehouse()
    store = Store(0)
    show_warehouse(warehouse)
    show_store(store)
    sell_products(store)
    
if __name__ == "__main__":
    main()
