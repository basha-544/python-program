class calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        print(self.a + self.b)
    def sub(self):
        print(self.a - self.b)
    def mul(self):
        print(self.a * self.b)
    def div(self):
        print(self.a / self.b)
a = calculator(1, 2)
a.add()
a.sub()
a.mul()
a.div()
