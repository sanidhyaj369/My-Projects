# Create a base class called Shape a method area() that return 0. Then create two subclasses, Rectangle and circle. Override the area() method in both subclasses to calculate the area of a rectangle and circle resp. Write a progress to demonstrate method overriding by crearting objects of each subclass and calling the area()method on them.

# class Shape():
#     def area(self):
#         return 0
    
# class Rectangle(Shape):
#     def area(self, length, breadth):
#         return length*breadth

# class Circle(Shape):
#     def area(self, r):
#         return 3.14*r*r

# r = Rectangle()
# c = Circle()
# print(r.area(5, 7))
# print(c.area(6))

#------------------------------------------------------------------------------------------------------

# Create a base class called BankAccount with methods deposit() and withdraw(). Then, create two subclasses SavingAccount and CheckingAccount. Override the withdraw() method in both subclasses to add specific rules for withdrawal (e.g, checking account may allow overdraft with a penalty, while saving account has a minimum balance requirement). Create instances of both subclasses and demonstrate method overriding by performing deposits and withdrawals on these accountas.

class BankAccount():
    min_balance = 100
    penalty = 10
    saving_balance = 500
    checking_balance = 300

    def deposit(self):
        return 0

    def withdraw(self):
        return 0

class SavingAccount(BankAccount):
    def withdraw(self, amount):
        if(amount > self.min_balance):
            print("Succefully withdrawed ",amount, " Your available balance is ",(self.saving_balance-amount))
        else:
            print("Insuficient balance, because min balance should be 100")

    def deposit(self, amount):
        self.saving_balance = self.saving_balance + amount 
        print("Succesfully deposited. Your current balance is ", self.saving_balance)
    
class CheckingAccount(BankAccount):
    def withdraw(self, amount):
        if(self.checking_balance <= self.min_balance):
            self.checking_balance - amount
            print("Succefully withdrawed ",amount, " but penalty ",self.penalty)
        else:
            self.checking_balance = self.checking_balance - amount
            print("Succefully withdrawed ",amount, " Your current balance is ",self.checking_balance)
        
    def deposit(self, amount):
        self.checking_balance = self.checking_balance + amount
        print("Succesfully deposited. Your current balance is ", self.checking_balance)
    
sbi = SavingAccount()
ubi = CheckingAccount()

# sbi.deposit(500)
# sbi.withdraw(200)

ubi.deposit(300)
ubi.withdraw(200)
ubi.withdraw(200)
ubi.withdraw(100)
ubi.withdraw(50)

###------------------------------------------------------------------------------------------------------

class BankAccount:
    penalty = 10
    def deposit(self, amount):
        return 0
    
    def withdraw(self, amount):
        return 0
    
class SavingAccount(BankAccount):
    def withdraw(self, amount):
        if(amount > self.min_balance):
            print("Succefully withdrawed ",amount, " Your available balance is ",(self.saving_balance-amount))
        else:
            print("Insuficient balance, because min balance should be 100")

class CheckingAccount(BankAccount):
    def withdraw(self, amount):
        if(self.checking_balance <= self.min_balance):
            self.checking_balance - amount
            print("Succefully withdrawed ",amount, " but penalty ",self.penalty)
        else:
            self.checking_balance = self.checking_balance - amount
            print("Succefully withdrawed ",amount, " Your current balance is ",self.checking_balance)

#----------------------------------------------------------------------------------------------------------

# Create a class 'Student' with three data members which are name, age and address. The constructor of the class assigns default values as 'unknown', age is '0' and address as 'not available'. It has two members with the same name 'setInfo'. First method has two parameters for name and age and assign the same whereas the second method takes three parameters which are assigned to name, age and address resp. Print the name, age and address of 10 students.

class Student:
    def __init__(self):
        self.name = 'unknown'
        self.age = 0
        self.address = 'not available'

    def setInfo(self, name, age):
        self.name = name
        self.age = age

    def setInfo(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

s = Student()
s.setInfo('Atul', 25,'Bina')
s.setInfo('Aman', 40,'Mumbai')
s.setInfo('Ajit', 60,'Rewa')
s.setInfo('Ajay', 30,'Indore')

#------------------------------------------------------------------------------------------------

# Create a class 'Degree' having a method 'getDegree' that prints "I got a degrr". It has two subclasses namely 'Undergraduate' and 'Postgraduate' each having a method with the same name that prints "I am an Undergraduate" and "I am a Postgraduate" resp. Call the method by creating an object of each of the three classes.

class Degree:
    def getDegree(self):
        print("I got a degree.")

class Undergraduate(Degree):
    def getDegree(self):
        print("I am an Undergraduate.")

class Postgraduate(Degree):
    def getDegree(self):
        super().getDegree()
        print("I am a Postgraduate.")      

under = Undergraduate()
post = Postgraduate()
under.getDegree()
post.getDegree()

#---------------------------------------------------------------------------------------------------

# A boy has his money deposited $1000, $1500 and $2000 in banks-Bank A, Bank B and Bank C resp. We have to print the money deposited by him in a particular bank.
#Create a class Bank with the method 'getBalance' with return 0. Make its three subclasses named 'BankA', 'BankB' and 'BankC' with a method with the same name 'getBalance' which returns the amount deposited in that particular bank. Call the method 'getBalance' by the object of each of the three banks.

class Bank:
    def getBalance(self):
        return 0
    
class BankA(Bank):
    def getBalance(self):
        return 1000
    
class BankB(Bank):
    def getBalance(self):
        return 1500
    
class BankC(Bank):
    def getBalance(self):
        return 2000
    
a = BankA()
b = BankB()
c = BankC()
print(a.getBalance())
print(b.getBalance())
print(c.getBalance())

#--------------------------------------------------------------------------------------------------
class BankAccount:
    def __init__(self, balance_a, balance_b, balance_c):
        self.balance_a = balance_a
        self.balance_b = balance_b
        self.balance_c = balance_c

    def get_balance(self, bank_name):
        if bank_name == 'Bank A':
            return self.balance_a
        elif bank_name == 'Bank B':
            return self.balance_b
        elif bank_name == 'Bank C':
            return self.balance_c
        else:
            return "Invalid bank name"

# Create an instance of BankAccount with initial balances
boy_account = BankAccount(1000, 1500, 2000)

# Print the balance of a specific bank
bank_name = 'Bank B'  # Change this to the desired bank
balance = boy_account.get_balance(bank_name)

if isinstance(balance, int):
    print(f"Money deposited in {bank_name}: ${balance}")
else:
    print(balance)  # Print an error message if the bank name is invalid

    