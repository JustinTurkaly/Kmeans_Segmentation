import pandas as pd
from sqlalchemy import text
from sqlalchemy.engine import URL


def create_table(table_name, columns, engine):
    columns_definition = ', '.join(columns) # Convert list of columns to a string
    create_table_query = f"CREATE TABLE {table_name} ({columns_definition})"
      
    try:
        with engine.connect() as connection:
            connection.execute(text(create_table_query))
        print(f"✅ Table '{table_name}' created successfully.")
    except Exception as e:
        print(f"Error creating table '{table_name}': {e}")


def insert_csv(engine): 
  # Read the CSV file
    csv_file_path = '/Mall_Customers.csv'
    data = pd.read_csv(csv_file_path)

    # Insert the data into the table
    table_name = 'customers'
    data.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"✅ {csv_file_path} succesfully inserted into {table_name}")


def create_df(table_name, engine):
    query = 'SELECT * FROM customers'

    # Read the data into a pandas DataFrame using the existing engine instance
    df = pd.read_sql_query(query, engine)
    print(f"✅ {table_name} succesfully converted to pandas dataframe")

    # Now you can use the DataFrame 'df' with sklearn or any other operations
    return df
