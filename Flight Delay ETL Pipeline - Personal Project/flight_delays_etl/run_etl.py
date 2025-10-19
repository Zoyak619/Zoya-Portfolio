from flight_delays import extract_data, transform_data, load_data

file_path = "raw_data/2025.csv"


# run the ETL 
def run_etl():
   try:
     # Extract
     raw_df = extract_data(file_path)
     # Transform
     cleaned_df = transform_data(raw_df)
     # Load
     load_data(cleaned_df)

     print("\nETL process successfully completed!!")
     print("\nAll done!")

   except Exception as ex:
     print("ETL process fails:", ex)


# run ETL process
run_etl()