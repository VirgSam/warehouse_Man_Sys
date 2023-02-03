from datetime import datetime

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

class User():
    def __init__(self,user_name:str) -> None:
        if not user_name:
            self._name = "Anonymous"
        else:
            self._name = user_name
        self.is_authenticated:bool = False
        # include anonymous as part of constructor
        
    def authenticate(self,password:str) -> False:
        return False

    def is_named(self,name:str) -> bool:
        if self._name == name:
            return True
 
    def greet(self) -> None:
        print(f"""Hello, {self._name}
            Welcome to our Warehouse Database.
            If you don't find what you are looking for,
            please ask one of our staff members to assist you."""
            )
        
    def bye(self,actions:list) -> None:
        print(f"Thank you for your visit, {self._name}")
        #print("Summary of actions: ")
        #print(actions,end='\n')
    
    def __repr__(self) -> str:
        return f"I am {self._name}"


class Employee(User):
    def __init__(self, user_name:str, password:str, head_of:None) -> None:
        super().__init__(user_name)
        self.__password = password
        if head_of == None:
            self.head_of = []
        else:
            self.head_of = head_of
    
    def greet(self) -> None:
        print(f"Hello, {self._name}")
        print("If you experience a problem with the system,")
        print("please contact technical support.")
    
    def authenticate(self,password:str) -> False:
        super().authenticate(password)
        # recursive authentication from class notes
        # get self.name and self.__password
        # iterate over personel objects list and check if self.name__str__ and self.__password are
        if self.__password==password:
            return True
    
    def order(self,item:Item, amount:int):
        self.item = item 
        self.amount = amount 
        return f"{self.item} was ordered, amount ordered: {self.amount}"
    
    def bye(self,actions:list) -> None:
        super().bye()
        print("Summary of actions: ")
        print(actions,end='\n')




em = Employee("Jan","xyz",None)
em2 = Employee("","xyz",None)
print(em2)
print(em)