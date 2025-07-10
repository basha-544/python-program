#Create Cat and Dog classes. Both should have a make_sound() method that prints different sounds.
class Animal:
    def sounds(self):
        print()
class Dog(Animal):
    def sounds(self):
        print("meoww.......")
class Cat(Animal):
    def sounds(self):
        print("boww.......")
cat=Cat()
cat.sounds()
dog = Dog()
dog.sounds()