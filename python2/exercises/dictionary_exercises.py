 # Car dictionary

#car = {

 #   'brand': 'Ford',

  #  'model': 'Mustang',

   # 'year' : 1964,

    #'isNew': False


# 1) Add colour

#car['colour'] = 'red'

#print(f"Colour: {car['colour']}")

# 2) Update model

#car['model'] = 'F-150'

#print(f"Updated model: {car['model']}")

# 3) Delete model

#del car['model']

#print("Dictionary after deleting 'model':", car)

# 4) Loop using items() — use str() safely

#for key, value in car.items():

 #   print(f"key: {key}, value: {str(value)}")
 

 # Exercise 6: 

 #1. Use a dictionary to store information about a person you know. #
 # Store their first name, last name, age, and the city in which they live. #
 # You should have keys such as first_name, last_name, age, and city. #
 # Print each piece of information stored in your dictionary.



def build_profile(first, last, **user_info):
    user_info[ 'first_name'] = first
    user_info[ 'last_name'] = last
    return user_info

new_user = build_profile('Aneesa', 'Iqbal', Age=28, Location='Manchester')
print(new_user)

#2. Use a dictionary to store people’s favorite numbers. 
# Think of five names, and use them as keys in your dictionary.
# Think of a favorite number for each person, and store each as a value in your dictionary.
# Print each person’s name and their favorite number. 
# For even more fun, poll a few friends and get some actual data for your program.


