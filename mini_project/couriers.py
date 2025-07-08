#courier functions 
# add courier 
# asks the user for courier name and adds it to the list 

from data_handler import load_data, save_data

def get_vaild_phone_num():
    while True:
        phone = input("Enter phone number: ")
        if phone.isdigit() and len(phone) == 11:
            return phone
        else:
            print("Invalid phone number, must be 11 digits!")

def add_courier(couriers):
    name = input("Enter the name off the courier you wish to add: ")
    phone = get_vaild_phone_num()

    new_couriers = {
        "index": len(couriers) + 1,
        "name": name,
        "phone": phone
    }
    couriers.append(new_couriers)
    print(f"{name} has successfully been added")

#update courier
# displays couriers via index, then asks user to pick one and asks them to enter a new name. relaces the current courier at that index. 
def update_courier(couriers): 
    if not couriers:
        print("No cpuriers to update!")
        return
    
    print("\nCurrent Couriers")
    for index, courier in enumerate(couriers, start=1):
        print(f"{index}. {courier['name']}, {courier['phone']}") # print current courier list 
        
    try: 
        index = int(input("Enter the number of courier you wish to update: "))
        if 1 <= index <= len(couriers):
            new_name = input(f"Enter the new courier name for '{couriers[index -1]['name']}': ")
            new_phone = input(f"Enter new phone for '{couriers[index -1]['phone']}': ")
            couriers[index -1]["name"] = new_name
            couriers[index -1]["phone"] = new_phone
            print(f"Courier updated sucessfully!")
        else:
            print("Invalid option, try again!")
    except ValueError:
        print("Invalid number, please try again!!")

# delete courier
# List all couriers and asks the user to chose one. deletes it using pop()
def delete_courier(couriers):
    if not couriers:
        print("No couriers to delete!")
        return
    
    print("\nCurrent Couriers")
    for index, courier in enumerate(couriers, start=1):
        print(f"{index}. {courier['name']}, {courier['phone']} ")
    
    try:
        index= int(input("Enter the number of the courier you wish to delete: "))
        if 1 <= index <= len(couriers):
            removed_courier = couriers.pop(index - 1)
            print(f"Deleted '{removed_courier}' successfully!")

        else:
            print("Invalid courier option selcted!")
            
    except ValueError:
        print("Invalid selection, please enter a valid number!")
    