"""Command line interface to query the stock.

To iterate the source data you can use the following structure:

for item in warehouse1:
    # Your instructions here.
    # The `item` name will contain each of the strings (item names) in the list.
"""

from data import warehouse1, warehouse2

# YOUR CODE STARTS HERE

# Get the user name
name = input("Please enter your Name: ")
# Greet the user
print(f"Hello {name} welcome to the Warehouse Management System: ")

# Show the menu and ask to pick a choice
print("User Menu: Please select between options 1-3: ")
print("1. List items by warehouse", "2. Search an item and place an order", "3. Quit", sep='\n')
choice = int(input("Enter option: "))

# If they pick 1
if choice==1:
    print("*****Warehouse 1 inventory:***** ")
    print()
    for item in warehouse1:
        print(item, sep='\n')
    print()
    print("*****Warehouse 2 inventory:***** ")
    for item in warehouse2:
        print(item, sep='\n')

# Else, if they pick 2
elif choice==2:
    user_item = input("Please input the item of your choice: ")
    total_warehouse = warehouse1 + warehouse2
    
    for item in total_warehouse:
        item_count= total_warehouse.count(user_item)
    print(f"Total number of {user_item} in both warehouses: {item_count}")
    for item in warehouse1:
        item_count= warehouse1.count(user_item)
    print(f"Total number of {user_item} in warehouse 1 is : {item_count}")
    for item in warehouse2:
        item_count= warehouse2.count(user_item)
    print(f"Total number of {user_item} in warehouse 2 is : {item_count}")  
    if user_item in warehouse1  and  warehouse2:
        print(f"{user_item} is located in both Warehouses.")
        if warehouse1.count(user_item)>warehouse2.count(user_item):
            print(f"{user_item} has a higher amount of inventory in Warehouse 1 with {warehouse1.count(user_item)} units.")
        else:
            print(f"{user_item} has a higher amount of inventory in Warehouse 2 with {warehouse2.count(user_item)} units.")
    elif user_item in warehouse1 and not warehouse2:
        print(f"{user_item} is located only in Warehouse 1.")
    elif user_item in warehous2 and not warehouse1:
        print(f"{user_item} is located only in Warehouse 2.")
    elif user_item not in warehous1 and warehouse2:
        print(f"{user_item} is not in stock.")
    buy_sig=input("Would you like to place an order? choose option Y/N: ")
    buy_sig = buy_sig.lower()
    if buy_sig=="n":
        print(f" Thank you for your visit {name}, wishing you a plesant day.")
    elif buy_sig=="y":
        num_prod = int(input(f"how many units of {user_item} would you like to purchase. "))


elif choice==3:
    pass

else:
    print("Error incorrect option selected: ")
# Else, if they pick 3
#
# Else

# Thank the user for the visit
