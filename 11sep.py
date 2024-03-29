# Create an abstract class Employee with abstract methods for calculate_salary(). Create two subclasses HourlyEmployee and SalariedEmployee, that inherit from Employee. Implement the calculate_salary() method in each subclasses to calculate the salary based on the hours worked for hourly employees and a fixed salary for salaried employees.

from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod   #annotation
    def calculate_salary():
        pass

class HourlyEmployee(Employee):
    def calculate_salary(self, hour, rate):
        self.hour = hour
        self.rate = rate
        return self.hour * self.rate
        
        
class SalariedEmployee(Employee):
    def calculate_salary(self, annual_salary):
        self.annual_salary = annual_salary
        return self.annual_salary
    
hourly = HourlyEmployee()
fixed = SalariedEmployee()
h = hourly.calculate_salary(5, 500)
s = fixed.calculate_salary(400000)
print("Hourly salary of employee is ",h)
print("Fixed salary of employee is ",s)
        