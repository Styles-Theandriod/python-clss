## Variables

# Variables store data in a computer memory. Mnemonic variables are recommended to use in many programming languages. A mnemonic variable is a variable name that can be easily remembered and associated. A variable refers to a memory address in which data is stored.
# Number at the beginning, special character, hyphen are not allowed when naming a variable. A variable can have a short name (like x, y, z), but a more descriptive name (firstname, lastname, age, country) is highly recommended.


# Python Variable Name Rules

# - A variable name must start with a letter or the underscore character
# - A variable name cannot start with a number
# - A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and \_ )
# - Variable names are case-sensitive (firstname, Firstname, FirstName and FIRSTNAME) are different variables)

# Let us se valid variable names

# firstname = 'chidi'

# print(firstname, len(firstname))

### Declaring Multiple Variable in a Line
# first_name, last_name, country, age, is_married = 'Styles', 'Yetayeh', 'Nigeri', 250, False

# print(first_name, last_name, country, age, is_married)

# Getting user input using the _input()_ built-in function. Let us assign the data we get from a user into first_name and age variables.

# firstname = input('What is your name: ')
# age = input('How old are you? ')

# print(firstname)
# print(age)


## Data Types

# There are several data types in Python. To identify the data type we use the _type_ built-in function. I would like to ask you to focus on understanding different data types very well. When it comes to programming, it is all about data types. I introduced data types at the very beginning and it comes again, because every topic is related to data types. We will cover data types in more detail in their respective sections.



print(type('OBi children')) #str
print(type(555)) #int
print(type(3.14)) #flot
print(type(1 + 1j)) #complex int
print(type(True)) #Boolen
print(type([1, 2, 3, 4])) #list 
print(type({'name':'Asabeneh','age':250, 'is_married':250})) #dict
print(type((1,2))) #tuple
print(type(zip([1,2],[3,4]))) #set


# - Casting: Converting one data type to another data type. We use _int()_, _float()_, _str()_, _list_, _set_
#   When we do arithmetic operations string numbers should be first converted to int or float otherwise it will return an error. If we concatenate a number with a string, the number should be first converted to a string. We will talk about concatenation in String section.

num_int = 10
num_float = float(num_int)
print(num_float)

gravity = 9.81
print(int(gravity))

print(str(num_int))

first_name = 'Asabeneh'

print(list(first_name))


## Numbers

# Number data types in Python:

# 1. Integers: Integer(negative, zero and positive) numbers
#    Example:
#    ... -3, -2, -1, 0, 1, 2, 3 ...

# 2. Floating Point Numbers(Decimal numbers)
#    Example:
#    ... -3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5 ...

# 3. Complex Numbers
#    Example:
#    1 + j, 2 + 4j, 1 - 1j

# 🌕 You are awesome. You have just completed day 2 challenges and you are two steps ahead on your way to greatness. Now do some exercises for your brain and muscles.

# Operators in Python

# Python language supports several types of operators. In this section, we will focus on few of them.

### Assignment Operators

# Assignment operators are used to assign values to variables. Let us take = as an example. Equal sign in mathematics shows that two values are equal, however in Python it means we are storing a value in a certain variable and we call it assignment or a assigning value to a variable. The table below shows the different types of python assignment operators, taken from [w3school](https://www.w3schools.com/python/python_operators.asp).

### Arithmetic Operators:
# - Addition(+): a + b
# - Subtraction(-): a - b
# - Multiplication(*): a * b
# - Division(/): a / b
# - Modulus(%): a % b
# - Floor division(//): a // b
# - Exponentiation(**): a ** b


print('Addition: ', 1 + 2)    #3
print('Subtrction: ', 1 - 2) 


# Declaring the variable at the top first

c = 3 # a is a variable name and 3 is an integer data type
d = 2 # b is a variable name and 2 is an integer data type
total = c - d
total = c + d

print(total)

radius = 20
area_of_circle = 3.24 * radius ** 2
print(area_of_circle)

# Calculating area of a rectangle
# length =int( input('Enter length '))
# width =int( input('Enter Width '))
# area_of_rectngle = length * width
# print(area_of_rectngle)


# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N') 


# Calculate the density of a liquid
mass = 75 # in Kg
volume = 0.075 # in cubic meter
density = mass / volume # 1000 Kg/m^3

print(density)


### Compare Operators 
# In programming we compare values, we use comparison operators to compare two values. We check if a value is greater or less or equal to other value. The following table shows Python comparison operators which was taken from [w3shool](https://www.w3schools.com/python/python_operators.asp).

print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False

# Comparing something gives either a True or False
print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)


# In addition to the above comparison operator Python uses:

# - _is_: Returns true if both variables are the same object(x is y)
# - _is not_: Returns true if both variables are not the same object(x is not y)
# - _in_: Returns True if the queried list contains a certain item(x in y)
# - _not in_: Returns True if the queried list doesn't have a certain item(x in y)

print('1 is 1', 1 is 1)                   # True - because the data values are the same
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string
print('B in Asabeneh', 'B' in 'Asabeneh') # False - there is no uppercase B
print('coding' in 'coding for all') # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

### Logical Operators

# Unlike other programming languages python uses keywords _and_, _or_ and _not_ for logical operators. Logical operators are used to combine conditional statements:
print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statements is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print('True or False:', True or False)
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False


# Day 4

## Strings
# Text is a string data type. Any data type written as text is a string. Any data under single, double or triple quote are strings. There are different string methods and built-in functions to deal with string data types. To check the length of a string use the len() method.

### Creating a String
letter = 'P'                # A string could be a single character or a bunch of texts
print(letter)               # P
print(len(letter))          # 1
greeting = 'Hello, World!'  # String could be made using a single or double quote,"Hello, World!"

print(greeting)             # Hello, World!
print(len(greeting))        # 13

sentence = "I hope you are enjoying 30 days of Python Challenge"
print(sentence)

# Multiline string is created by using triple single (''') or triple double quotes ("""). See the example below.

multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.
'''
print(multiline_string)

### String Concatenation

# We can connect strings together. Merging or connecting strings is called concatenation. See the example below:

first_name = 'Michel'
last_name = 'Obi'
space = ' '

full_name = first_name + space + last_name
print(full_name) # Michel  Obi
# Checking the length of a string using len() built-in function
print(len(first_name))  # 6
print(len(last_name))   # 3
print(len(first_name) > len(last_name)) # True
print(len(full_name)) # 9


### Escape Sequences in Strings
# In Python and other programming languages \ followed by a character is an escape sequence. Let us see the most common escape characters:

# - \n: new line
# - \t: Tab means(8 spaces)
# - \\\\: Back slash
# - \\': Single quote (')
# - \\": Double quote (")

print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # line break

print('Days\tTopics\tExercises') # adding tab space or 4 spaces 
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
print('This is a backslash  symbol (\\)') # To write a backslash
print('In every programming language it starts with \"Hello, World!\"') # to write a double quote inside a single quote

### String formatting
#### Old Style String Formatting (% Operator)

color = 'red'

data = 'i have a %s skin'%format(color)
print(data)






