# product fnctions 
# This allow users to add products to both the drinks and food lists. as it is split into categories it promots user to make a secletion into which category they would lieke to add to first 
#inputs are used to hep fuction the app and also make is user friendly and easy to understand the steps. 


from data_handler import load_data, save_data

def add_products(drink_products, food_products):
    category = input("Select (1) for Drinks or (2) for Food: ") #as there is a sub catogry list to allow user to add products in both catogries
    if category == '1':
        name = input("Enter the name of the product you wish to add: ")
        price = input("Enter the price: ")

        new_drink_product = {
            "index": len(drink_products) +1,
            "name": name,
            "price": price
        }
        drink_products.append(new_drink_product)
        print(f" {name} has now been sucessfully added!")

    elif category == '2': 
        name = input("Enter the name of the product you wish to add: ")
        price = input("Enter the price: ")

        new_food_product = {
            "index": len(food_products) + 1,
            "name": name,
            "price": price
        }
        food_products.append(new_food_product)
        print(f" {name} has now been successfully added!")

    else:
        print("Invalid option, no products added")

# update existing list by index 
# Allows users to update the name off existing products in both categories. 
# uses index to display products and chose via index so it is easier to use and quick 
def update_products(drink_products, food_products):
    if not drink_products and not food_products:
        print("No products to update")
        return
    
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
        print(f"{index}. {product["name"]}, - £{float(product["price"]):.2f}")

    try:
        product_update = int(input("Enter the number of the product you wish to update: "))
        if 1 <= product_update <= len(products):
            new_name = input(f"Enter the new product name: ")
            new_price = float(input(f"Enter the new price: "))

            products[product_update -1]['name'] = new_name
            products[product_update -1]['price'] = new_price
            
            print("Product updated successfully!")

        else:
            print("This is not a valid option")

    except ValueError:
        print("Invalid selection, please enter a number")

# Allow user to delete a product from the list using index selection. But first lists the products out 
# uses pop() to remive the selected item

def delete_product(drink_products, food_products):
    if not drink_products and not food_products:
        print("No products to delete")
        return
    
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
        print(f"{index}. {product['name']} - £{product['price']}")

    try:
        delete_index = int(input("Enter the number of the product you wish to delete: "))
        if 1 <= delete_index <= len(products):
            removed_item = products.pop(delete_index - 1)
            print(f"Deleted '{removed_item}' successfully!")

            #re-index the updated list of products
            for index, product in enumerate(products, start=1):
                product["index"] = index


        else:
            print("Invalid selection, enter a valid product number")

    except ValueError:
        print("Invalid input, please enter a number")
