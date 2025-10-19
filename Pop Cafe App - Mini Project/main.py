from menu import main_menu, product_menu, order_menu, courier_menu
from products_db_app import add_product, update_product, delete_product, view_products
from orders_db_app import add_order, update_order_status, delete_order, view_orders, view_order_statuses, view_orders_by_status, view_orders_by_courier
from couriers_db_app import add_courier, update_courier, delete_courier, view_couriers

# to make sure correct number of digits is entered when entering a phone number as well as to make sure only numbers are being entered. And to make sure it starts with a 0 


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

        

print("Welcome To Pop Cafe!!")

# This runs the entrie app. 
# it shows the main menu and guides the user to the sub menues based on what they input. 
while True:
    main_menu() # prints the full menu 
    choice = input("Select an option: ")

    if choice == '1':
        while True:
            product_menu() # prints the product sub-menu 
            user_choice = input("Select an option: ") # from the products sub-menu 
            if user_choice == '1': 
                view_products() # prints all products in the sql database 
              

            elif user_choice == '2': # allows user to add a new product 
                name = input("Enter new product name: ")
                price = float(input("Enter product price: "))
                category = input("Enter the product category (e.g is it a food or drink product): ") 
                add_product(name, price, category)

            elif user_choice == '3': # allows user to update an existing product using product_id
                product_id = int(input("Enter product ID you wish to update: "))
                name = input("Enter the new name: ")
                price = float(input("Enter the products new price: "))
                category = input( "Enter the products new category (e.g. food or drink): ")
                update_product(product_id, name, price, category)

            elif user_choice == '4': # allows user to delete a product using product_id
                product_id = int(input("Enter the product ID you wish to delete: "))
                delete_product(product_id) 
                

            elif user_choice == '0':
                break

            else:
                print("Invalid option, try again!")
    
    elif choice == '2':
        while True:
            order_menu() # prints orders sub-menu 
            order_choice = input("Select an option: ") #from orders-sub-menu 
            if order_choice == '1':
                print("\n Current Orders: ") # prints all current orders 
                view_orders()

            elif order_choice == '2': # add new order 
               customer_name = input("Enter your name: ")
               customer_address = input("Enter your address: ")
               customer_phone = get_valid_phone_num()
               view_couriers()  
               courier_id = int(input("Select the courier you wish to use by entering the courier ID: "))
               order_status_id = 1 # always defaulted to preparing
               view_products()
               items = (input("Select your items through product IDs (seprate each with a comma): "))
               add_order(customer_name, customer_address, customer_phone, courier_id, order_status_id, items)

            elif order_choice == '3': # updates order status
                view_orders()
                order_id = int(input("Enter order ID you wish to update: "))
                view_order_statuses()
                new_status_id = int(input("Enter the new status ID: "))
                update_order_status(order_id, new_status_id)
                
            elif order_choice == '4': # views orders through their status IDs 
                try:
                    view_order_statuses() #shows availble status 
                    status_id = int(input("Enter the status ID to filter orders by: "))
                    view_orders_by_status(status_id) 
                except ValueError:
                    print("Invalid input, please try again with a valid status ID!")
            
            elif order_choice == '5': # view orders by courier 
                try:
                    view_couriers()
                    courier_id = int(input("Enter the courier ID to filter orders by: "))
                    view_orders_by_courier(courier_id)
                except ValueError:
                    print("Invalid input, please enter a valid courier ID!")

            elif order_choice == '6': # delete an order 
                view_orders()
                order_id = int(input("Enter the order ID you wish to delete: "))
                delete_order(order_id)

            elif order_choice == '0':
                print("returning to main menu")
                break
            else:
                print("Invalid option, try again!")

    elif choice == '3':
        while True:
            courier_menu() # displays couriers sub-menu 
            courier_choice = input ("Select an option: ")
            if courier_choice == '1':
                view_couriers()

            elif courier_choice == '2': # allows user to add courier
                name = input("Enter new courier name: ")
                phone = get_valid_phone_num()
                add_courier(name, phone)

            elif courier_choice == '3': # allows user to update courier
                courier_id = int(input("Enter courier ID you wish to update; "))
                name = input("Enter new courier name: ")
                phone = get_valid_phone_num()
                update_courier(courier_id, name, phone)
                

            elif courier_choice == '4': # allows user to delete courier 
                courier_id = int(input("Enter courier ID you wish to delete: "))
                delete_courier(courier_id)
            
            elif courier_choice == '0':
                print("Returing to main menu")
                break
            else:
                print("Invalid option, try again!")

    elif choice == '0': # existing the app 
        print("Saving data and exiting, Thank you for visting, Goodbye!!")
        break


    else:
        print("Invalid option, try again!")

    

