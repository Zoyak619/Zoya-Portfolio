# pop cafe - welcome message when opening the app 

print("Welcome To Pop Cafe!! Please select from the following option '1' to print products menu or '0' to exit")

#shows main menu option 
def main_menu():
    print("\n=== Main Menu ===")
    print("1. Products Menu")
    print("0. Exit")

#shows sub menu option after selecting 1 
def product_menu():
    print("\n=== Products Menu ===")
    print("1. Drink Products")
    print("2. Food Products")
    print("3. Add Products")
    print("4. Update Products")
    print("5. Delete Products")
    print("0. Back to Main Menu") #returns back to main menu 

# list of items sold in sub catogries 
Drink_products = ["cappuccino", "Americano", "latte", "mocha"]
Food_products = ["cheese melt", "tuna and cheese melt", "chicken club", "croissant", "choc chip cookie", "banana bread"]

# to add a product 
def Add_products():
    category = input("Select (1) for Drinks or (2) for Food: ") #as there is a sub catogry list to allow user to add products in both catogries
    if category == '1':
        name = input("Enter the name of the product you wish to add: ")
        Drink_products.append(name)
        print(f"Added {name} to Drinks")

    elif category == '2': 
        name = input("Enter the name of the product you wish to add: ")
        Food_products.append(name)
        print(f"Added {name} to Foods")

    else:
        print("Invalid option, no products added")

# update existing list by index 
def Update_products():
    category = input("Select (1) for Drinks or (2) for Food: ") # to aloowe users to make changes to both caogries
    if category == '1':
        products = Drink_products

    elif category == '2':
        products = Food_products

    else:
        print("Invalid category.")
        return
# shows current products by index starting with 1 
    print("\nCurrent Products:") 
    for i, product in enumerate(products, start=1):
        print(f"{i}. {product}")

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
def Delete_product():
    category = input("Select (1) for Drinks or (2) for Food: ")
    if category == '1':
        products = Drink_products

    elif category == '2':
        products = Food_products

    else:
        print("Invalid category.")
        return
# shows current product in list by index starting from 1 
    print("\nCurrent Products:")
    for i, product in enumerate(products, start=1):
        print(f"{i}. {product}")

    try:
        delete_product = int(input("Enter the number of the product you wish to delete: "))
        if 1 <= delete_product <= len(products):
            removed_item = products.pop(delete_product - 1)
            print(f"Deleted '{removed_item}' successfully!")

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
                print("Drinks:", Drink_products)

            elif user_choice == '2':
                print("Foods:", Food_products)

            elif user_choice == '3':
                Add_products()

            elif user_choice == '4':
                Update_products()

            elif user_choice == '5':
                Delete_product()

            elif user_choice == '0':
                break

            else:
                print("Invalid option, try again!")

    elif choice == '0': # exisitng app 
        print("Thank you for visiting Pop Cafe!")
        break

    else:
        print("Invalid option, try again!")
 