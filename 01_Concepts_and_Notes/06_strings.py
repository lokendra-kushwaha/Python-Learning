#==================================================================================================
#                              Day - 6 : Strings in Python
#==================================================================================================

# <--- Strings in Python --->
# In python specifically, strings are a sequence of Unicode Characters.

# Creating Strings -->

s1 = 'Hello'
s2 = "Hello World"
s3 = """Hello World""" # for multiines strings

# s4 = 'It's raining outside' # Throws an error
s4 = "It's raining outside"
s5 = """Hello"""
s6 = '''hello'''

s = str('hello')

print(s1, s2, s3, s4)

# Accessing Substrings from a String -->
# 1. Indexing Method
# Positive Indexing
s = 'Hello World'
print(s[::-1])

# Negative Indexing
s = 'Hello World'
print(s[-4])

# 2. Slicing Method
# Slicing
s = 'Hello world'
print(s[1:5])

s = 'Hello world'
print(s[1:])

s = 'Hello world'
print(s[0:6:3])

s = 'Hello world'
print(s[6:0:-2])

print(s[::-1])

s = 'Hello World'
print(s[-5:])

s = 'Hello World'
print(s[-1:-6:-1])

# Editing and Deleting in Strings -->
# Python strings are immutale (can not be change)
s = 'Hello World'
s[0] == 'h' # Not work
del s
print(s)

# del s[-1:-5:2] # Throws an error
# print(s)

# Operation on strings -->

# 1. Arithmethic Operation (+, * only)
print('delhi' + 'mumbai') # work as concatination
print('delhi' * 5) # work as repitition of string
print('='*30)

# 2. Relational Operators (all rel operators works)
print('delhi' == 'mumbai')
print('delhi' != 'mumbai')
print('mumbai' > 'pune') # compares lexiographically (basis of ASCII number values)
print('Pune' > 'pune') # P's ASCII value is smaller than 'p'.

# 3. Logical Operator
print('' and 'world') # In python empty string is False else True
print('' or 'world')
print('hello' or 'world')
print('hello' and 'world')
print(not '')
print(not 'hello')

# 4. Loops on strings
for i in 'hello':
    print(i)

for i in 'delhi':
    print('pune')

# 5. Membership Operators
print('D' in 'Delhi')
print('D' not in 'Delhi')
print('D' not in 'delhi')

# Common Functions # Works on all datatypes (tuple, list, dict)
# 1. len
# 2. max
# 3. min
# 4. sorted

print(len('hello'))
print(max('hello'))
print(min('hello'))
print(sorted('hello world')) # Output is a list
print(sorted('hello world', reverse=True)) # Output is a list

# Capitalize/Title/Upper/Lower/Swapcase
s = 'hello world'

print(s.capitalize())
print(s) # strings are immutable original string doesn't change
print(s.title())
print(s.upper())
print(s.lower())
print(s.swapcase())

# Count/Find/Index
print('My name is lokendra'.count('a')) # frequency count 
print('My name is lokendra'.find('z')) # throw -1 not error
print('My name is lokendra'.find('is'))
print('My name is lokendra'.index('z')) # throws an error


# endswith/startswith
s = 'Lokendra Kushwaha'
print(s.endswith('ha'))

s = 'Lokendra Kushwaha'
print(s.startswith('Lo'))

# format
name = 'lokendra'
gender = 'male'

print('Hii my name is {} and I am a {}.'.format(name, gender))
print('Hii my name is {} and I am a {}.'.format(name, gender))
print('Hii my name is {1} and I am a {0}.'.format(gender, name))

# isalpha/isalnum/isdigit/isidentifier

print('lokendra1234'.isalnum()) # Output is True
print('lokendra1234%'.isalnum()) # Output is False special characters not alpha nor num.
print('lokendra'.isalpha())
print('1234'.isdigit())
print('lokendra_'.isidentifier())

# split/join
s = 'Hii my name is lokendra' # Splites all values and stores in a list by give split parameter.
print(s.split())

print(' '.join(['Hii', 'my', 'name', 'is', 'lokendra'])) # Joins many string as a sentence.

# replace

s = 'Hii my name is lokendra'
print(s.replace('lokendra', 'vivek'))

# Strip
s = 'lokendra          '
print(s.strip()) # removes trailing spaces from string

# How to write program in python strings
# 1. finding len withoth len() function
string = 'lokendra'
count = 0
for char in string:
    count = count + 1

print(count)

# 2. extracting username from email
# 1st Method -->
string = 'lokendrakushwaha@gmail.com'
for i in string:
    if i == '@':
        break
    print(i, end='')

print("\n" ,string.split('@')[0])

# 2nd Method -->
position = string.index('@')
print(string[0:position])

# 3. count of a char in string

s = 'Hii i am harry'
c = 'h'
print(s.count(c))

s = input("Enter your email: ")
name = input("What would you like to search: ")

counter = 0
for i in s:
    if i == name:
        counter += 1

print('frequency', counter)

# 4. remove a particular char from a string

string = input("Enter the string: ")
term = input("What would you like to remove: ")

result = ''
for i in string:
    if i != term:
        result += i

print(result)

# 5. given string is palindrom or not

string = input("Enter a string: ")

if string == string[::-1]:
    print("This a palindrome string.")

else:
    print("Not a palindrom string.")

string = input("Enter a string: ")

flag = True
for i in range(0, len(string)//2):
    if string[i] != string[len(string) - i - 1]:
        print("Not a palindrome")
        flag = False
        break

if flag:
    print("Palindrom")

# 6. split a string without split method
string = input("Enter a string: ")

l = []
temp = ''
for i in string:
    if i != ' ':
        temp = temp + i

    else:
      l.append(temp)
      temp = ''

l.append(temp)  
print(l)

# 7. change a string into title without using title function

string = input("Enter a string: ")

new_string = []
for i in string.split():
    new_string.append(i[0].upper() + i[1:].lower())

print(' '.join(new_string))

# 8. convert into str number to a given interger

number = int(input("Enter the number: "))

digits = '0123456789'
result = ''
while number != 0:
    result = digits[number % 10] + result

    number = number//10

print(result)