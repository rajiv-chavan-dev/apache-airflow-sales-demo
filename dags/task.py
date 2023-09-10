import psycopg2
import pandas as pd
import config as config

class CSVToPostgreSQL:
    def __init__(self, csv_file, db_params):
        self.csv_file = csv_file
        self.db_params = db_params

    def extract_data(self):
        data = pd.read_csv(self.csv_file)
        return data

    def insert_into_postgresql(self, data):
        # Establish a connection to the PostgreSQL
        try:
            conn = psycopg2.connect(**self.db_params)
            cursor = conn.cursor()

            # SQL statement to insert data into a table
            table_name = "sales"
            columns = ",".join(data.columns)
            placeholders = ",".join(["%s"] * len(data.columns))
            sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

            # Insert data into the PostgreSQL database
            for row in data.itertuples(index=False):
                cursor.execute(sql, tuple(row))

            # Commit the changes and close the connection
            conn.commit()
            conn.close()
            print("Data inserted successfully.")
        except Exception as e:
            print(f"Error: {e}")

def main():
    # CSV file path
    csv_file = "organizations-100.csv"

    # PostgreSQL database connection parameters
    db_params = {
        "dbname": config.database,
        "user": config.user,
        "password": config.password,
        "host": config.host,
        "port": config.port
    }

    csv_to_postgresql = CSVToPostgreSQL(csv_file, db_params)
    data = csv_to_postgresql.extract_data()
    csv_to_postgresql.insert_into_postgresql(data)
