from data import personnel, stock
from loader import Loader
#from classes import Warehouse, Item, User, Employee
#from query_v04 import get_user_name, search_and_order_item

# personnel = Loader(model="personnel")
# stock = Loader(model="stock")

# one = Warehouse(1)
# two = Warehouse(2)
# one.add_item("anything goes")
# print(one.occupancy())
# print(two.occupancy())

#get_user_name()
#search_and_order_item("High quality Game console")
import re

def list_items_by_one_warehouse(num):
    wh = [f"{item['state']} {item['category']}" for item in stock if item['warehouse'] == num]
    return wh

def max_warehouse():
    return max([item['warehouse'] for item in stock])

def list_items_by_warehouse():
        number_of_warehouses = max_warehouse()
        print(number_of_warehouses)
        warehouses_dict = {}
        for wh_num in range(1, number_of_warehouses + 1):
            wh = list_items_by_one_warehouse(wh_num)
            warehouses_dict[f"total_items_wh{wh_num}"] = len(wh)
            # items_in_warehouses = set(warehouse1) | set(warehouse2)
            # print_items(set(wh))
        for key, amount in warehouses_dict.items():
            wh_num = re.findall('\d+', key)[0]
            print(f'Warehouse {wh_num}:', warehouses_dict[key])
            
        print('Thank you for your visit!')

