#Create a class Marks with private math marks. Add methods to update and display the marks safely.
class Marks:
    def __init__(self):
        self.__mathmarks = 55
    def update(self,m):
        self.__mathmarks = m
    def display(self):
        print(self.__mathmarks)
m = Marks()
m.display()
m.update(99)
m.display()
