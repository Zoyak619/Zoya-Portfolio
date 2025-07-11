# load/read prodcuts/couriers and orders from a .csv file each time the app is used 
import csv

# This shows the paths to where the .csv files are stored - 
order_file_path ="Data/orders.csv"

 # This reads each row in the orders csv and dictreader is used to help assign the headers and keys automatically. in the csv file the items_ordered is stored as a string via commas therefore to convert it back into a list i've used .split(","). 


def load_data():
     orders = []
     try:
         with open (order_file_path, mode='r') as orders_file:
            order_reader = csv.DictReader(orders_file)
            for row in order_reader: # skips rows that are empty or missing the order_num field 
                if not row["order_num"]:
                    continue
                order = {
                "order_num": int(row["order_num"]),
                "customer_name": row["customer_name"],
                "customer_address": row["customer_address"],
                "customer_phone": row["customer_phone"],
                "courier": row["courier"],
                "status": row["status"],
                "items_ordered": row["items_ordered"].split(",") # converts from csv string to list 
                }
                
                orders.append(order)
     except FileNotFoundError:
         print("Orders file not found")

     # returns all loaded data after files are read 
     return orders

# saves files 

def save_data(orders):

    # feild names show the headrs off each csv file
    orders_fieldnames = ["order_num", "customer_name", "customer_address", "customer_phone", "courier", "status", "items_ordered"]
   
# uses dictwriter to save data in each csv file using the headers and data implemented.  
          
    with open(order_file_path, mode='w', newline ='') as order_file:
        writer = csv.DictWriter(order_file, fieldnames=orders_fieldnames)
        writer.writeheader()
        for order in orders:
            order_copy = order.copy() #This copies the order and converts items_ordered back to a string
            order_copy["items_ordered"] = ",".join(order_copy["items_ordered"])
            writer.writerow(order_copy)
            