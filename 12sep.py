# ENCASULATION

class Employee:
    def __init__(self, name, salary):
        self._name = name  # protected attribute
        self.__salary = salary  # private attribute

    def get_salary(self):  # public method to access private attribute
        return self.__salary

    def get_name(self):  # public method to access protected attribute
        return self._name

emp = Employee("John", 5000)
print(emp.get_name())  # Accessing protected attribute via public method
print(emp.get_salary())  # Accessing private attribute via public method

#-----------------------------------------------------------------------------------------
# class A:
#     num = 4

# class B(A):
#     __num1 = 7
#     def run(self):
#         print(B().num)

# class C(B):
#     num2 = 9

# a = A()
# b = B()
# c = C()
# print(b.num)

#------------------------------------------------------------------------------------------

# RECURSION

# swap two numbers using third variable and without third variable.

x = 6
y = 8
# z = x
# x = y
# y = z
x = x+y   # x=14 , y=8 
y = x-y   # x=14 , y=6
x = x-y   # x=8  , y=6

print(x)
print(y)

#-----------------------------------------------------------------------------------------------
# print 1 to 100 without using loop

def recur(n):
    if n<=100:
        print(n, end=' ')
        n=n+1
        recur(n)

recur(1)