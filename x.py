# age = int(input("Enter age: "))
# gen = input("Enter Gender: ")
# m_status = input("Enter Marital status: ")

# if gen == 'f':
#     print("She will work only in urban areas")
# elif gen == 'm' and (age>20 and age<=40):
#     print("He work in anywhere")
# elif gen == 'm' and (age>40 and age<=60):
#     print("He works in urban areas only")
# else:
#     print("ERROR")

# Question
quant = int(input("Enter quantity purchased: "))
cost = quant*100

if cost>1000:
    t_cost = cost * 10/100
    print("Total cost is ",t_cost)
else:
    print("Total cost is ",cost)


#Question
salary = int(input("Enetr the salary: "))
year = int(input("Enetr the year of service: "))

if year>=5:
    net_bonus = salary * 5/100
    print("Net bonus amount of employee is ",net_bonus)
else:
    print("Service year of employee is not more than 5years")