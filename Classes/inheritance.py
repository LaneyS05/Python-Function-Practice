class Pet:
    def walk(self):
        print("walk")


class Dog(Pet):
    def bark(self):


class Cat(Pet):
    pass


dog1 = Dog()
dog1.walk()