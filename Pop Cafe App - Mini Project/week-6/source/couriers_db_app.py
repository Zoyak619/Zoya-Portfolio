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
# view couriers 

def view_couriers():
    try:
        with psycopg.connect(f"""
        host={host_name}
        dbname={database_name}
        user={user_name}
        password={user_password}
        """) as connection:
        
            cursor = connection.cursor()
   
   
            print('Viewing All Couriers...')
            cursor.execute('SELECT courier_id, name, phone FROM couriers ORDER BY courier_id ASC')

            couriers = cursor.fetchall()
            for courier in couriers:
                print(f'courier id: {courier[0]}, Name: {courier[1]}, phone: {courier[2]}')

            cursor.close()

        # The connection will automatically close here 
    except Exception as ex:
        print('Failed to:', ex)


# add courier 

def add_courier(name, phone):
    try:
        with psycopg.connect(f"""
        host={host_name}
        dbname={database_name}
        user={user_name}
        password={user_password}
        """) as connection:
            
            cursor = connection.cursor()

            cursor.execute("INSERT INTO couriers ( name, phone) VALUES (%s, %s) RETURNING courier_id;", (name, phone))
            new_id = cursor.fetchone()[0]
            connection.commit()

            print(f"New courier successfully added: {new_id}")
            cursor.close()
            
    except Exception as ex:
        print("Failed to add courier:", ex)

# update a courier within the table 


def update_courier(courier_id, new_name, new_phone):
    try:
        with psycopg.connect(f"""
        host={host_name}
        dbname={database_name}
        user={user_name}
        password={user_password}
        """) as connection:
            
            cursor = connection.cursor()

            cursor.execute("UPDATE couriers SET name = %s, phone = %s WHERE courier_id = %s;", (new_name, new_phone, courier_id))
            connection.commit()

            print(f"Courier {courier_id} has successully been updated!!")
            cursor.close()
            
    except Exception as ex:
        print("Failed to update courier:", ex)

# delete courier in sql 
 

def delete_courier(courier_id):
    try:
        with psycopg.connect(f"""
        host={host_name}
        dbname={database_name}
        user={user_name}
        password={user_password}
        """) as connection:
            
            cursor = connection.cursor()

            cursor.execute("DELETE FROM couriers WHERE courier_id = %s;", (courier_id,))
            connection.commit()

            print(f"Courier {courier_id} has successfully been deleted!")
            cursor.close()

    except Exception as ex:
        print("Failed to delete courier:", ex)
