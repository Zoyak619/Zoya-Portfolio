#file = open('people.txt', 'w')
#file.write('Susan')
#file.close()

text_context = None


with open('pets.txt', 'r') as file_handle:
    text_context = file_handle.read()
    print(f'text = {text_context}')

print('all done')
print(text_context)

 
