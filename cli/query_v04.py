"""Command line interface to query the stock.

To iterate the source data you can use the following structure:

for item in warehouse1:
    # Your instructions here.
    # The `item` name will contain each of the strings (item names) in the list.
"""

from data import stock
import datetime
import collections
from itertools import zip_longest

# YOUR CODE STARTS HERE
def get_user_name():
    name = input("Please enter your Name: ")
    return name

def greet_user(name):
    print(f" Hello {name} welcome to the Warehouse Management System: ")
    
def goodbye():
    print(f"Thank you for your visit {name}, wishing you a plesant day.")

def user_menu():
    # Show the menu and ask to pick a choice
    print('1: List all items')
    print('2: search and place order')
    print('3: browse by category')
    print('4: Quit')

def get_user_input():
    user_input = int(input("Choose between 1-4. "))
    return user_input


def list_items_by_warehouse():
    
    if user_input == 1:
        warehouse1 = [ f"{item['state']} {item['category']}" for item in stock if item.get('warehouse') == 1]
        warehouse2 = [ f"{item['state']} {item['category']}" for item in stock if item.get('warehouse') == 2]
        warehouse3 = [ f"{item['state']} {item['category']}" for item in stock if item.get('warehouse') == 3]
        warehouse4 = [ f"{item['state']} {item['category']}" for item in stock if item.get('warehouse') == 4]
        for item in set(warehouse1) | set(warehouse2) | set(warehouse3)| set(warehouse4):
            print('')
            print('-', item)
        print(f"Total items in warehouse1: {len(warehouse1)}")
        print(f"Total items in warehouse2: {len(warehouse2)}")
        print(f"Total items in warehouse3: {len(warehouse3)}")
        print(f"Total items in warehouse4: {len(warehouse4)}")
        print('')
        goodbye()
            

def search_and_order_item():
    
    if user_input == 2:
        item_name = input('What is the name of the item? ')
        wh1 = [item['date_of_stock'] for item in stock if item.get('warehouse') == 1 and f"{item['state']} {item['category']}".lower() == item_name.lower()]
        wh2 = [item['date_of_stock'] for item in stock if item.get('warehouse') == 2 and f"{item['state']} {item['category']}".lower() == item_name.lower()]
        wh3 = [item['date_of_stock'] for item in stock if item.get('warehouse') == 3 and f"{item['state']} {item['category']}".lower() == item_name.lower()]
        wh4 = [item['date_of_stock'] for item in stock if item.get('warehouse') == 4 and f"{item['state']} {item['category']}".lower() == item_name.lower()]
        if len(wh1 + wh2 + wh3 + wh4) == 0:
            print("Amount available: 0")
            print('Location: Not in Stock')
        else:
            today = datetime.datetime.now()
            for item in wh1:
                print(f"- Warehouse1 (in stock {(today - datetime.datetime.strptime(item, '%Y-%m-%d %H:%M:%S')).days} days)")
            for item in wh2:
                print(f"- Warehouse2 (in stock {(today - datetime.datetime.strptime(item, '%Y-%m-%d %H:%M:%S')).days} days)")
            for item in wh3:
                print(f"- Warehouse3 (in stock {(today - datetime.datetime.strptime(item, '%Y-%m-%d %H:%M:%S')).days} days)")
            for item in wh4:
                print(f"- Warehouse4 (in stock {(today - datetime.datetime.strptime(item, '%Y-%m-%d %H:%M:%S')).days} days)")
            
            if len(wh1) > 0 or len(wh2) > 0 or len(wh3) > 0 or len(wh4) > 0:
                wh_d = {len(wh1): 'Warehouse 1', len(wh2): 'Warehouse 2', len(wh3): 'Warehouse 3', len(wh4): 'Warehouse 4'}
                maximum = max(wh_d.keys())
                print(f"Maximum availability: {maximum} in {wh_d[maximum]}")
                

def browse_by_category():
    
    if user_input == 3:
        categories = [item['category'] for item in stock ]
        categories_ct = collections.Counter(categories)
        cat_d = {id: f"{category} ({categories_ct[category]})" for id, category in enumerate(categories_ct, start = 1)}
        print()
        for id, category in cat_d.items():
            print(f"{id}. {category}")
        get_id = int(input('Choose a category'))
        print()
        selected_cat = cat_d[get_id].split(" ")[0]
        print(f'List of {selected_cat} available:')
        wh1 = [ f"{item['state']} {item['category']}" 
        for item in stock if item.get('warehouse') == 1 and item.get('category') == selected_cat]
        wh2 = [ f"{item['state']} {item['category']}" for item in stock if item.get('warehouse') == 2 and item.get('category') == selected_cat] # wrap this into a func and dont hardcode the warehouses as we dont know how many are there seee below
        wh3 = [ f"{item['state']} {item['category']}" for item in stock if item.get('warehouse') == 3 and item.get('category') == selected_cat] # for item in stock if item.get('warehouse') == 2** 
        wh4 = [ f"{item['state']} {item['category']}" for item in stock if item.get('warehouse') == 4 and item.get('category') == selected_cat] # def a func that takes info from warehous num 1 and selected_cat ruturns the value and selected_cat of all the warehouse obj locations 
        print(len(set(wh1)))
        print(len(set(wh2)))
        print(len(set(wh3)))
        print(len(set(wh4)))
        print(list(zip(set(wh1), set(wh2), set(wh3), set(wh4))))
        print(list(zip_longest(set(wh1), set(wh2), set(wh3), set(wh4), fillvalue=False)))
        for item_wh1, item_wh2, item_wh3, item_wh4  in zip_longest(set(wh1), set(wh2), set(wh3), set(wh4), fillvalue=False):
            if item_wh1: print(f"{item_wh1}, warehouse1")
            if item_wh2: print(f"{item_wh2}, warehouse2")
            if item_wh3: print(f"{item_wh3}, warehouse3")
            if item_wh4: print(f"{item_wh4}, warehouse4")
        goodbye()
            

# Get the user name
name = get_user_name()
# Greet the user
greet_user(name)
user_menu()
user_input = get_user_input()

while True:
    # If they pick 1
    if user_input==1:
        list_items_by_warehouse()
        break
    
    # Else, if they pick 2
    elif user_input==2:
    # user_item = input("Please input the item of your choice: ")
        search_and_order_item()
        break
    # Else, if they pick 3
    elif user_input==3:
        browse_by_category()
        break
    # Else, Thank the user for the visit
    elif user_input==4:
        #print(f"{user_input}: is not a valid operation.")
        goodbye()
        break





