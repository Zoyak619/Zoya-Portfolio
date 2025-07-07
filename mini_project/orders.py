# order functions 

# Collects user input, name, address, phone etc which then builds it into a dict to represent the order and adds it the orders list.
# items_ordered is a list which is created by splitting user input. 

# order list - each order contains customer deatils, items ordered and status to track the prgress of each order 

orders = [
    {
         "customer_name": "Sam Smith",
         "customer_address": "Langdale Drive, Huddersfeild",
         "customer_phone": "07355456285",
         "status":  "preparing",
         "items_ordered": ["cheese melt", "latte"],
  },
    {
        "customer_name": "Fozia Iqbal",
        "customer_address": "Whalley New Road, Blackburn",
        "customer_phone": "07123456788",
        "status":  "ready for collection",
        "items_ordered": ["cappuccino", "chicken club", "croissant"],
     },
    {
        "customer_name": "Ryan Maddocks",
        "customer_address": "Ancoats, Manchester",
        "customer_phone": "07899567432",
        "status":  "delivered",
        "items_ordered": ["latte", "americano", "cheese melt", "banana bread"]

  },
]


order_status_list = ["preparing", "ready for collection", "out for delivery", "delivered"]
# to add order
def add_order():
    name = input ("Enter your name: ")
    address = input ("Enter your address: ")
    phone = input("Enter your phone number: ")
    
    print("select your chosen courier by number: ")
    for index, courier in enumerate(couriers, start=1):
        print(f"{index}: {courier}")
    courier_index = int(input("courier number: "))

    items = input("Enter the items you wish to add to this order (use comma's to seperate each item): ").split(",")
    items = [item.strip() for item in items]
    new_order = {
        "customer_name": name,
        "customer_address": address,
        "customer_phone": phone, 
        "courier": couriers[courier_index -1],
        "status": "preparing",
        "items_ordered": items
    }

    orders.append(new_order)
    print("New order added!")
   
# update order 
# shows current orders and staus first then allows user to pick one they wish to update and allows them to chose a new status from the staus list 
def update_order_status():
    if not orders:
        print("No orders to update")
        return
    

    for index, order in enumerate(orders, start=1):
        print(f"{index}. {order['customer_name']} - Status: {order['status']}")

    print("orders:")
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
        

# delete order
# allows user to delete an order useing customer name via index 
def delete_order():
    for index, order in enumerate(orders, start=1):
        print(f"{index}. {order['customer_name']}")
    idx = int(input("Select order number to delete: "))
    if 1 <= idx <= len(orders):
        deleted = orders.pop(idx - 1)
        print(f"Deleted order for {deleted['customer_name']}")
    else:
        print("Invalid order number.")
