# dictionary examples

dora = {
    'name': 'Dora',
    'age': 14,
    'is_hungry': True
}

print(dora)
pet_age = dora['age']
print(f'Doras age is {pet_age}')


# using keys

#dora_weight = dora['weight']
#print(f'Doras weight is {dora_weight}')

#add a key + value

dora['weight'] = 5
dora_weight= dora['weight']
print(f'Doras weight is {dora_weight}')

#update

dora['age'] = 15
pet_age = dora['age']
print(f'Doras age is {pet_age}')

#delete a key-value

del dora['is_hungry']
print(dora)

is_hungry = dora.get("is_hungry")
print(f'cat is hungry? {is_hungry}')


# dictionary examples

dora = {
    'name': 'Dora',
    'age': 14,
    'is_hungry': True
}

print(dora) # everything

print(dora.items()) # list of tuples

print(dora.keys()) # list of the keys

print(dora.values()) # list of the values


if'weight' in dora:
    print(f'pet weight {dora["weight"]} kgs')
else:
    #get user input
    print('.......')


# number of keys
print(len(dora))

dora.clear() # remove all contnts 
print(dora) #everything 



