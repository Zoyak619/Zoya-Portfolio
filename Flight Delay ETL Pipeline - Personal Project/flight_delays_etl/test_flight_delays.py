# testing all 3 stages of the ETL process 

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from flight_delays import extract_data, transform_data, load_data
import pytest
import psycopg2 as psycopg
import pandas as pd
from dotenv import load_dotenv
from unittest.mock import patch

# loads enviormants for the datbase connection 
load_dotenv()
host_name = os.environ.get("POSTGRES_HOST")
database_name = os.environ.get("POSTGRES_DB")
user_name = os.environ.get("POSTGRES_USER")
user_password = os.environ.get("POSTGRES_PASSWORD")

# file path for testing
test_file_path = "raw_data/2025.csv"

# fixture to create a small test dataframe (sample_df)
@pytest.fixture
def sample_df():
    return pd.DataFrame({
        "run_date": ["2025-03-14", "2025-03-14"],
        "reporting_airport": ["Aberdeen", "Aberdeen"],
        "origin_destination_country": ["United Kingdom", "Poland"],
        "origin_destination": ["Edinburgh", "Gdansk"],
        "airline_name": ["Loganair LTD", "Wizz Air"],
        "average_delay_mins": [22.0, 14.0],
        "number_flights_cancelled": [0, 1],
        "number_flights_matched": [10, 13]
    })

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                 Extract Test
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

# Happy case

def test_happy_extract_not_empty(): # test to see if csv file loads and is not empty 
    # Arrange
    file_path = test_file_path

    # Act
    df = extract_data(file_path)

    # Assert
    assert not df.empty, "Extraction failed, the Dataframe is empty"

def test_happy_extract_has_expected_columns(): # test to see the raw csv file contains all original column names
    # Arrange
    expected_columns = [
        "run_date", "reporting_airport", "origin_destination_country", "origin_destination",
        "airline_name", "average_delay_mins", "number_flights_cancelled", "number_flights_matched"
    ]
    
    # Act
    df = extract_data(test_file_path)

    # Assert
    for columns in expected_columns:
        assert columns in df.columns, f'missing columns; {columns}'

# Unhappy case

def test_unhappy_extract_invalid_file(): # testing wrong file path should raie error filenotfound 
    # Arrange
    wrong_file_path = "raw_data/2026.csv"

    # Act & Assert
    with pytest.raises(FileNotFoundError):
        extract_data(wrong_file_path) 

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                 Transform Test
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Happy case 

def test_happy_transforms_correct_columns(sample_df): # tests to see if columns have been renamed correctly 
    # Arrange 
    expected_columns = [
        "flight_date", "origin_airport", "destination_country", "destination_airport", "airline", "average_delay", 
        "num_flights_cancelled", "total_flights"
    ]

    # Act
    clean_df = transform_data(sample_df)

    # Assert
    assert list(clean_df.columns) == expected_columns, "Columns rename was unsccessful after transformation"

def test_happy_transform_correct_types(sample_df): # tests coloumns are converted to correct data types after transformation 
    # Arrange 
    expected_types = {
        "flight_date": "datetime64[ns]",
        "average_delay": "float64",
        "num_flights_cancelled": "int64",
        "total_flights": "int64"
    }
   
    # Act
    clean_df = transform_data(sample_df)

    # Assert 
    for column, expected_type in expected_types.items():
        assert clean_df[column].dtype == expected_type, f"{column} should be {expected_type}, got {clean_df[column].dtype}"

# Unhaappy case

def test_unhappy_transform_empty_dataframe(): # tests empty dataframe should raise an error.
    # Arrange 
    empty_df = pd.DataFrame()

    # Act & Assert
    with pytest.raises(KeyError):
        transform_data(empty_df)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                          Load Test
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Happy case

@patch("flight_delays.psycopg.connect") # mock db connection
def test_happy_load_data_success(mock_connect, sample_df): # tests dtata is intersted into db correctly 
    # Arrange
    # ensure sample df is in cleaned db format
    sample_df = sample_df.rename(columns={
        "run_date": "flight_date",
        "reporting_airport": "origin_airport",
        "origin_destination_country": "destination_country",
        "origin_destination": "destination_airport",
        "airline_name": "airline",
        "average_delay_mins": "average_delay",
        "number_flights_cancelled": "num_flights_cancelled",
        "number_flights_matched": "total_flights"
    })
    # setup mock connection and cursor
    mock_connection = mock_connect.return_value.__enter__.return_value
    mock_cursor = mock_connection.cursor.return_value

    # Act 
    load_data(sample_df)

    # Assert
    # tests sql was executed once per row
    assert mock_cursor.execute.call_count == len(sample_df), (
        f"Expected {len[sample_df]} SQL executions, got {mock_cursor.execute.call_count})"
    )
    # tests commit was called once
    mock_connection.commit.assert_called_once()


# Unhappy case

@patch("builtins.print")
@patch("flight_delays.psycopg.connect")
def test_unhappy_load_data_failure(mock_connect, mock_print, sample_df): # tests error handing when db connection fails
    # Arrange
    mock_connect.side_effect = Exception("DB connection failed")

    # ACt 
    load_data(sample_df)

    # Assert
    # tests id printed message includes expected text
    all_prints = [str(call.args) for call in mock_print.call_args_list]

    assert any("DB connection failed" in p for p in all_prints), (
        f"Expected 'DB connection failed' in printed outup, got: {all_prints}" 
    )
 