# start = int(input("Enter the number: "))
# end = int(input("Enter the last number: "))
# avg = 0
# while start<end:
#     avg = ()/2
#     start+=1
# print(avg)

# Ques. Take 10 int from keyboard using loop and print their average value.
value = int(input("Enter the num: "))
sum = 0
num=1
while num<=value:
    sum = sum + num
    num = num + 1
print(sum)
avg = sum/value
print(avg) 

# Ques. Print multiplication table of 24, 50 and 26 using while loop.
num = int(input("Enter the number: "))
i=1
while i<=10:
    print(num, '*', i, '=', num*i)
    i+=1

# Ques. Program that asks the user to enter a password, keep prompting until they enter the correct password 'python123'.
attemps = 0
while attemps <= 3:
    password = input('Enter your password: ')

    if password == 'python123':
        print('You have successfully logged in.')
        break
    else:
        print('Incorrect credentials. Check if you have Caps lock on and try again.')
        attemps += 1
        continue
