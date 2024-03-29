#POLYMORPHISM

# defining class A
class A:
    def run(self, x,y):
        print(x+y, " is running")

    def run(self):
        print("A is again running")

class B:
    def run(self):
        print("B is running")

# object of A and B
a = A()
b = B()

# calling the function
a.run()
b.run()

#------------------------------------------------------------------------------------------

# Overriding

class Bird():
    def sing(self):
        print("Bird is singing")

    def fly(self):
        print("Bird is flying")

class Pigeon(Bird):
    def sing(self):
        print("Pigeon is singing")

    def peck(self):
        print("Pigeon is pecking")

    def fly(self):
        super().fly()
        print("Pigeon is flying")

pigeon = Pigeon()

pigeon.sing()
pigeon.fly()
pigeon.peck()