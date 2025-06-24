#def add_numbers(num1, num2):
  #  total = num1 + num2
   # return total

#def pet_hello(name, age, ishungry):
    #print(f"The cat {name} is {age} yrs old and is is it hungry? {ishungry}")

#more code
#more code
#more code
#more code

#result = add_numbers(12, 34)
#print(f"result = {result}")

#pet_hello("diago", 13, True)


#code example 

#def get_name():
 #   user_input = input("Please enter you're name: ")
  #  return user_input
 
 
#user_name1 = get_name()
#print(f"You're name is {user_name1}")
 
 
#user_name2 = get_name()
#print(f"{user_name2}")
 

 # exercise 8

 #1. Write a function called display_message() 
 # that prints one sentence telling everyone what you are learning about 
 # in this module. Call the function, and make sure the message displays 
 # correctly

def display_message():
    print("In this module i we will be learning about python")

display_message()

#2. Write a function called favorite_book() that accepts one parameter, 
# title. The function should print a message, such as, 
# “One of my favorite books is Alice in Wonderland.” Call the function, 
# making sure to include a book title as an argument in the function call.

def favourite_book(book):
    print(f"One of my favorite books is {book.title()}")

favourite_book('A thousand splended sun')

#3 Write a function called make_shirt() that accepts a size and the text 
# of a message that should be printed on the shirt. The function should 
# print a sentence summarizing the size of the shirt and the message printed 
# on it. Call the function once using positional arguments to make a shirt. 
# Call the function a second time using keyword arguments.

def make_shirt(shirt_message, size):
    print("\nI would like a " + size + "," + "the message I would like on the shirt " + shirt_message ",")

make_shirt(shirt_message= 'free palestine', size= 'L' )