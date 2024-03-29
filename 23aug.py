def is_prime(num):
    prime = True
    if num==0 or num==1:
        print(num, "is not a prime number")
    elif num>1:
        for i in range(2,num):
            if num%i==0:
                prime = False
        if prime == True:
            print(num, "is a prime number")
        else:
            print(num, "is not a prime number")
is_prime(67)
is_prime(3)
is_prime(50)
is_prime(84)

#-----------------------------------------------------------------

print('\n')
def even_odd(num):
    if num%2==0:
        print(num, "is an even number")
    else:
        print(num, "is an odd number")
even_odd(4)
even_odd(7)

#-----------------------------------------------------------------
print('\n')
def maximum(a, b, c):
    if(a>b and a>c):
        print(a, "is maximum among three")
    elif(b>c and b>a):
        print(b, "is maximum among three")
    else:
        print(c, "is maximum among three")
maximum(3,8,5)
maximum(45,23,89)

#---------------------------------------------------------------------

print('\n')
def fib_series(num):
    n1 = 0
    n2 = 1
    count = 0
    print("Fibonacci Series: ")
    while count<num:
        print(n1, end=' ')
        n3=n1+n2
        n1=n2, n2=n3
        count+=1
fib_series(10)

#------------------------------------------------------------------------

print('\n')
def armstrong(num):
    t1 = num
    sum = 0
    while(t1>0):
        sum += 1
        t1 = t1//10
    t2 = num
    digit = 0
    while t2>0:
        rem = t2%10
        digit = digit + rem**sum
        t2 = t2//10
    if num==digit:
        print(num, "is an Armstrong number")
    else:
        print(num, "is not an Armstrong")
armstrong(153)
armstrong(400)

#--------------------------------------------------------------------------------------------------

# 1. Create a function that takes an integer as input and returns whether number is even or odd.
# 2. Write a function that takes three numbers as a input and returns the maximum of the three.
# 3. Write a function to generate the first n terms of the fibonicci series, where each term is the sum of the two preceeding number.
# 4. Write a function to print amstrong number

import turtle as t
import tkinter as kin

kin.t