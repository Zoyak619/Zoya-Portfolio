# load the liabairries needed 
import psycopg2 as psycopg
import os
from dotenv import load_dotenv
import pandas as pd 

# Load environment variables from .env file for the datbase connection 
load_dotenv()
host_name = os.environ.get("POSTGRES_HOST")
database_name = os.environ.get("POSTGRES_DB")
user_name = os.environ.get("POSTGRES_USER")
user_password = os.environ.get("POSTGRES_PASSWORD")


# Extract data 
file_path = ("raw_data/2025.csv") # this is shows where the csv file is located 
def extract_data(file_path): # reads the csv file and creates a pandas datefram (df)
    print("\nExtracting data from csv  ")
    df = pd.read_csv(file_path) # this reads the csv file
        
    print(df)  # this prints the csv file as a dataframe (df) and shows the num of rows and columns
    print(df.info()) # this prints a summary of the dataframe which includes column names, num of non-null, data types, total rows and memory usage. 
    print("Data extracted successfully!!")
    return df

# Transform data
def transform_data(df): # cleans and trasform the raw flight data 
        print("\nTransforming data  ")

         # renames the columns to be more clean. - inplace=True tells pandas to modify the exisitng datatframe directtly nstead of making a copy. 
        df.rename(columns={"run_date": "flight_date", 
                                "reporting_airport": "origin_airport", 
                                "origin_destination_country": "destination_country", 
                                "origin_destination": "destination_airport", 
                                "airline_name": "airline", 
                                "average_delay_mins": "average_delay", 
                                "number_flights_cancelled": "num_flights_cancelled", 
                                "number_flights_matched": "total_flights"}, inplace=True)
        
        # coloumns which are kept 
        df = df[["flight_date", "origin_airport", "destination_country", "destination_airport", "airline", "average_delay", "num_flights_cancelled", "total_flights"]].copy() # pandas creates a new copy of the dataframe which can be modifyed

        # converts data type 
        df["flight_date"] = pd.to_datetime(df["flight_date"]) # convers flight_date from text (object) to datetime for date filtering/sorting 
        df["average_delay"] = df["average_delay"].astype(float) # converts average delay to a float for calculations 
        df["num_flights_cancelled"] = df["num_flights_cancelled"].astype(int) # converts num of flights to int as decimals are not needed 
        df["total_flights"] = df["total_flights"].astype(int) # converts total flights to int to allow proper counting 

        # remove duplicated data to aviod counting the same flight twice and inplace=true used again to modidy existing dataframe. 
        df.drop_duplicates()

        # handle missing values
        df.dropna(subset=["average_delay"]) # this will delete rows which has no average_delay data
        df["num_flights_cancelled"].fillna(0) # fills missing data with 0 in flights cancelled row as it assumes flight was not cancelled. 

        print("Data Transformed successfully!!")
        print(df.info()) #prints column types and counts after transformation 
        return df

# Load the new data into PostgreSQL
def load_data(clean_df): # loads the clean data into postgresql database 
    print("\nLoading data into PostgreSQL  ")
    
    #connects to postgresql 
    try:
        with psycopg.connect(
        host=host_name,
        dbname=database_name,
        user=user_name,
        password=user_password
        ) as connection:
            # creates a cursor to execute all SQL queries 
            cursor = connection.cursor()

            # loops through all the cleaned df and inserts init the database 
            for index, row in clean_df.iterrows():
                cursor.execute("""
                    INSERT INTO flight_delays
                    (flight_date, origin_airport, destination_country, destination_airport, airline, 
                    average_delay, num_flights_cancelled, total_flights)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """, (
                    row["flight_date"], row["origin_airport"], row["destination_country"], row["destination_airport"], row["airline"], 
                    row["average_delay"], row["num_flights_cancelled"], row["total_flights"]))
            
            # saves all changes to the database 
            connection.commit()
            # one all inserts have finished closes the cursor 
            cursor.close()

        print("Data loaded successfully!!")

            
    except Exception as ex:
        print("ETL process failed:", ex)

        
