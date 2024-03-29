# 1. Write a Python program to check if a number is even or odd.
num = int(input("Enter Number: "))
if num%2==0:
    print("Even number")
else:
    print("Odd Number")


# 2. Write a Python program to check if a year is leap year or not.
year = int(input("Enter year to check: "))
if( ((year % 4 == 0) and (year % 100 != 0)) or (year % 400==0) ):
    print("Leap Year")
else:
    print("Not leap Year")


# 3. Write a Python program to check if a number is positive, negative or zero.
num = int(input("Enter Number: "))
if num>0:
    print("Positive number")
elif num<0:
    print("Negative number")
else:
    print("Zero")


# 4. Write a Python program to check if a string is palindrome or not.
num = int(input("Enter the number: "))
result = 0
temp = num
while num>0:
    rem = num%10
    result = result*10 + rem
    num = num//10

if temp == result:
    print(temp, "is a palindrome number")
else:
    print(temp, "is not a palindrome number")


# 5. Write a Python program to check if a given number is prime or not.
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")


# 6. Write a Python program to check if a given string contains only digits.
string = input("Enter the string: ")
if string.isdigit():
    print("The string contains only digits!")
else:
    print("The string does not contain only digits.")


# 7. Write a Python program to check if a given string is uppercase or lowercase.
string = input("Enter the string: ")
if string.islower():
    print("The string is in lower case")
else:
    print("The string is in upper case")


# 8. Write a Python program to check if a given string is alphanumeric.
string = input("Enter the string: ")
if string.isalnum():
    print("The string is alphanumeric")
else:
    print("The string is not alphanumeric")


# 9. Write a Python program to check if a given string is a valid email address.
email = input("Enter the string: ")
if '@' in email and '.' in email:
    if 


# 10. Write a Python program to check if a given string is a valid phone number.
ph_num = int(input("Enter phone number: "))
if len(ph_num) == 10:
    print("Phone number is valid")
else:
    print("Phone number is not valid")