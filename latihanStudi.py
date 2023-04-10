data=[
    {
    'name': 'myName',
    'age': 'myAge'
    },
    {
    'name' : 'myName1',
    'age' : 'myAge1'
    },
    {
    'name' : 'myName2',
    'age' : 'myAge2'
    }
]

for x in data:
    if x['name'] == 'myName1' and x['age'] == 'myAge1':
        print(x ['name'], x['age'])
        
