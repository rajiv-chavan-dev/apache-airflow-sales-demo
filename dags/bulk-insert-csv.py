from airflow import DAG    
from airflow.operators.python_operator import PythonOperator
from datetime import datetime,timedelta
import pandas as pd
import psycopg2
import config

def reading_csv(csv_file_path):
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(csv_file_path)
        return df
    except Exception as e:
        print(f"Error reading CSV: {str(e)}")
        return None

def cleaning_csv(df):
    # You can add data cleaning logic here if needed
    return df

def insertion_csv(df, connection_params, table_name):
    try:
        conn = psycopg2.connect(**connection_params)
        
        cursor = conn.cursor()

        columns = ",".join(df.columns)
        placeholders = ",".join(["%s"] * len(df.columns))
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        
        for row in df.itertuples(index=False):
            cursor.execute(sql, tuple(row))
            
        conn.commit()
        print("data inserted successfully........")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error inserting data into PostgreSQL: {str(e)}")

def main():
    csv_file_path = 'organizations-100.csv'
    connection_params = {
         "dbname": config.database,
        "user": config.user,
        "password": config.password,
        "host": config.host,
        "port": config.port
    }
    table_name = 'demo'

    # Step 1: Read the CSV file
    df = reading_csv(csv_file_path)

    if df is not None:
        # Step 2: Clean the data (if needed)
        df = cleaning_csv(df)

        # Step 3: Insert data into PostgreSQL
        insertion_csv(df, connection_params, table_name)

default_args = {
    "owner":"rajiv.chavan",
    "depends_on_past":False,
    "start_date":datetime(2023,9,10),
    "retries":0,
    "retry_delay":timedelta(minutes=5),
}

dag = DAG('new_csv_postgresql',default_args = default_args,schedule_interval = timedelta(days=1))


task1 = PythonOperator(
    task_id = "new_csv_insertion",
    python_callable = main,
    dag = dag
)

task1
