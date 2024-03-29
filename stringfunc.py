# String:
# Write a function that takes a string as input and returns a new string with all of the vowels removed.
my_string = input("Enter string: ")
new = ''
for i in my_string:
    if i not in 'aeiouAEIOU':
        new+=i
print('new string with all of the vowels removed: ',new)
        
# Write a function that takes a string as input and returns a new string with all of the letters reversed.
rev_new = ''
for i in my_string:
    rev_new = i + rev_new
print('Reversed string: ',rev_new)

# Write a function that takes a string as input and returns a new string with all of the words capitalized.
# cap_new = my_string.split(' ')
new1 = ''
for i in my_string:
    new1 += i.upper()
print('All words capitalized: ',new1)
    

# Write a function that takes a string as input and returns a new string with all of the punctuation removed.
punct = ''
for i in my_string:
    if i not in ',:![]()':
        punct+=i
print('All punctuation removed: ',punct)

# Write a function that takes a string as input and returns a new string with all of the whitespace removed.
white = ''
for i in my_string:
    if i not in ' ':
        white += i
print('Whitespace removed: ',white)

# Write a function that takes a string as input and returns a new string with all of the duplicate characters removed.
dupli = ''
for i in my_string:
    if i not in dupli:
        dupli += i
print('Duplicate char removed: ',dupli)

# Write a function that takes two strings as input and returns a new string with the two strings concatenated together.
string1 = input('1st string: ')
string2 = input('2nd string: ')
for i in string2:
    string1 += i
print('Two strings concatenated: ',my_string)

# Write a function that takes a string as input and returns a new string with all of the characters sorted alphabetically.
alpha = ''
for i in range(26):
    for char in my_string:
        if ord(char.lower()) - 97 == i:
                alpha += char
print('All char sorted: ',alpha)


# Write a function that takes a string as input and returns a new string with all of the numbers removed.
numb = ''
for i in my_string:
    if i not in '1234567890':
        numb += i
print('All numbers removed: ',numb)

# Write a function that takes a string as input and returns a new string with all of the letters converted to lowercase.
lower1 = ''
for i in my_string:
    lower1 += i.lower()
print('All words in lowercase: ',lower1)

