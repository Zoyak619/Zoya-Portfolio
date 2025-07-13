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
# view products 
def view_products():
    try:
        with psycopg.connect(f"""
        host={host_name}
        dbname={database_name}
        user={user_name}
        password={user_password}
        """) as connection:
        
            cursor = connection.cursor()
   
   
            print('Viewing All products...')
            cursor.execute('SELECT product_id, name, price, category FROM products ORDER BY product_id ASC')

            products = cursor.fetchall()
            for product in products:
                print(f'product id: {product[0]}, Name: {product[1]}, Price: £{product[2]}, Category: {product[3]}')

            cursor.close()

        # The connection will automatically close here 
    except Exception as ex:
        print('Failed to:', ex)


# add product in sql database 

def add_product(name, price, category):
    try:
        with psycopg.connect(f"""
        host={host_name}
        dbname={database_name}
        user={user_name}
        password={user_password}
        """) as connection:
            
            cursor = connection.cursor()

            cursor.execute("INSERT INTO products ( name, price, category) VALUES (%s, %s, %s) RETURNING product_id;", (name, price, category))
            new_id = cursor.fetchone()[0]
            connection.commit()

            print(f"New product successfully added: {new_id}")
            cursor.close()
            
    except Exception as ex:
        print("Failed to add product:", ex)

# update a product within the table  

def update_product(product_id, new_name, new_price, new_category):
    try:
        with psycopg.connect(f"""
        host={host_name}
        dbname={database_name}
        user={user_name}
        password={user_password}
        """) as connection:
            
            cursor = connection.cursor()

            cursor.execute("UPDATE products SET name = %s, price = %s, category = %s WHERE product_id = %s;", (new_name, new_price, new_category, product_id))
            connection.commit()

            print(f"Product {product_id} has successully been updated!!")
            cursor.close()
            
    except Exception as ex:
        print("Failed to update product:", ex)

# delete product in sql 

def delete_product(product_id):
    try:
        with psycopg.connect(f"""
        host={host_name}
        dbname={database_name}
        user={user_name}
        password={user_password}
        """) as connection:
            
            cursor = connection.cursor()

            cursor.execute("DELETE FROM products WHERE product_id = %s;", (product_id,))
            connection.commit()

            print(f"Product {product_id} has successfully been deleted!")
            cursor.close()

    except Exception as ex:
        print("Failed to delete product:", ex)


