# Tuple : 
# Write a Python program to create a tuple.
num = (2,4,8,7,5,3)
print(num , type(num))

# Write a Python program to create a tuple with different data types.
num = (2,4, 6.7, "hello" , 3+6j ,7.8 , 3)
print('Tuple: ',num)

# Write a Python program to create a tuple of numbers and print one item.
num = (2,4,6,7,9,8,4)
print('One item: ',num[4])

# Write a Python program to unpack a tuple into several variables.
num = (2,4,6,7)
n1, n2, n3, n4 = num
print(n1, n2, n3, n4)

# Write a Python program to add an item to a tuple.
num = (2,4,8,7,5,3)
num = list(num)
num.append(10)
print('New tuple: ',tuple(num))

# Write a Python program to convert a tuple to a string.
num = ('hello', '@',1,2,3,4)
my_string = ''
for i in num:
    my_string += str(i)
print('Tuple to string is: ',my_string)


# Write a Python program to get the 4th element from the last element of a tuple.
num = (2,4,8,7,5,3)
num = list(num)
num.pop(-4)
print('New tuple after removing last 4th element: ',tuple(num))

# Write a Python program to create the colon of a tuple.
num = (2,4,8,7,5,3)
new = num[:-3]
print('Colon of a tuple: ',new)


# Write a Python program to find repeated items in a tuple.
num = (2,4,8,3,7,5,3)
new = []
for i in num:
    if i not in new:
        new.append(i)
print("New Tuple: ",tuple(new))


# Write a Python program to check whether an element exists within a tuple.
num = (2,4,8,3,7,5,3)
check = False
for i in num:
    if i==2:
        check = True
        break
print('Element exists in tuple: ',check)
