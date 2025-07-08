# order functions 

# Collects user input, name, address, phone etc which then builds it into a dict to represent the order and adds it the orders list.
# items_ordered is a list which is created by splitting user input. 

from data_handler import load_data, save_data

def get_vaild_phone_num():
    while True:
        phone = input("Enter phone number: ")
        if phone.isdigit() and len(phone) == 11:
            return phone
        else:
            print("Invalid phone number, must be 11 digits!")

order_status_list = ["preparing", "ready for collection", "out for delivery", "delivered"]
# to add order
def add_order(orders, couriers, drink_products, food_products):

    # get customer details 
    name = input ("Enter your name: ")
    address = input ("Enter your address: ")
    phone = get_vaild_phone_num()
    
    # load availble couroers 
    print("\nAvailble Couriers:")
    for index, courier in enumerate(couriers, start=1):
        print(f"{index}: {courier['name']}, {courier['phone']}")
    
    while True:
        try: 
            courier_index = int(input("Entre the courier number you wish to use: "))
            if 1 <= courier_index <= len(couriers):
                break
            else:
                print("invalid number entered, please try again")
        except ValueError:
            print("Please enter a valid number!")

    # loads current products 
    print("\nDrink Products")
    for product in drink_products:
        print(f"{product['index']}. {product['name']} - £{float(product['price']):.2f}")
    print("\nFood Products")
    for product in food_products:
        print(f"{product['index']}, {product['name']} - £{float(product['price']):.2f}")

    items = input("Enter the name of items you wish to add to this order (use comma's to seperate each item): ").split(",")
    items = [item.strip() for item in items]
    
    # generates order num 
    new_order_num = len(orders) + 1 
    new_order = {
        "order_num": new_order_num,
        "customer_name": name,
        "customer_address": address,
        "customer_phone": phone, 
        "courier": courier_index,    # shows just the index number 
        "status": "preparing",       # default status 
        "items_ordered": items       # stored as a list and then coverts to string when saving 
    }

    # adds new order to list 
    orders.append(new_order)
    print("New order added successfully!")
   
# update order 
# shows current orders and staus first then allows user to pick one they wish to update and allows them to chose a new status from the staus list 
def update_order_status(orders):
    if not orders:
        print("No orders to update")
        return

    print("\nCurrent Orders:")
    for index, order in enumerate(orders, start=1):
        print(f"{index}. {order['customer_name']} - Status: {order['status']}")

    try:
        order_index = int(input("Select order number to update status: "))
        if 1 <= order_index <= len(orders):
            print("Select new status:")
            for index, status in enumerate(order_status_list, start=1):
                print(F"{index}. {status}")
        
            status_index = int(input("Select the status number to update status: "))
            if 1 <= status_index <= len(order_status_list):
                orders[order_index -1]['status'] = order_status_list [status_index -1]
                print("Status updated!")
            else:
                print("invalid status number selection")
        else:
            print("Invalid order number.")
    except ValueError:
        print("Please enter a vaild number!")
    
        

# delete order
# allows user to delete an order useing customer name via index 
def delete_order(orders):
    if not orders:
        print("No orders to delete!")
        return

    print("\nOrders:")
    for index, order in enumerate(orders, start=1):
        print(f"{index}. {order['customer_name']}")
    
    try:
        idx = int(input("Select order number to delete: "))
        if 1 <= idx <= len(orders):
            deleted = orders.pop(idx - 1)
            print(f"Deleted order for {deleted['customer_name']}")
        else:
            print("Invalid order number.")
    except ValueError:
        print("please enter a vaild number!")
