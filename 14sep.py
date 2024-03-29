class XYZ:
    #variable
    __num = 1
    # getter function
    def getNum(self):
        return self.__num
    
    # setter function
    def setNum(self,num):
        self.__num = num

class JKL(XYZ):
    #variable
    x = 7

j = JKL()
print(j.x)
print(j.getNum())
j.setNum(34)
print(j.getNum())