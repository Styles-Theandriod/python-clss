# lst = list(range(11))
# print(lst)

seet = list(range(1,11,3))


for num in range(20):
    print(num)


person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    if key == 'address':
        for address in person['address']:
            print(address)

for iterator in range(0, 20, 2):
    print('hello ', iterator)
else:
    print('The loop ended')

count = 1
while count <= 10:
    print(count)
    count +=1




def myFunction():
    FirstN = 'Emekos'
    spce = ' '
    LastN = 'Phelix'
    FullN = FirstN + spce + LastN
    print(FullN)
# myFunction()


def generate_full_name ():
    first_name = 'Mnchester'
    last_name = 'Peter Obi'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())

def grettings(name):
    message = name + ', welcome to Python for Everyone!'
    return message
print(grettings('Henry'))


def add_ten(num):
    ten = 20
    print( num + ten )
add_ten(25)

def square_number(x):
    return x * x
print(square_number(2))


def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))

print('\n')
print('\n')
print('\n')

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    print(total)
print(sum_of_numbers(30)) # 55
# print(sum_of_numbers(100))


def generate_name (first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_name('Peter', "Obi"))


# def calculate_age():
#     txt = int(input('Enter Your Birth Year'))
#     age = 2023 - txt
#     return 'You re', age, 'Yers Old';
# print(calculate_age())

def weight_of_object(mass, gravity):
    weight = str(mass * gravity) + 'N'
    return weight
print(weight_of_object(100, 9.81))

print('40 * 40')