#PYTHON DATES
import datetime
x = datetime.datetime.now()
print(x)

#PYTHON OUTPUT
import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

#Creating Date Objects
import datetime
x = datetime.datetime(2020, 5, 17)
print(x)

#PYTHON OUTPUT
import datetime
x = datetime.datetime.now()
print(x.strftime("%m/%d/%y"))

#ARRAY
Arr_1 = [5, 78, 2, 0]
assert(min(Arr_1)) == 0
assert(max(Arr_1)) == 78

#function 5 pangkat 5
assert (pow(5, 5)) == 3125

#The Math Module
#contoh1
import math

x = math.sqrt(64)

print(x)

#contoh2
import math

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1

#contoh3
import math

x = math.pi

print(x)

#Exception Handling
#Many Exception
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

#Else
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

#finally
#contoh3
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

#contoh2
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

  #Python JSON
  #Parse JSON - Convert from JSON to Python

import json
#some Json:
x = '{"name": "John", "age":30, "city": "New York"}'
#parse x:
y= json.loads(x)
#the result os a python dctionary:
print(y["age"])

#Convert from Python to JSON (Kebalikan)
import json
# a Python object (dict):
import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)


#json
import json
x ={
  "Name": "Fajar",
  "Age": 16
}

print('DICT: ',x)
print(type(x))

y= json.dumps(x)

print('JSON:', y)
print(type(y))
#Send data
#dict >> convert to json(dump) >> Done
#get Data
#json >> convert to dict(loads) >> Done
#baru bisa manipulasi Data

#FILE HANDLING
#f = open("demofile.txt", "rt")

#Python File Open

#Python File Write
f= open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file afther file the appending:
f= open('./fajar.txt', "r")
print(f.read())


#Python Delete File
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

  #contoh latihan
#   f= open('./fajar.txt')
#   json_string= f.read()
#   print(json_string)
#   # 2. loads
#   json_dict= json.loads(json_string)
#   print(json_dict)
#   print(type(json_dict))
#   print(json-dict['name'])

#   users.append= [
#     {
#     'email': "fajarferdiansyah3009@gamail.com",
#     'password': '1234'
#   }
#   {
#     'email': "fajarferdiansyah3009user@mail.com",
#     'password': "1234"
#   }
# ]
# #1. dumps
# json_string = json.dumps(users)
# #2. file & write
# f= open('./fajar.txt', 'w')
# f.write(json_string)

# f.close()

# def

import json
def write_too_file(file, data):
     json_string= json.dumps(data)

     f= open(file, 'w')
     f.write(json_string)
     f.close()

def read_file(file, mode= 'r'):
  
     try:
         f= open(file, mode=mode)
         json_string= f.read()
         json_dict= json.loads(json_string)
         f.close()
         return json_dict
     except:
       return False

#cara menambahkan function/ module menyimpan users dan transaction ke fle

