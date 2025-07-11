# order functions 

import csv

orders_file_path = "Data/orders.csv" #file path for orders so it can read/view from it and save to it 
orders_fieldnames = ["order_num", "customer_name", "customer_address", "customer_phone", "courier", "status", "items_ordered"] # feildnames for sorting orders in csv 

# View all orders from csv 

def view_orders():
    with open(orders_file_path, mode='r', newline= ',') as orders_file: # reads from the orders csv file and loads all orders onto a newline 
        reader = csv.DictReader(orders_file)
        return list(reader)


# save orders to csv 
def save_orders(orders):
    with open(orders_file_path, mode='w', newline= ',') as order_file:
        writer = csv.DictWriter(order_file, fieldnames=orders_fieldnames)
        writer.writeheader()
        writer.writerows(orders)



# to make sure correct number of digits is entered when entering a phone number as well as to make sure only numbers are being entered. And to make sure it starts with a 0 
def get_valid_phone_num():
    while True:
        phone = input("Enter phone number: ")
        if phone.isdigit() and len(phone) == 11 and phone.startswith("0"):
            return phone
        else:
            print("Invalid phone number, must be 11 digits!")

order_status_list = ["preparing", "ready for collection", "out for delivery", "delivered"] # shows available order status app uses 

# to add a new order to the list  

def add_order(orders, couriers, products):

    # get user details 
    name = input ("Enter your name: ")
    address = input ("Enter your address: ")
    phone = get_valid_phone_num()
    
    # load availble couriers 
    print("\nAvailble Couriers:")
    for courier in couriers:
        print(f"{courier[0]}: {courier[1]} ({courier[2]})") # this loads courier_id, name and phone 
    
    while True:
        try: 
            courier_id = int(input("Enter the courier ID you wish to use: ")) # allows user to select courier by their ID 
            if any (str(courier_id) == str(courier[0]) for courier in couriers):
                break # this will break the loop one a vaild ID is found 
            else:
                print("invalid courier ID entered, please try again")
        except ValueError:
            print("Please enter a valid number!")
    
    # loads current products 
    print("\n Products") 
    for product in products:
        print(f"{product[0]}. {product[1]} - £{float(product[2]):.2f} ({product[3]})") #product_id, name, price, category
 
    # to get product id from user imputs     
    items_ordered = input("Enter the product IDs you wish to add to this order (use comma's to seperate each item): ")
    item_id = ",".join(item.strip() for item in items_ordered.split(",") if item.strip().isdigit()) # turnss id inputs into a list as they're stored as a string in csv, removes all spaces and make sures its just a number and is then able to join it back into a string
    
    # generates new order
    new_order_num = len(orders) + 1 
    new_order = {
        "order_num": str(len(orders) + 1),
        "customer_name": name,
        "customer_address": address,
        "customer_phone": phone, 
        "courier": str(courier_id),     
        "status": "preparing",       # default status 
        "items_ordered": item_id     # stored as IDs
    }

    # adds new order to list 
    orders.append(new_order)
    print("New order added successfully!")
   

# update order 
# shows current orders and staus first then allows user to pick one they wish to update and allows them to chose a new status from the staus list 
def update_order_status(orders):
    if not orders: # if no data is available then exist
        print("No orders to update")
        return

    print("\nCurrent Orders:") # displays current orders in the app 
    for index, order in enumerate(orders, start=1):
        print(f"{index}. {order['customer_name']} - Status: {order['status']}")

    try:
        order_index = int(input("Select order number to update status: ")) # asking user to select the order they wish to update through numbers 
        if 1 <= order_index <= len(orders):
            print("\nSelect new status:")  # shows available status options to choose from 
            for index, status in enumerate(order_status_list, start=1):
                print(F"{index}. {status}")
        
            status_index = int(input("Select the status number to update status: ")) # allows users to select new status by number 
            if 1 <= status_index <= len(order_status_list):
                orders[order_index -1]['status'] = order_status_list [status_index -1] # updates secleted status
                print("Status updated!")
                
                # save after updating order 
                save_orders(orders)
            else:
                print("invalid status number selection")
        else:
            print("Invalid order number.")
    except ValueError:
        print("Please enter a vaild number!")
 


# delete order
# allows user to delete an order useing customer name via index 
def delete_order(orders):
    if not orders: # if no data is availble then exist 
        print("No orders to delete!")
        return

    print("\nOrders:") # shows current orders with customer names 
    for index, order in enumerate(orders, start=1):
        print(f"{index}. {order['customer_name']}")
    
    try:
        idx = int(input("Select order number to delete: ")) # asks user which order to delete by number 
        if 1 <= idx <= len(orders):
            deleted = orders.pop(idx - 1) #removes order from the list 
            print(f"Deleted order for {deleted['customer_name']}")
           
            # save after deleting an order 
            save_orders(orders)
        else:
            print("Invalid order number.")
    except ValueError:
        print("please enter a vaild number!")

    