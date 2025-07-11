# load/read prodcuts/couriers and orders from a .csv file each time the app is used 
import csv

def load_data():
     drink_products = []
     food_products = []
     couriers = []
     orders = []
    # This shows the paths to where the .csv files are stored - 
     drink_file_path = "Data/drink_products.csv" 
     food_file_path = "Data/food_products.csv" 
     courier_file_path = "Data/couriers.csv"
     order_file_path = "Data/orders.csv"

# This reads each row in the drinks csv and adds it to the the drinks_products list and dictreader is sued to help assign the headers and keys automatically. the same format has been applied to food and courier function
     with open (drink_file_path, mode='r') as drinks_file:
        drinks_reader = csv.DictReader(drinks_file)
        for row in drinks_reader:
             if not row["index"]: # skips rows that are empyt or missing the index feild 
                 continue
             drink_products.append({"index": int(row["index"]), "name": row['name'], "price": float(row['price'])})
            
            
     with open(food_file_path, mode='r') as food_file:
        food_reader = csv.DictReader(food_file)
        for row in food_reader:
             if not row["index"]: # skips rows that are empyt or missing the index feild 
                 continue
             food_products.append({"index": int(row["index"]), "name": row['name'], "price": float(row['price'])})
            

     with open (courier_file_path, mode='r') as courier_file:
        couriers_reader = csv.DictReader(courier_file)
        for row in couriers_reader:
             if not row["index"]: # skips rows that are empyt or missing the index feild 
                 continue
             couriers.append({"index": int(row["index"]),"name": row['name'], "phone": row['phone']})
            
# the same format has been used for orders but as they include lsts and multiple feilds. in the csv file the items_ordered is stored as a string via commas therefore to convert it back into a list i've used .spli(","). 
     with open (order_file_path, mode='r') as orders_file:
        order_reader = csv.DictReader(orders_file)
        for row in order_reader: # skips rows that are empyt or missing the order_num feild 
            if not row["order_num"]:
                continue
            order = {
            "order_num": int(row["order_num"]),
            "customer_name": row["customer_name"],
            "customer_address": row["customer_address"],
            "customer_phone": row["customer_phone"],
            "courier": row["courier"],
            "status": row["status"],
            "items_ordered": row["items_ordered"].split(",")
            }
            orders.append(order)

    # returns all loaded data after files are read 
     return drink_products, food_products, couriers, orders
    

# saves files 

def save_data(drink_products, food_products, couriers, orders):
     # This shows the paths to where the .csv files are stored - 
    drink_file_path = "Data/drink_products.csv" 
    food_file_path = "Data/food_products.csv" 
    courier_file_path = "Data/couriers.csv"
    order_file_path = "Data/orders.csv"

    # feild names show the headrs off each csv file
    drinks_fieldnames = ["index", "name", "price"]
    food_fieldnames = ["index", "name", "price"]
    couriers_fieldnames = ["index", "name", "phone"]
    orders_fieldnames = ["order_num", "customer_name", "customer_address", "customer_phone", "courier", "status", "items_ordered"]
   
# uses dictwriter to save data in each csv file using the headers and data implemented.  
    with open(drink_file_path, mode='w', newline ='') as drinks_file:
        writer = csv.DictWriter(drinks_file, fieldnames=drinks_fieldnames)
        writer.writeheader()           
        for product in drink_products:
            writer.writerow(product)
    
    with open(food_file_path, mode='w', newline ='') as food_file:
        writer = csv.DictWriter(food_file, fieldnames=food_fieldnames)
        writer.writeheader()
        for product in food_products:
            writer.writerow(product)
     
    with open(courier_file_path, mode='w', newline ='') as couriers_file:
        writer = csv.DictWriter(couriers_file, fieldnames=couriers_fieldnames)
        writer.writeheader()
        for courier in couriers:
            writer.writerow(courier)
    
          
    with open(order_file_path, mode='w', newline ='') as order_file:
        writer = csv.DictWriter(order_file, fieldnames=orders_fieldnames)
        writer.writeheader()
        for order in orders:
            order_copy = order.copy() #This oopies the ordder and converts it back to a csv string
            order_copy["items_ordered"] = ",".join(order_copy["items_ordered"])
            writer.writerow(order_copy)
            