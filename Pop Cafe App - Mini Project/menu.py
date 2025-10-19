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
    print("1. View Products")
    print("2. Add Products")
    print("3. Update Products")
    print("4. Delete Products")
    print("0. Back to Main Menu") #returns back to main menu 

# sub menu for orders 
def order_menu():
    print("\n=== Orders Menu ===")
    print("1. View Orders")
    print("2. Add Order")
    print("3. Update Order Status")
    print("4. View Orders by Status")
    print("5. View Orders by Courier")
    print("6. Delete Order")
    print("0. Back to Main Menu")

# sub menu for couriers 
def courier_menu():
    print("\n=== Couriers Menu ===")
    print("1. View Courier")
    print("2. Add Courier")
    print("3. Update Courier")
    print("4. Delete Courier")
    print("0. Back to Main Menu")
