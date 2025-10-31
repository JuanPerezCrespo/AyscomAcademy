from source.extract import read_csv
import pandas as pd
from io import StringIO


def transform_data(csv_content):
    # Usar StringIO para que pd.read_csv pueda leer desde el string csv_content
    df = pd.read_csv(StringIO(csv_content))
    df = df.drop_duplicates()
    # Change string columns to lowercase
    string_cols = df.select_dtypes(include='object').columns
    for col in string_cols:
        df[col] = df[col].str.lower()
    df['Total'] = df['Quantity'].astype(float) * df['Price'].astype(float)
    print(df)



