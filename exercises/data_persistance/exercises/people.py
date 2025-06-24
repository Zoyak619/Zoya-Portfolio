
file = None
#1 

people = ["John", "Sally", "Mark", "Lisa", "Joe", "Barry", "Jane"]


file = open('people.txt', 'w')
for person in people:
    file.write(person + "\n")
    file.close()

#2

people = ["John", "Sally", "Mark", "Lisa", "Joe", "Barry", "Jane"]

try:
    file = open('people.txt', 'w')
    for person in people:
        file.write(person + "\n")
        file.close()

except FileNotFoundError as fnfe:
    print(f'unable to open file', {fnfe})

#3

people = ["John", "Sally", "Mark", "Lisa", "Joe", "Barry", "Jane"]

try:
    file = open('people.txt', 'w')
    for person in people:
        file.write(person + "\n")
        file.close()

except FileNotFoundError as fnfe:
    print(f'unable to open file', {fnfe})

