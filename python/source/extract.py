import pandas as pd

def extract_data():
  df=pd.read_csv("../files/sales.csv")
  print(df.head())