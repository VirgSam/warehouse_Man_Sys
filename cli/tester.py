from data import personnel, stock
from loader import Loader
from classes import Warehouse, Item, User, Employee

personnel = Loader(model="personnel")
stock = Loader(model="stock")

one = Warehouse(1)
two = Warehouse(2)
one.add_item("anything goes")
print(one.occupancy())
print(two.occupancy())