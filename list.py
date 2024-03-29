# Lists :
# Write a Python program to reverse a list.
num = [1,4,5,7,8,4,5]
rev_num = []
for i in num:
    rev_num = [i] + rev_num
print('Reverse list: ',rev_num)

# Write a Python program to find the largest element in a list.
num = [1,4,5,7,8,4,5]
largest = None

for i in num:
    if largest is None or largest<i:
        largest = i
print('Largest element: ',largest)

# Write a Python program to find the smallest element in a list.
num = [1,4,5,7,8,4,5]
smallest = None

for i in num:
    if smallest is None or i<smallest:
        smallest = i
print('Smallest element: ',smallest)

# Write a Python program to check if a list is empty.
num = [1,2,3,4,5]
if len(num)==0:
    print("List is empty")
else:
    print("List is not empty")

# Write a Python program to remove duplicates from a list.
num = [1,4,5,7,8,4,5]
num1 = []
for i in num:
    if i not in num1:
        num1.append(i)
print('Non duplicate list: ',num1)

# Write a Python program to count the number of occurrences of an element in a list.
num = [1,4,5,7,8,4,5,4]
count = 0
for i in num:
    if i==4:
        count+=1
print("Occurence of an element is: ",count)

# Write a Python program to sort a list in ascending order.
num = [1,4,5,7,8,6,5,4]
for i in range(0,len(num)):
    for j in range(i+1, len(num)):
        if num[i]>=num[j]:
            num[i], num[j] = num[j], num[i]
print("Ascending order: ",num)

# Write a Python program to sort a list in descending order.
num = [1,4,5,7,8,6,5,4]
for i in range(0,len(num)):
    for j in range(i+1, len(num)):
        if num[i]<=num[j]:
            num[i], num[j] = num[j], num[i]
print("Descending order: ",num)

# Write a Python program to split a list into two sublists.
num = [1,4,5,7,8,6,5,4]
even = []
odd = []
for i in num:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("Two sublists are: ",even, odd)

# Write a Python program to merge two lists.
num = [1,4,5,7,8,6,5,4]
num1 = [11,45,23,9]
for i in num1:
    num.append(i)
print("Merged list: ",num)
