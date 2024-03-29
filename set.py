# Set :
# Write a Python program to create a set.
num = {2,4,6,8,5,3,6}
print('Set: ',num, type(num))

# Write a Python program to add members to a set.
num = {2,4,6,8,5,3,6}
num.add(10)
print('Adding new element: ',num)

# Write a Python program to remove members from a set.
num = {2,4,6,8,5,3,6}
num.remove(8)
print('After removing one element: ',num)

# Write a Python program to check if a member exists in a set.
num = {2,4,6,8,5,3,6}
check = False
for i in num:
    if i==8:
        check = True
        break
print("Element exists in Set: ",check)

# Write a Python program to clear a set.
num = {2,4,6,8,5,3,6}
num.clear()
print('Empty set: ',num)

# Write a Python program to print the elements of a set.
num = {2,4,6,8,5,3,6}
print("Elements of a set: ")
for i in num:
    print(i)

# Write a Python program to find the length of a set.
num = {2,4,6,8,5,3,6}
length = 0
for i in num:
    length+=1
print('Length of a set: ',length)


# Write a Python program to find the union of two sets.
num = {2,4,6,8,5,3,6}
num1 = {12,5,17,11,4}
for i in num1:
    if i not in num:
        num.add(i)
print('Union of two sets: ',num)

# Write a Python program to find the intersection of two sets.
num = {2,4,6,8,5,3,6}
num1 = {12,5,17,11,4}
set_inter = set()
for i in num:
    if i in num1:
        set_inter.add(i)
print('Intersection of two sets: ',set_inter)

# Write a Python program to find the difference of two sets.
num = {2,4,6,8,5,3}
num1 = {12,5,17,11,4}
set_differ = set()
for i in num:
    if i not in num1:
        set_differ.add(i)
print('Difference of two sets: ',set_differ)