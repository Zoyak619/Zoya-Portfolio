from dotenv import load_dotenv
import os
import psycopg2 as psycopg

# Load environment variables from .env file

load_dotenv()
host_name = os.environ.get("POSTGRES_HOST")
database_name = os.environ.get("POSTGRES_DB")
user_name = os.environ.get("POSTGRES_USER")
user_password = os.environ.get("POSTGRES_PASSWORD")


try:
    with psycopg.connect(f"""
    host={host_name}
    dbname={database_name}
    user={user_name}
    password={user_password}
    """) as connection:
        
        cursor = connection.cursor()

        # view products 

        print('Selecting all records...')
        cursor.execute('SELECT product_id, name, price, category FROM products ORDER BY product_id ASC')

        products = cursor.fetchall()
        for product in products:
            print(f'product id: {product[0]}, Name: {product[1]}, Price: £{product[2]}, Category: {product[3]}')

        cursor.close()

        # The connection will automatically close here 
except Exception as ex:
        print('Failed to:', ex)


# add product 

def add_product(name, price, category):
    try:
        with psycopg.connect(f"""
        host={host_name}
        dbname={database_name}
        user={user_name}
        password={user_password}
        """) as connection:
            
            cursor = connection.cursor()

            cursor.execute("INSERT INTO products ( name, price, category) VALUES (%S, %S, %S) RETURNING product_id;",
                           {name, price, category})
            new_id = cursor.fetchone()[0]
            connection.commit()

            print(f"New product added: {new_id}")
            cursor.close()
            
    except Exception as ex:
        price("Failed to add product:", ex)
        return None


    
