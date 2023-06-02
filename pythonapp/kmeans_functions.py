import pandas as pandas
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def rename_columns(df, old_name, new_name):
  df.rename(columns = {old_name: new_name}, inplace=True)
  print(f"✅ Renamed column {old_name} to {new_name}")

def drop_column(df, column_name):
  df.drop([column_name], axis = 1, inplace = True)
  print(f"✅ dropped column {column_name}")


def customer_segmentation(df, annual_income, spending_score):
  # Extract the correct columns
  columns = df[["annual income (k$)", "spending score (1-100)"]]
  # Scale the data
  scaler = StandardScaler()
  columns_scaled = scaler.fit_transform(columns)

  # Choose optimal number of clusters
  n_clusters = 5

  # Perform KMeans Clustering
  kmeans  = KMeans(n_clusters = n_clusters, init = "k-means++", random_state = 42)
  kmeans.fit(columns_scaled)

  # Predict the cluster for the given input
  customer_data = scaler.transform([[annual_income, spending_score]])
  cluster = kmeans.predict(customer_data)

  return cluster[0]