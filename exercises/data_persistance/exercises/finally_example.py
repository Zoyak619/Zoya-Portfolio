file = None

items = ['teddy', 'snowy', 'pablo']

try:
    file = open('pets.txt', 'w')
    for item in items:
        file.write(item + '\n')

except FileNotFoundError as fnfe:
    print(f'Unable to open file: {fnfe}')

finally:
    print('--finally-block--')
    if file:
        print('--closing-file--')
        file.close()
    else:
        print('--file-already-closed--')