# product fnctions 
# This allow users to add products to both the drinks and food lists. as it is split into categories it promots user to make a secletion into which category they would lieke to add to first 
#inputs are used to hep fuction the app and also make is user friendly and easy to understand the steps. 


drink_products = [
    {"index": 1,"name": "cappuccino","price": 3.00},
    {"index": 2,"name": "Americano","price": 2.00},
    {"index": 3,"name":"latte","price": 2.50},
    {"index": 4,"name": "mocha","price": 3.00} 
]

food_products = [
    {"index": 5,"name": "cheese melt", "price": 2.35},
    {"index": 6,"name": "tuna and cheese melt","price": 3.75},
    {"index": 7,"name": "chicken club","price": 5.95}, 
    {"index": 8,"name": "croissant","price": 1.75},
    {"index": 9,"name": "choc chip cookie","price": 2.00},
    {"index": 10,"name": "banana bread","price": 2.35}
]



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
# Allows users to update the name off existing products in both categories. 
# uses index to display products and chose via index so it is easier to use and quick 
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

# Allow user to delete a product from the list using index selection. But first lists the products out 
# uses pop() to remive the selected item
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