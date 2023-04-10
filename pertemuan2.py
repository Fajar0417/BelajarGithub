#contoh 1
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#contoh 2
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist[1:3]= ["blackcurrant", "watermelon"]
print(thislist)

#contoh 3
thislist= ["apple", "banana",]
thislist.append("orange") #ctrl + space untuk memunculkan 
print(thislist)

#PYTHON REMOVE
thislist = ['apple', 'banana']

thislist.remove("apple")
thislist.pop(0)
print(thislist) #hasilnya kosong

#contoh
thislist = ["apple", "banana", "cherry"]
print(len(thislist)) #menghitung jumlah thislist

#contoh
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist] #hasilnya menderet kebawah

#contoh
thislist = ['apple', 'banana', 'mango']
thislist.pop(1)
assert(thislist) == ['apple', 'mango']

assert(thislist.append('kiwi')) == ['apple', 'mango', 'kiwi']

new_list = ['apple', 'apple', 'apple', 'apple', 
            'mango', 'kiwi', 'apple', 'apple',
            'apple', 'apple'] #use loop, membership 'in' , and 

assert(new_list[4:6]) == ['mango', 'kiwi']
new_list = ['apple', 'apple', 'apple', 'apple', 'mango', 'kiwi', 'apple', 'apple', 'mango', 'kiwi', 'apple', 'apple']
assert([x for x in new_list if x == 'apple']) == ['mango', 'kiwi', 'mango', 'mango', 'kiwi']

list1 = ['mango']
list2 = ['apple']


list1 + list2 #equal to list = list1 + list2
print(list1)

list =[1,4,5,6,2,4]
list.sort()
print(list1)

list1 = [1,4,5,6,2,4]
list1.reverse()
print(list1)

list = ['apple', 'banana','mango']
list1.reverse()
print(list1)

list1 = [1,4,5,6,2,4]

assert ([x for x in list1 if x ==4]) == [1, 5, 6, 2]

assert ([x for x in list1 if x ==4]) == [4, 4]

list1= [1, 4, 5, 6, 2, 4]
list2= list1.copy()
list2.pop()

print(list1, list2)

list1 = [1, 4, 5, 7]
list3 = list1.copy()
list2.pop

assert(list3) == [1, 4, 5]
assert(list1) == list1

#UNPACKING USING ASTERISK

fruits = ("apple", "banana", "cherry", "strawberry", "rasberry")

(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)