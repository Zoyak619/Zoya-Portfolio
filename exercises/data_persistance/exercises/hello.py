
try:
  file_handle = open("Hello.txt", 'r')

  text_lines = file_handle.readlines()

  for line in text_lines:
    trimmed_line = line.strip()
    print(f'My pet is called "{trimmed_line}"')

except FileNotFoundError as whoops:
  print(f'Could not find the file: {whoops}')


except Exception as whoops:
  print(f'unexpected eroor: {whoops}')

 

 