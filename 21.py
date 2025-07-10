#Create a class Product with attributes name and price. Create two product objects and display them.
class product:
    def __init__(self,name,price):
        self.name = name
        self.price = price
p2=product("IQOO",31000)
print(p2.price)
print(p2.name)

