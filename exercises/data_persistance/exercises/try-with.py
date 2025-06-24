pets = ['teddy', 'snowy', 'pablo']

try:
    with open('saved_pets.txt', 'w') as file_handler:
        for pet in pets:
            file_handler.write(pet)

except Exception as whoops: 
    print(f'problem saving file: {whoops}')
    