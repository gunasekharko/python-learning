import copy


d={'a':1,'b':2,'c':3}

print(d)

person={
    'first Name': "Eric",
    'Last Name' : "Idle",
    "year Born" : 2023
}

#looping into dictionaries

person={
    'firstname':'guna',
    'lastname':'sekhar',
    'age':32,
}

for keys,values in person.items():
    print(f'{keys}--->{values}')
    

#working with dictionaries

person={
    'firstname':'guna',
    'lastname' :'sekhar',
    'age':32,
    'address':{
        'city':'New York',
        'zipcode':'10001'
    }
}

person_copy=copy.deepcopy(person)

person_copy['address']['city']='Los Angeles'

print('original dicitonay:',  person)

print('Deep coped dictionary:', person_copy)

shallow_person_copy=person.copy()

shallow_person_copy['address']['city']='Tirupati'

# Original dictionary
person = {
    'firstname': 'guna',
    'lastname': 'sekhar',
    'age': 32,
    'address': {
        'city': 'New York',
        'zipcode': '10001'
    }
}

# Perform a shallow copy
shallow_person_copy = person.copy()

# Modify the shallow copy
shallow_person_copy['firstname'] = 'KO gunasekhar'
shallow_person_copy['address']['city'] = 'Los Angeles'

# Print both dictionaries to see the difference
print("Original dictionary:", person)
print("Shallow copied dictionary:", shallow_person_copy)


transactions = [
    {'item': 'widget', 'trans_type': 'sale', 'quantity': 10},
    {'item': 'widget', 'trans_type': 'sale', 'quantity': 5},
    {'item': 'widget', 'trans_type': 'refund', 'quantity': 2},
    {'item': 'license', 'trans_type': 'sale', 'quantity': 1},
    {'item': 'license', 'trans_type': 'sale', 'quantity': 1},
    {'item': 'license', 'trans_type': 'refund', 'quantity': 1},
]

total_sold={}

for transaction in transactions:
    item=transaction['item']
    issale= True if transaction['trans_type']=='sale' else False
    quantity=transaction['quantity']
    
    if issale:
        if item in total_sold:
            total_sold[item]+=quantity
        else:
            total_sold[item]=quantity

print(total_sold)

net_sales={}

for transaction in transactions:
    item=transaction['item']
    issale= True if transaction['trans_type']=='sale' else False
    quantity=transaction['quantity']
    
    if not issale:
        quantity=-quantity
    net_sales[item]=net_sales.get(item,0) + quantity
            
print(f'net_sales:{net_sales}')

net_sales={'item': 'widget', 'trans_type': 'sale', 'quantity': 10}

print(net_sales.get('item'))


#======================================================================