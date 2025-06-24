# try and break my program

dora = {
    'type': 'cat',
    'floofy': True
}

try:
    age = dora['age']
    print(f"my cat is {age}")
except:
    print("could not get the age")

print("All done")



try:
    age = dora['age']
    print(f'my cat is {age}')
except Exception as whoops:
    print('Could not get the age:', type(whoops), whoops)



    import traceback

clubs = ['arsenal', 'chelsea', 'liverpool']

try:
    for x in clubs:
        print(x)
    1 / 0
except TypeError as whoops:
    print('Could not get the clubs', whoops)
except ZeroDivisionError as whoops:
    print('Could not get the scores', whoops)
    traceback.print_exc()