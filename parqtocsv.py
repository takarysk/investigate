import pandas as pd

df = pd.read_parquet(
    "c:/Users/takah/investigate/part-00000-464cbeb3-9be0-48e1-8079-9c287f8f3b8d-c000.gz.parquet"
)
df.to_csv("Vehicle.csv")
