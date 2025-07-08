from menu import main_menu, product_menu, order_menu, courier_menu
from products import add_products, update_products, delete_product
from orders import add_order, update_order_status, delete_order
from couriers import add_courier, update_courier, delete_courier
from data_handler import load_data, save_data

drink_products, food_products, couriers, orders = load_data()


print("Welcome To Pop Cafe!!")

# This runs the entrie app. 
# it shows the main menu and guides the user to the sub menues based on what they input. 
while True:
    main_menu()
    choice = input("Select an option: ")

    if choice == '1':
        while True:
            product_menu() # entering the product menu 
            user_choice = input("Select an option: ")
            if user_choice == '1': #no indiactes the selected section 
                print("\n===Drink Products===")
                for product in drink_products: # to list the items 
                    print(f"{product['index']}, {product['name']} - £{float(product['price']):.2f}")  # :,2f ensures prices always show two decimal places.

            elif user_choice == '2':
                print("\n===Food Products===")
                for product in food_products:
                    print(f"{product['index']}, {product['name']}, - £{float(product['price']):.2f}") #  ensures there is two decimal space in prices. 

            elif user_choice == '3':
                add_products(drink_products, food_products)

            elif user_choice == '4':
                update_products(drink_products, food_products)

            elif user_choice == '5':
                delete_product(drink_products, food_products)

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
                    print("-" * 30)

            elif order_choice == '2':
                add_order(orders, couriers, drink_products, food_products)
        
            elif order_choice == '3':
                update_order_status(orders)

            elif order_choice == '4':
                delete_order(orders)

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
                add_courier(couriers)

            elif courier_choice == '3':
                update_courier(couriers)

            elif courier_choice == '4':
                delete_courier(couriers)
            
            elif courier_choice == '0':
                print("Returing to main menu")
                break
            else:
                print("Invalid option, try again!")

    elif choice == '0': # existing the app 
        print("Saving data and exsting, Thank you for visting, Goodbye!!")



else:
    print("Invalid option, try again!")


