"""Command line interface to query the stock.

To iterate the source data you can use the following structure:

for item in warehouse1:
    # Your instructions here.
    # The `item` name will contain each of the strings (item names) in the list.
"""

from data import warehouse1, warehouse2

# YOUR CODE STARTS HERE
def goodbye():
    print(f"Thank you for your visit {name}, wishing you a plesant day.")

def user_menu():
    # Show the menu and ask to pick a choice
    print("User Menu: Please select between options 1-3: ")
    print("1. List items by warehouse", "2. Search an item and place an order", "3. Quit", sep='\n')
    

def option1():
    print()
    print("*****Warehouse 1 inventory:***** ")
    print()
    for item in warehouse1:
        print("-", item)
    print()
    print("*****Warehouse 2 inventory:***** ")
    print()
    for item in warehouse2:
        print("-",item)

def item_counter(warehouse:list, location:str)->None:
    for item in warehouse:
        item_count=warehouse.count(user_item)
    print(f"Total number of {user_item}s {location}: {item_count}")

def option2():
    total_warehouse = warehouse1 + warehouse2

    locationt= "in both warehouses"
    location1= "in Warehouse 1 is "
    location2= "in Warehouse 2 is "
    
    item_counter(total_warehouse,locationt)
    item_counter(warehouse1,location1) 
    item_counter(warehouse2,location2)  
        
    if user_item in warehouse1:
        if user_item in warehouse2:
            print(f"{user_item} is located in both Warehouses.")
    elif user_item in warehouse1:
        if not user_item in warehouse2:
            print(f"{user_item} can only be found in one Warehouse.")       
    if warehouse1.count(user_item)>warehouse2.count(user_item):
        print(f"{user_item} has a higher amount of inventory in Warehouse 1 with {warehouse1.count(user_item)} units.")
    if warehouse2.count(user_item)>warehouse1.count(user_item):
        print(f"{user_item} has a higher amount of inventory in Warehouse 2 with {warehouse2.count(user_item)} units.")
    
    if not user_item in warehouse1:
        if not user_item in warehouse2:
            print(f"{user_item} is Not in stock") 
    else: 
        buy_sig=input("Would you like to place an order? choose option Y/N: ") 
        buy_sig = buy_sig.lower()
        if buy_sig=="n":
            goodbye()
        elif buy_sig=="y":
            num_prod = int(input(f"how many units of {user_item} would you like to purchase. ")) # closing the trxn should fall under this else statement.
            if num_prod<=(warehouse1.count(user_item)+warehouse2.count(user_item)):
                print(f"An order has been placed for item: { user_item } Quantity: {num_prod}")
                goodbye()
            else:
                print("Unfortunately we do not have enough stock to complete this transaction. ")
                print("Please return to the user menu if you wish to amend your order. ")
                goodbye()
    



# Get the user name
name = input("Please enter your Name: ")
# Greet the user
print(f"Hello {name} welcome to the Warehouse Management System: ")
user_menu()
choice = int(input("Enter option: "))

# If they pick 1
if choice==1:
    option1()
    

# Else, if they pick 2
elif choice==2:
    user_item = input("Please input the item of your choice: ")
    option2()
    
# Else, if they pick 3
# Thank the user for the visit
elif choice==3:
    goodbye()
# Else
else:
    print("Error incorrect option selected: ")





