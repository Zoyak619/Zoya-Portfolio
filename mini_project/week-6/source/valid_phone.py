# phone function 

def get_valid_phone_num(max_attempts=3):
    attempts = 0  # sets the attempt counter 
    while attempts < max_attempts: # prompots the user to enter a valid number untill max attempts are reached 
        phone = input("Enter phone number: ") 
        if phone is None: # if nothing is entered counts as a failed attempt and continues 
            attempts += 1
            continue
        phone = phone.strip().replace(" ", "") # removes any spaces, from each end and within the string 
        if phone.isdigit() and len(phone) == 11 and phone.startswith("0"): # this checks to make sure number is all digits, 11 numbers long and starts with 0
            return phone
        else:
            print("Invalid phone number, must be 11 digits!")
            attempts += 1 # counts this as a failed attempt 
        return False

          
