# num = int(input('Enter number: '))

# if num%2==0:
#     print("Even")
# else:
#     print("Odd")

# if num>=80 and num<=100:
#     print("Grade A")
# elif num>=65 and num<80:
#     print("Grade B")
# elif num>=45 and num<65:
#     print("Grade C")
# elif num>=33 and num<45:
#     print("Grade D")
# elif num<33 and num>=0:
#     print("Fail")
# else:
#     print("Invalid marks")

#----------------------------------------------------------------

# num = int(input("Enter number: "))
# temp = num
# result = 0
# sum = 0
# t1 = num
# while t1!=0:
#     sum = sum+1
#     t1 = t1//10
# i = sum
# while num>0:
#     rem = num%10
#     result = result + rem**i
#     num = num//10

# if temp==result:
#     print(temp, "is an Armstrong number")
# else:
#     print(temp, "is not an armstrong number")

#-------------------------------------------------------------------------

# n = int(input("Enter number: "))
# prime= True

# if n==0 or n==1:
#     print(n, "is not a prime number")
# elif n>1:
#     for i in range(2,n):
#         if n%i==0:
#             prime = False
#     if prime==True:
#         print(n, "is a prime number")
#     else:
#         print(n, "is not a prime number")

#-------------------------------------------------------------------------------

# for i in range(1,100):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i, end=' ')

#---------------------------------------------------------------------------------

# num = 1
# fact = 1
# while num<=5:
#     fact = fact*num
#     num+=1
# print(fact)
    

n1=0
n2=1
count = 0
while count < 20:
    print(n1, end=" ")
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1