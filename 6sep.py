class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def display(self):
        print(self.a)

    def output(self):
        print(self.b)

objA = A(5,7)
objA.display()
objA.output()