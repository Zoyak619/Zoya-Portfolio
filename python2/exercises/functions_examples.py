def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ",")
    print("My " + animal_type + "'s name is " + pet_name.title() + ",")


#Example of positional arugments 
#describe_pet('teddy', 'honey')
describe_pet('bengal', 'honey')
describe_pet('snowy', 'cat')

#Example of keyword arguments 
describe_pet(animal_type='bengal', pet_name='honey' )
describe_pet(pet_name='snowy', animal_type='cat')



#example of default value 
# Example of a default value
def describe_pet(pet_name, animal_type='bengal'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='honey')

#more complicated example
def describe_pet(pet_name, animal_type, pet_last_name=' '):
    if pet_last_name:
        pet_info = pet_name + ', ' + pet_last_name + ', ' + animal_type
    else:
        pet_info = pet_name + ', ' + animal_type
    return pet_info

my_pet = describe_pet('honey', 'bengal')
print(my_pet)

my_pet = describe_pet('honey', 'bengal', 'Furter')
print(my_pet)


#another example

def describe_pet(pet_first_name, pet_last_name):
    my_pet = {'first': pet_first_name, 'last': pet_last_name}
    return my_pet

dog = describe_pet('Frankie', 'Furter')
print(dog)

for x, y in dog.items():
    print(y)



# exapmle 
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

new_user = build_profile('Antony', 'Foy', Age=41, Height="6'", Location='Manchester', Subject='Cloud')
print(new_user)

