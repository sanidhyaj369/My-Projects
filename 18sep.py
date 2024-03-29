# Count the occurence of 2
num = [2,5,1,7,2,5,3,8,9,56,2,22,15]
count = 0
for i in num:
    if i==2:
        count+=1
    else:
        continue

print("Occurence of 2 is: ",count)

#----------------------------------------------------------------------------------

# find the largest element in the list
num = [2,5,1,7,2,5,3,8,9,56,2,22,15]
largest_num = None
for i in num:
    if largest_num is None or largest_num<i:
        largest_num = i

print("Largest element is: ",largest_num)

#-----------------------------------------------------------------------------------

# find the smallest element in the list
num = [2,5,1,7,2,5,3,8,9,56,2,22,15]
smallest_num = None
for i in num:
    if smallest_num is None or i<smallest_num:
        smallest_num = i

print("Smallest element is: ",smallest_num)

#--------------------------------------------------------------------------------------

# create a list having all the odd elements in the list
num = [2,5,1,7,2,5,3,8,9,56,2,22,15]
odd_elements = []

for i in num:
    if i%2!=0:
        odd_elements.append(i)

print("Odd elements list: ",odd_elements)
    
#--------------------------------------------------------------------------------------

# create a list with elements which can be multiplied by 3
num = [2,5,1,7,2,5,3,8,9,56,2,22,15]
multiple_3 = []

for i in num:
    if i%3==0:
        multiple_3.append(i)

print("3 Multiple list: ",multiple_3)

#---------------------------------------------------------------------------------------

# create a list with palindrome numbers in the above list
num = [2,5,1,7,2,5,3,8,9,56,2,22,15]
palindrome = []

for i in num:
    temp = i
    result = 0
    while temp>0:
        rem = temp%10
        result = result * 10 + rem
        temp = temp//10

    if i == result:
        palindrome.append(i)

print("Palindrome no. list: ",palindrome)