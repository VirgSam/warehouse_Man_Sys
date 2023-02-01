from datetime import datetime

class User():
    def __init__(self,user_name:str) -> None:
        self._name = user_name
        self.is_authenticated:bool = False
        pass

    def authenticate(self,password:str) -> False:
        return False

    def is_named(self,name:str) -> bool:
        if self._name == name:
            return True
 
    def greet(self) -> None:
        print(f"Hello, {self._name}")
        print("Welcome to our Warehouse Database.")
        print("If you don't find what you are looking for,")
        print("please ask one of our staff members to assist you.")
        
    def bye(self,actions:list) -> None:
        print(f"Thank you for your visit, {self._name}")
        print("Summary of actions: ")
        print(actions,end='\n')


class Employee(User):
    def __init__(self, user_name: str) -> None:
        super().__init__(user_name)
    
    def greet(self) -> None:
        print(f"Hello, {self._name}")
        print("If you experience a problem with the system,")
        print("please contact technical support.")

    pass


class Item():
    def __init__(self, state:str,category:str, warehouse: int,date_of_stock:datetime) -> None:
        self.state = state
        self.category = category
        self.warehouse = warehouse
        self.date_of_stock = date_of_stock
    
    def __str__(self) -> str:
        return f"Item: {self.state} {self.category}"
        
    def __repr__(self) -> str:
        return f"Item: a {self.state} {self.category} located in Warehouse:{self.warehouse} date of stock: {self.date_of_stock}"


class Warehouse():
    def __init__(self, warehouse_id:int) -> None:
        self.warehouse_id = warehouse_id
        self.stock = []
    def occupancy(self) -> int:
        return f"Occupancy: {len(self.stock)}"
    def add_item(self,item:Item) -> None:
        self.stock.append(item)
    def search(self,item:str) -> list:
        pass