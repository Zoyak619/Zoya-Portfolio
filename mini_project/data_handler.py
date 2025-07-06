# load/read prodcuts/couriers and orders from a .csv file each time the app is used 
import csv

# This shows the paths to where the .csv files are stored - 
drink_file_path = "zoya-portfolio/mini_project/week-4/data/drinks_products.csv" 
food_file_path = "zoya-portfolio/mini_project/week-4/data/food_products.csv" 
courier_file_path = "zoya-portfolio/mini_project/week-4/data/couriers.csv"
order_file_path = "zoya-portfolio/mini_project/week-4/data/orders.csv"

# This reads each row in the drinks csv and adds it to the the drinks_products list and dictreader is sued to help assign the headers and keys automatically. the same format has been applied to food and courier function
with open (drink_file_path, mode='r') as drinks_file:
        drinks_reader = csv.DictReader(drinks_file)
        for row in drinks_reader:
            drink_products.append({"index": row["index"], "name": row['name'], "price": float(row['price'])})
            
            
with open(food_file_path, mode='r') as food_file:
        food_reader = csv.DictReader(food_file)
        for row in food_reader:
            food_products.append({"index": row["index"], "name": row['name'], "price": float(row['price'])})
            

with open (courier_file_path, mode='r') as courier_file:
        couriers_reader = csv.DictReader(courier_file)
        for row in couriers_reader:
            couriers.append({"index": row["index"],"name": row['name'], "phone": row['phone']})
            
# the same format has been used for orders but as they include lsts and multiple feilds. in the csv file the items_ordered is stored as a string via commas therefore to convert it back into a list i've used .spli(","). 
with open (order_file_path, mode='r') as orders_file:
    order_reader = csv.DictReader(orders_file)
    for row in order_reader:
        order = {
            "order_num": int(row["Order_Num"]),
            "customer_name": row["Customer_Name"],
            "customer_address": row["Customer_Address"],
            "customer_phone": row["Customer_Phone"],
            "courier": int(row["Courier"]),
            "status": row["Status"],
            "items_ordered": row["Items_Ordered"].split(",")
        }
        orders.append(order)

        # saves the updated data using csv. 
        import csv
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
                writer.writerow(order)
        break # ends while loop and exists the app 
    