# pop cafe - welcome message when opening the app 

print("Welcome To Pop Cafe!!")

# list of items sold in sub catogries 
drink_products = ["cappuccino", "Americano", "latte", "mocha"]
food_products = ["cheese melt", "tuna and cheese melt", "chicken club", "croissant", "choc chip cookie", "banana bread"]


# order list 

orders = [
    {
         "customer_name": "Sam Smith",
         "customer_address": "Langdale Drive, Huddersfeild",
         "customer_phone": "07355456285",
         "status":  "preparing",
         "item(s)_ordered": ["cheese melt", "latte"],
  },
    {
        "customer_name": "Fozia Iqbal",
        "customer_address": "Whalley New Road, Blackburn",
        "customer_phone": "07123456789",
        "status":  "ready for pick up",
        "item(s)_ordered": ["cappuccino", "chicken club", "croissant"],
     },
    {
        "customer_name": "Ryan Maddocks",
        "customer_address": "Ancoats, Manchester",
        "customer_phone": "07899567432",
        "status":  "delivered",
        "item(s)_ordered": ["latte", "americano", "cheese melt", "banana bread"]

  },
]


# courier list

couriers = ['deliveroo', 'under_eat', 'just_eat']


#shows main menu option 
def main_menu():
    print("\n=== Main Menu ===")
    print("1. Products Menu")
    print("2. Order Menu")
    print("3. Courier Menu")
    print("0. Exit")

#shows sub menu option after selecting Products menu 
def product_menu():
    print("\n=== Products Menu ===")
    print("1. Drink Products")
    print("2. Food Products")
    print("3. Add Products")
    print("4. Update Products")
    print("5. Delete Products")
    print("0. Back to Main Menu") #returns back to main menu 

# sub menu for orders 
def order_menu():
    print("\n=== Orders Menu ===")
    print("1. View Orders")
    print("2. Add Order")
    print("3. Update Order")
    print("4. Delete Order")
    print("0. Back to Main Menu")

# sub menu for couriers 
def courier_menu():
    print("\n=== Couriers Menu ===")
    print("1. View Courier")
    print("2. Add Courier")
    print("3. Update Courier")
    print("4. Delete Courier")
    print("0. Back to Main Menu")

# product fnctions 
# to add a product 
def add_products():
    category = input("Select (1) for Drinks or (2) for Food: ") #as there is a sub catogry list to allow user to add products in both catogries
    if category == '1':
        name = input("Enter the name of the product you wish to add: ")
        drink_products.append(name)
        print(f" {name} has now been added")

    elif category == '2': 
        name = input("Enter the name of the product you wish to add: ")
        food_products.append(name)
        print(f" {name} has now been added")

    else:
        print("Invalid option, no products added")

# update existing list by index 
def update_products():
    category = input("Select (1) for Drinks or (2) for Food: ") # to aloowe users to make changes to both caogries
    if category == '1':
        products = drink_products

    elif category == '2':
        products = food_products

    else:
        print("Invalid category.")
        return
# shows current products by index starting with 1 
    print("\nCurrent Products:") 
    for index, product in enumerate(products, start=1):
        print(f"{index}. {product}")

    try:
        product_update = int(input("Enter the number of the product you wish to update: "))
        if 1 <= product_update <= len(products):
            new_update = input(f"You've selected '{products[product_update - 1]}'. Enter the new name: ")
            products[product_update - 1] = new_update
            print("Product updated successfully!")

        else:
            print("This is not a valid option")

    except ValueError:
        print("Invalid selection, please enter a number")

# to delete a product from the list 
def delete_product():
    category = input("Select (1) for Drinks or (2) for Food: ")
    if category == '1':
        products = drink_products

    elif category == '2':
        products = food_products

    else:
        print("Invalid category.")
        return
# shows current product in list by index starting from 1 
    print("\nCurrent Products:")
    for index, product in enumerate(products, start=1):
        print(f"{index}. {product}")

    try:
        delete_index = int(input("Enter the number of the product you wish to delete: "))
        if 1 <= delete_index <= len(products):
            removed_item = products.pop(delete_index - 1)
            print(f"Deleted '{removed_item}' successfully!")

        else:
            print("This is not a valid option")

    except ValueError:
        print("Invalid selection, please enter a number")

# order functions 

# to add order
def add_order():
    name = input ("Enter your name: ")
    address = input ("Enter your address: ")
    phone = input("Enter your phone number: ")
    status = "preparing"

    items = input("Enter the items ordered (use comma's to seperate each item): ").split(",")
    items = [item.strip() for item in items]
    new_order = {
        "customer_name": name,
        "customer_address": address,
        "customer_phone": phone, 
        "status": status,
        "item(s)_ordered": items
    }

    orders.append(new_order)
    print("New order added!")
   
# update order 
def update_order():
    for index, order in enumerate(orders, start=1):
        print(f"{index}. {order['customer_name']} - Status: {order['status']}")
    idx = int(input("Select order number to update status: "))
    if 1 <= idx <= len(orders):
        new_status = input("Enter new status: ")
        orders[idx - 1]['status'] = new_status
        print("Status updated!")
    else:
        print("Invalid order number.")

# delete order
def delete_order():
    for index, order in enumerate(orders, start=1):
        print(f"{index}. {order['customer_name']}")
    idx = int(input("Select order number to delete: "))
    if 1 <= idx <= len(orders):
        deleted = orders.pop(idx - 1)
        print(f"Deleted order for {deleted['customer_name']}")
    else:
        print("Invalid order number.")

#courier functions 
# add courier 
def add_courier():
    name = input("Enter the name off the courier you wish to add: ")
    couriers.append(name)
    print(f"{name} has successfully been added")

#update courier
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


while True:
    main_menu()
    choice = input("Select an option: ")

    if choice == '1':
        while True:
            product_menu() # entering the product menu 
            user_choice = input("Select an option: ")
            if user_choice == '1': #no indiactes the selected section 
                print("Drinks:", drink_products)

            elif user_choice == '2':
                print("Foods:", food_products)

            elif user_choice == '3':
                add_products()

            elif user_choice == '4':
                update_products()

            elif user_choice == '5':
                delete_product()

            elif user_choice == '0':
                break

            else:
                print("Invalid option, try again!")
    
    elif choice == '2':
        while True:
            order_menu()
            order_choice = input("Select an option: ")
            if order_choice == '1':
                print("\n Current Orders: ")
                for index, order in enumerate(orders, start=1):
                    print(f"{index}.") 
                    print (f"Name: {order['customer_name']}") 
                    print(f"Address: {order['customer_address']}")
                    print(f"phone: {order['customer_phone']}")
                    print(f"Items: {order['item(s)_ordered']}")
                    print(f"status: {order['status']}")

            elif order_choice == '2':
                add_order()
        
            elif order_choice == '3':
                update_order()

            elif order_choice == '4':
                delete_order()

            elif order_choice == '0':
                print("returning to main menu")
                break
            else:
                print("Invalid option, try again!")

    elif choice == '3':
        while True:
            courier_menu()
            courier_choice = input ("Select an option: ")
            if courier_choice == '1':
                print("Couriers List:", couriers)
            
            elif courier_choice == '2':
                add_courier()

            elif courier_choice == '3':
                update_courier()

            elif courier_choice == '4':
                delete_courier()
            
            elif courier_choice == '0':
                print("Returing to main menu")
                break
            else:
                print("Invalid option, try again!")

    elif choice == '0':
        print("Thank you for visting, Goodbye!!")
        break
    else:
        print("Invalid option, try again!")


