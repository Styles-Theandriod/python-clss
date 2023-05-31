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