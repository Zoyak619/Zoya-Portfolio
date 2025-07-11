from menu import main_menu, product_menu, order_menu, courier_menu
from products_db_app import add_product, update_product, delete_product, view_products
from orders import add_order, update_order_status, delete_order
from couriers import add_courier, update_courier, delete_courier
from data_handler import load_data, save_data

couriers, orders = load_data()


print("Welcome To Pop Cafe!!")

# This runs the entrie app. 
# it shows the main menu and guides the user to the sub menues based on what they input. 
while True:
    main_menu() # displays the full menu 
    choice = input("Select an option: ")

    if choice == '1':
        while True:
            product_menu() # dispalys the product sub-menu 
            user_choice = input("Select an option: ") # from the products sub-menu 
            if user_choice == '1': 
                view_products() #dispalys all products in the sql database 
              

            elif user_choice == '2': # allows user to add a new product 
                name = input("Enter new product name: ")
                price = float(input("Enter product price: "))
                category = input("Enter the product category (e.g is it a food or drink product): ") 
                add_product(name, price, category)

            elif user_choice == '3': # allows user to update an existing product using product_id
                product_id = int(input("Enter product ID you wish to update: "))
                name = input("Enter the new name: ")
                price = float(input("Enter the products new price: "))
                category = input( "enter the products new category (e.g. food or drink): ")
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
            order_menu() # orders section 
            order_choice = input("Select an option: ")
            if order_choice == '1':
                print("\n Current Orders: ")
                for index, order in enumerate(orders, start=1):
                    print(f"{index}.") 
                    print (f"Name: {order['customer_name']}") 
                    print(f"Address: {order['customer_address']}")
                    print(f"phone: {order['customer_phone']}")
                    print(f"Items: {order['items_ordered']}")
                    print(f"courier:{order['courier']}")
                    print(f"status: {order['status']}")
                    print("-" * 30) # to seperate each order clearly from another when printing 

            elif order_choice == '2':
                add_order(orders, couriers, drink_products, food_products)
        
            elif order_choice == '3':
                update_order_status(orders, drink_products, food_products, couriers)

            elif order_choice == '4':
                delete_order(orders, drink_products, food_products, couriers)

            elif order_choice == '0':
                print("returning to main menu")
                break
            else:
                print("Invalid option, try again!")

    elif choice == '3':
        while True:
            courier_menu() # courier section 
            courier_choice = input ("Select an option: ")
            if courier_choice == '1':
                print("\n===couriers List===")
                for courier in couriers:
                    print(f"{courier['index']}, {courier['name']} - {courier['phone']}")
            
            elif courier_choice == '2':
                add_courier(couriers, drink_products, food_products, orders)

            elif courier_choice == '3':
                update_courier(couriers, drink_products, food_products, orders)

            elif courier_choice == '4':
                delete_courier(couriers, drink_products, food_products, orders)
            
            elif courier_choice == '0':
                print("Returing to main menu")
                break
            else:
                print("Invalid option, try again!")

    elif choice == '0': # existing the app 
        print("Saving data and exsting, Thank you for visting, Goodbye!!")
        save_data(drink_products, food_products, couriers, orders)
        break


else:
    print("Invalid option, try again!")
    

