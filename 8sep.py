#ABSTRACTION

from abc import ABC, abstractmethod

class Car(ABC):    #abstract class
    @abstractmethod
    def frame():      # abstract function
        pass
    
    @abstractmethod
    def engine():
        pass 

    @abstractmethod
    def brakes():
        pass
    
    @abstractmethod
    def controls():
        pass

    def sunroof(self):
        return "Rectangle"
    
class Honda(Car):
    def frame(self):
        return "Sedan"
    
    def engine(self):
        return "2.4 turbo"

    def brakes(self):
        return "Hydraulics"
    
    def controls():
        return "XYZ"
    
class Tata(Car):
    def frame():
        return "XUV"
    
    def engine():
        return "1.3 turbo"

    def brakes():
        return "Manual"
    
    def controls():
        return "ABC"
    
    @abstractmethod
    def power():
        pass

honda = Honda()
tata = Tata()

print(honda.brakes())
print(tata.engine())
