# function
# constructor
# self
# global and local

# constructor = __int__  (default)
# self - attribute, keyword
# user defined functions
# creating objects
# calling functions using objects

#defining class
class Bike:
    
    b = 8 #global variable
    
    #defining constructor
    def __init__(self, name, cc, hp, color):
        self.name = name   #instance variable
        self.cc = cc
        self.hp = hp
        self.color = color
    
    # defining functions
    def start(self):
        a = 9  #local variable
        print(self.name," has been started")

    def ride(self):
        print("The bike is riding")

    def stop(self):
        print("The bike has been stoped")

    def details(self):
        print("Name: ",self.name)
        print("CC: ",self.cc)
        print("Horse power: ",self.hp)
        print("Color: ",self.color)

# defining objects
splendor = Bike("Splendor", 100, 12, "white")
karishma = Bike("Karishma", 250, 25, "red")
kawasaki = Bike("Ninja", 350, 33.5, "Neon Green")

#calling functions
splendor.start()
karishma.start()
kawasaki.details()
print(splendor.name)