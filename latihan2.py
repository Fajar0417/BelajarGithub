#UNPACKING USING ASTERISK

fruits = ("apple", "banana", "cherry", "strawberry", "rasberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

#contoh <<<

cars = {
    'brand': 'honda',
    'product': 'civic'
}
print(cars['brand'])

print(cars.keys())

for key in cars.keys():
    print(cars[key])

cars = {
    'brand' : 'honda',
    'product': 'civic'
}


assert(list(cars.keys())[1]) == 'product'

print(cars.values())

print(cars.get('year', 'none'))
print('Tidak akan dijalankan')

if 'year' in cars:
    print (cars['year']) #cars.get('year','none')

cars.update(
    {
        'year': 2020,
        'key2' : 2021
    }
)
cars['year'] = 2020
print(cars)

cars['brand'] = 'Toyota'
print(cars)

#ARGUMENT
def my_function(fname): #contoh1
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#KEYWORD ARGUMENT

#Default Parameter Value
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


#Passing a List as an Argument
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

#Contoh latihan
def upper_case_country(country="Norway"):
    print(country.upper())

upper_case_country("Swiss")

def multiply_by_two(a):
    return a * 2

assert(multiply_by_two(3)) == 6


def multiply_by_x(a, x=2):
    "If not passed, then define the default value to 2"
    return a * x

assert(multiply_by_x(3)) ==6
assert(multiply_by_x(3, 1)) ==3

user_input = input('input dikali dengan 2:')
print(multiply_by_two(user_input))
#user input - input('input dikali dengan 2:)
#print(multiply_by_two(user_input))

how_many_input= input('Berapa kali ingin input data?')
i= 0
while True:
    if i == 0:
        break

    user_input = input('input dikali dengan 2: ')
    print(multiply_by_two(int(user_input)))
    i += 1