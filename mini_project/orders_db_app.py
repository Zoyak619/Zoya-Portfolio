from dotenv import load_dotenv
import os
import psycopg2 as psycopg

# Load environment variables from .env file

load_dotenv()
host_name = os.environ.get("POSTGRES_HOST")
database_name = os.environ.get("POSTGRES_DB")
user_name = os.environ.get("POSTGRES_USER")
user_password = os.environ.get("POSTGRES_PASSWORD")

# connect to sql
# view orders 

def view_orders():
   try:
       with psycopg.connect(
           host=host_name,
           dbname=database_name,
           user=user_name,
           password=user_password
       ) as connection:
           
           cursor = connection.cursor()


           print('Viewing All Orders...\n')
           cursor.execute("""
               SELECT orders.order_id, orders.customer_name, orders.customer_address, orders.customer_phone,
                      couriers.name AS courier_name,
                      order_status.status AS status_name,
                      orders.items
               FROM orders
               INNER JOIN couriers ON orders.courier_id = couriers.courier_id
               INNER JOIN order_status ON orders.order_status_id = order_status.order_status_id
               ORDER BY orders.order_id ASC;
           """)

           orders = cursor.fetchall()
           for order in orders:
               print(f"""
Order ID: {order[0]}
Customer_Name: {order[1]}
Customer_Phone: {order[2]}
Customer_Address: {order[3]}
Courier: {order[4]}
Status: {order[5]}
Items: {order[6]}
{"-"*30}                                              
        """) # to seperate each order clearly from another when printing 
               cursor.close()

        # The connection will automatically close here 
   except Exception as ex:
       print('Failed to:', ex)


# add order 

def add_order(customer_name, customer_address, customer_phone, courier_id, order_status_id, items):
   try:
       with psycopg.connect(
           host=host_name,
           dbname=database_name,
           user=user_name,
           password=user_password
       ) as connection:
           
           cursor = connection.cursor()


           cursor.execute("""
               INSERT INTO orders (customer_name, customer_address, customer_phone,
                                   courier_id, order_status_id, items)
               VALUES (%s, %s, %s, %s, %s, %s)
               RETURNING order_id;
           """, (customer_name, customer_address, customer_phone,
                 courier_id, order_status_id, items))
           new_id = cursor.fetchone()[0]
           connection.commit()

           print(f"New order successfully added: {new_id}")
           cursor.close()

            
   except Exception as ex:
        print("Failed to add order:", ex)

# update a courier within the table 


def update_order_status(order_id, new_status_id):
   try:
       with psycopg.connect(
           host=host_name,
           dbname=database_name,
           user=user_name,
           password=user_password
       ) as connection:
           
           cursor = connection.cursor()

           cursor.execute("""
               UPDATE orders SET order_status_id = %s
               WHERE order_id = %s;
           """, (new_status_id, order_id))
           connection.commit()

           print(f"Order {order_id} status updated to {new_status_id}.")
           cursor.close()
            
   except Exception as ex:
        print("Failed to update order status:", ex)

# delete courier in sql 
 

def delete_order(order_id):
   try:
       with psycopg.connect(
           host=host_name,
           dbname=database_name,
           user=user_name,
           password=user_password
       ) as connection:
           
           cursor = connection.cursor()

           cursor.execute("DELETE FROM orders WHERE order_id = %s;", (order_id,))
           connection.commit()

           print(f"Order {order_id} deleted successfully.")
           cursor.close()

   except Exception as ex:
        print("Failed to delete order:", ex)


# view availble order statuses 
def view_order_statuses():
   try:
       with psycopg.connect(
           host=host_name,
           dbname=database_name,
           user=user_name,
           password=user_password
       ) as connection:
           
           cursor = connection.cursor()

           cursor.execute("SELECT order_status_id, status FROM order_status ORDER BY order_status_id ASC")
           statues = cursor.fetchall()

           print("\nOrder Status Options: ")
           for status in statues:
               print(f"{status[0]}: {status[1]}") # id and name 
           cursor.close()

   except Exception as ex:
        print("Failed to to load order statues:", ex)

# view orders by their status 
def view_orders_by_status(status_id):
   try:
       with psycopg.connect(
           host=host_name,
           dbname=database_name,
           user=user_name,
           password=user_password,
       ) as connection:
           cursor = connection.cursor()
           cursor.execute("""
               SELECT orders.order_id, orders.customer_name, order_status.status, couriers.name
               FROM orders
               INNER JOIN order_status ON orders.order_status_id = order_status.order_status_id
               INNER JOIN couriers ON orders.courier_id = couriers.courier_id
               WHERE orders.order_status_id = %s
           """, (status_id, ))
           results = cursor.fetchall()
           if results:
               print("\nOrders with selected status:")
               for order in results:
                   print(f"order_id: {order[0]}, name: {order[1]}, status: {order[2]}, courier: {order[3]}")
           else:
               print("No orders found with that status.")
   except Exception as ex:
       print("Failed to load order with that status:", ex)