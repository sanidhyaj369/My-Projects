# attemps = 0

# while attemps < 3:
#     password = input('Enter your password: ')

#     if password == 'password123':
#         print('You have successfully logged in.')
#         break
#     else:
#         print('Incorrect credentials. Check if you have Caps lock on and try again.')
#         attemps += 1
#         continue

# n = int(input("Enter number: "))
# prime= True

# if n==0 or n==1:
#     print(n, "is not a prime number")
# elif n<-1:
#     for i in range(2,n):
#         if n%i==0:
#             prime = False
#     if prime==True:
#         print(i)
#     else:
#         print(n, "is not a prime number")


# for i in range(-100,0):
#     if i<2:
#         continue
#     is_prime = True
#     for j in range(2, int(i**0.5) + 1):
#         if i%j==0:
#             is_prime = False
#             break
#     else:
#         print(i, end=' ')




# def maximum(a, b, c):
#     if(a>b and a>c):
#         print(a, "is maximum among three")
#     elif(b>c and b>a):
#         print(b, "is maximum among three")
#     else:
#         print(c, "is maximum among three")

# maximum(4,7,2)


def fib_series(num):
    n1 = 0
    n2 = 1
    count = 0
    print("Fibonacci Series: ")
    while count<num:
        print(n1)
        n3=n1+n2
        n1=n2
        n2=n3
        count+=1

fib_series(10)