import sys
import pandas as pd
import os

file_path = sys.argv[1]
print(f"Cleaning file: {file_path}")

df = pd.read_csv(file_path)
df = df.dropna()
df["product"] = df["product"].str.strip().str.lower()

filename = os.path.basename(file_path)
output_path = f"output/cleaned_{filename}"
os.makedirs("output", exist_ok=True)
df.to_csv(output_path, index=False)
print(f"Saved cleaned file to {output_path}")