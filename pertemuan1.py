#PYTHON STRING <<<

#STRINGS
a ="Hello"
print(a)

#STRINGS ARE ARRAY
a ="Hello, World!"
print(a[1])

#LOOPING THROUGH A STRING
# contoh 1 membuat teks menurun
for x in "banana":
    print(x)

# STRING LENGTH menyatakan false
a = "Hello, World"
print (len(a))

# CHECK STRING
txt = "The best things in life are from!"
print("free" in txt)

#UPPER CASE mengubah ke Huruf Kafital
a = "Hello, World"
print (a.upper())

#LOWER CASE mengubah ke huruf Kecil
a ="Hello, World"
print (a.lower())

#REMOVE WHITESPACE return "Hello, Word!"
a ="Hello, World!"
print(a.strip())

#REPLACE STRINGS 
a ="Hello, World!"
print(a.replace("H", "J"))

#SPILIT STRING membuat ['Hello', 'World']
a ="Hello, World!"
print(a.split(','))


#PYTHON SLICING STRINGS
#contoh 1
b ="Hello, World!"
print(b[2:5])

b ="Hello, World!"
print(b[:5])

b ="Hello, World!"
print(b[:2])

b ="Hello, World!"
print(b[-5:-2])


#PYTHON STRING CONCATENATION
#contoh 1 Hasilnya "Hello World"
a ="Hello "
b ="World"
c = a + b
print(c)

#PYTHON FORMAT STRINGS

#contoh 1
age = 16
txt ="My Name is Fajar, and I am {}"
print(txt.format(age))

#contoh 2
quantity = 3 
itemo = 567 
price = 49.95 
myorder ="I want to pay {2} dollars forv{0} pleces of item{1}."
print (myorder.format(quantity, itemo, price))


#PYTHON STRING EXERCISES
#contoh 1
txt= "We are the so-called \"VICKING\" from the moth."