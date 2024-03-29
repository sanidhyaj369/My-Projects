# from itertools import *

# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# output = list(product(A,B))

# for i in output:
#     print(i,end=' ')

class A:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def add(self):
        print(self.n1 + self.n2)

class B:
    def add(self,n1,n2):
        print(n1+n2)

a = A(4,8)
a.add()
classB = B()
classB.add(4,7)

# Inheritance - Single, Multilevel, Herarchichal

class Animal:
    def eat(self):
        print(" is eating")

    def sleep(self):
        print(" is sleeping")

class Dog(Animal):
    def bark(self):
        print(" is barking")

    def wiggle(self):
        print(" is wiggling")

class Cat(Animal):
    def meow(self):
        print(" is meowing")

    def scratch(self):
        print(" is scratching")

class Human(Animal):
    def work(self):
        print(" is working")

    def study(self):
        print(" is studying")

class Student(Human):
    def play(self):
        print(" is playing")

animal = Animal()
pug = Dog()
persiancat = Cat()
rohit = Human()
ajay = Student()

pug.bark()
pug.eat()
persiancat.meow()
rohit.work()
ajay.play()