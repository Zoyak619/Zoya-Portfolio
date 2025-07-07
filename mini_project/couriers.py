#courier functions 
# add courier 
# asks the user for courier name and adds it to the list 

couriers = [
    {"index": 1,"name": "deliveroo","phone": "07123456789"},
    {"index": 2,"name": "uber_eats","phone": "07234567890"},
    {"index": 3,"name": "just_eat","phone": "07345678901"}
]



def add_courier():
    name = input("Enter the name off the courier you wish to add: ")
    couriers.append(name)
    print(f"{name} has successfully been added")

#update courier
# displays couriers via index, then asks user to pick one and asks them to enter a new name. relaces the current courier at that index. 
def update_courier(): 
    for index, courier in enumerate(couriers, start=1):
        print(f"{index}. {courier}") # print current courier list 
        
    try: 
        index = int(input("Enter the number of courier you wish to update: "))
        if 1 <= index <= len(couriers):
            new_name = input(f"You've selcted '{couriers[index -1]}'. Enter the new name")
            couriers[index -1] = new_name
            print(f"Courier updated sucessfully")
        else:
            print("Invalid option, try again!")
    except ValueError:
        print("Invalid selecton, please try again!!")

# delete courier
# List all couriers and asks the user to chose one. deletes it using pop()
def delete_courier():
    for index, courier in enumerate(couriers, start=1):
        print(f"{index}. {courier}")
    
    try:
        index= int(input("Enter the number of the courier you wish to delete: "))
        if 1 <= index <= len(couriers):
            removed_courier = couriers.pop(index - 1)
            print(f"Deleted '{removed_courier}' successfully!")

        else:
            print("This is not a valid option")
            
    except ValueError:
        print("Invalid selection, please enter a number")
    