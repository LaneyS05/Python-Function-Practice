class Pet:
    def walk(self):
        print("walk")


class Dog(Pet):
    def bark(self):
        print("bark")


class Cat(Pet):
    def jump(self):
        print("Jumped on counter")


dog1 = Dog()
cat1 = Cat()
dog1.walk()
dog1.bark()
cat1.jump()