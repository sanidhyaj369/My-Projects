# x = {1,2,3,4,5,6}
# y = {6,7,4,2,8,9}

# x.intersection_update(y)
# print(x)
# print(x.intersection(y))
# print(x)

# Program to reverse a list
num = [1,4,5,7,8,4,5]
rev_num = []
for i in num:
    rev_num = [i] + rev_num
print('Reverse list: ',rev_num)

# Program to find the sum of all the elements in a list.
num = [1,4,5,7,8,4,5]
sum = 0
for i in num:
    sum+=i
print('Sum of all elements: ',sum)

# Program to find the largest and smallest elements in the list.
num = [1,4,5,7,8,4,5]
largest = None
smallest = None
for i in num:
    if largest is None or largest<i:
        largest = i
print('Largest element: ',largest)

for i in num:
    if smallest is None or i<smallest:
        smallest = i
print('Smallest element: ',smallest)

# Program to remove the duplicate from a list.
num = [1,4,5,7,8,4,5]
num1 = []
for i in num:
    if i not in num1:
        num1.append(i)
print('Non duplicate list: ',num1)

# Program to merge two lists into a single list.
num = [1,4,5,7,8,4,5]
num1 = [3,6,4,8,6]
for i in num1:
    num.append(i)
print('Merged list: ',num)