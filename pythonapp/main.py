import queries
import kmeans_functions
import argparse
import os
from alchemy_engine import EngineConnection

def main(annual_income, spending_score):
  engine = EngineConnection.get_instance()
  db_engine = engine.engine
  columns = [
    "CustomerID INT PRIMARY KEY",
    "Genre NVARCHAR(50)",
    "Age INT",
    "Annual_Income INT",
    "Spending_Score INT"
]

  queries.create_table('customers', columns, db_engine)
  queries.insert_csv(db_engine) 
  df = queries.create_df('customers', db_engine)
  kmeans_functions.rename_columns(df, 'Genre', 'Gender')
  kmeans_functions.drop_column(df, 'customerid')
  prediction = kmeans_functions.customer_segmentation(df, annual_income, spending_score)
  print(f"A customer with an annual income of {annual_income} and a spending score of {spending_score} belongs in customer group {prediction}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Enter the annual income and spending score you want to infer on")
    parser.add_argument("annual_income", type=int, default=os.environ.get("annual_income", 15), help="Annual income")
    parser.add_argument("spending_score", type=int, default=os.environ.get("spending_score", 33), help="Spending score")
    args = parser.parse_args()

    main(args.annual_income, args.spending_score)