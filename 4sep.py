class A:
    def run(self):
        print('Class A is running')

class B(A):
    def walk(self):
        print('Class B is walking')

class C(A):
    def talk(self):
        print('Class C is talking')

class D(B):
    def eat(self):
        print('Class D is eating')

a = A()
b = B()
c = C()
d = D()

a.run()
b.walk()
c.talk()
d.eat()
d.run()