#loops 

#1

for number in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
    print(f'cureent number is {number}')

#2

i = 0
while i <= 10:
    print(i)
    i += 1

#3

number_list = [0, 2, 8, 20, 43, 82, 195, 204, 367]
for number in number_list:
    print(number)

#4 

import random 

for number in range(11):
    print(number)
else:
    print("Done!")

#5

list1 = ['apple', 'banana', 'cherry', 'durian', 'ekederberry', 'fig']
list2 = ['avacodo', 'banana', 'coconut', 'date', 'elderberry', 'fig']

for item1 in list1:
    for item2 in list2:
        if item1 == item2:
            print(f'match found: {item1}')

#6

while True: 
    x = random.randint(1, 100)
    if x % 5 == 0:
        print(f'multiple of 5 found: {x}')
        break
    elif x % 3 == 0:
        print(f'multiple of 3 found: {x}')
        continue
    else:
        print(f'number: {x}')
