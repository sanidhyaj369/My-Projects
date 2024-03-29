n = int(input("Enter the number"))

if n==0 or n==1:
    print("Not a prime number")
else:
    while n>1:
        for i in range(2,n):
            if n%i==0:
                print("Not a prime number")
        else: 
            print("Prime number")