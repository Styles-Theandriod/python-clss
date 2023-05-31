
# Variables in Python

first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname':'Asabeneh', 
    'lastname':'Yetayeh', 
    'country':'Finland',
    'city':'Helsinki'
    }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

plyer = 'michel obi'

print(' length', len(plyer))

PHONE,PROFILE = int('09090582388'),'TRUE'
print(PHONE)

# nme = input("wht is your nme? ")
# print(nme)
print(zip([2,3], [3,4]))


first = str(20.66)
print(first)

first_name = 'brother benrd'
print(type(data (first_name)))

print((2 + 2) * 2)

rd = 20
circle = 3.22 * rd ** 2
totl = circle
print(totl)

length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

print(20 > 5)
print(20 >= 20)
print(20 < 200)
print(30 <= 50)
print(40 == "40")

print(3 != 2) #Not EQU

print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)


print(30 is 30)
print(30 is not 3)

print('e' in 'eMM')

print(4 is 2 ** 2)

# num = int( input('enter bse '))
# print(num)
# height = int( input('enter height'))
# print(height)
# area = 0.5

# result = area*num*height
# print("your result is:", result)



item3 =  'ornge'
item4 = 'fishs'



print(len(item3) == len(item4))
print('logicl',8 < 2 or 4 < 3)

multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)

print('\n')
print('Were  \n  is mick')
print('Days\tTopics\tExercises')
print('200dys\t Python\t Strings')
print('This is a backslash  symbol (\\)')
print(" lnguge progrm \"Hello world\" ")

song = 'Loction'
musicin = 'kiss dniel'

result = 'i\'m %s i sng %s ' %(musicin, song)
print(result) 

radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = '''
The area of circle with a radius %d is %.3f'''%(radius,area)

print(formated_string)
myFirstName = 'emmnuel'
myLastName = 'Bizmrrow'

resultss = 'I\'m {} {} from Nigeri'.format(myFirstName,myLastName)
print(resultss)


a = 4
b = 3

c = print('''{}/ {} {:.2f}'''.format(a,b, a / b))
print(c)

slope = 20
constant = 3.44
r = constant * 20 ** 2

formating ='The Value of {} is {:.2f}'.format(slope, r)
print(formating)


screenHeight = 20
screenWidth = 40

print(f'{screenHeight} + {screenWidth} = {screenHeight + screenWidth:.2f}')

Club = 'Chelsea'
last_index = len(Club) - 2
last_letter = Club[last_index]
print(last_letter)

first_three = Club[::-1]
pto = Club[0:6:1]
print(pto)

print(Club.upper())
Clubss = 'Thirty\tDayys\tOf\tPython'
print(Clubss.count('y',7,11))
print(Clubss.endswith('ons'))
print(Clubss.expandtabs(20))

data  = ['item', 'item2', 'item3','item4','item5']
first_item, second_item, third_item, *rest = data 
print(rest)

first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(rest)

fruits = ['banana', 'orange', 'mango', 'lemon', 'pine']
orange_and_lemon = fruits[::2]
orange_and_lemon = fruits[::-1]
fruits[0] = 'cherry'
fruits.append('Ogechi')
fruits.insert(1,'Ogbonn')
# fruits.clear()
# fruits.pop()
del fruits[2:4]

fruits_copy = fruits.copy()

positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers


list1 = ['item1', 'item2']
list2 = ['item3', 'item4', 'item5']

list1.extend(list2)
print(list1)

list1.count(list1)
print(list1)

print(list1.index('item2'))

list1.reverse()
# list1.sort(reverse=True)

print(sorted(list1))
b = 2

if b > 2:
    print('B is greter thn 2')
elif(b > 4):
    print('its is greter thn 4')
else:
    print("2 is grter thn B")

# code if condition else code 
henry = 'celebrte Grce1'
henryVlue = 'Hi i\'m Henry'

print(henryVlue) if henry == 'celebrte Grce' else print('Wrong sttement!!')



a = 2
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')


# count = 0
# while count < 5:
#     print(count)
#     # count = count + 1
#     count += 1

# count = 0
# while count < 5:
#     print(count)
#     count = count + 1
# else:
#     print(count)

count = 0
while count < 5:
    print(count)
    count += 1
    if count == 3:
        continue

numbers = [40,50,60,70]

for x in numbers:
    print(x)


language = "Python"

for x in range(len(language)):
    print(language[x])


numberss = (0, 1, 2, 3, 4, 5)

for x in numberss:
    print(x)

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

# for P in person:
#     print(P)


for key, value, in person.items():
    print(key, value)

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 2:
        break
        # pass


numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')

