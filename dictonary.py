# Dictionary : 
# Write a Python program to create a dictionary.
my_dict = {'roll': 101, 'name':'anuj', 'place':'indore'}
print('Dictonary: ',my_dict)

# Write a Python program to add a key-value pair to a dictionary.
my_dict = {'roll': 101, 'name':'anuj', 'place':'indore'}
my_dict['result'] = 'pass'
print('New entry add: ',my_dict)

# Write a Python program to remove a key-value pair from a dictionary.
my_dict = {'roll': 101, 'name':'anuj', 'place':'indore'}
my_dict.pop('place')
print('After removing: ',my_dict)

# Write a Python program to check if a key exists in a dictionary.
my_dict = {'roll': 101, 'name':'anuj', 'place':'indore'}
check = False
for key in my_dict:
    if key=='place':
        check = True
print('Key exists in dictonary: ',check)

# Write a Python program to iterate over the key-value pairs in a dictionary.
my_dict = {'roll': 101, 'name':'anuj', 'place':'indore'}
print("Iterate over key-value pair: ")
for key,value in my_dict.items():
    print(f"{key}:{value}")

# Write a Python program to get the keys of a dictionary.
my_dict = {'roll': 101, 'name':'anuj', 'place':'indore'}
keys = []
for key in my_dict:
    keys.append(key)
print("Keys of dictonary are: ",keys)

# Write a Python program to get the values of a dictionary.
my_dict = {'roll': 101, 'name':'anuj', 'place':'indore'}
values = []
for key in my_dict:
    values.append(my_dict[key])
print("Values of dictonary are: ",values)

# Write a Python program to sort a dictionary by key.
my_dict = {'roll': 101, 'name':'anuj', 'place':'indore'}
for key in my_dict.keys():
    for 

# Write a Python program to sort a dictionary by value.


# Write a Python program to copy a dictionary.
my_dict = {'roll': 101, 'name':'anuj', 'place':'indore'}
dict2 = {}
for key, value in my_dict.items():
    dict2[key] = value
print("Copied dictonary is: ",dict2)