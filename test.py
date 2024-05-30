import pandas as pd

pd.set_option("display.max_columns", 2)
pd.set_option("display.max_rows", 2)
df = pd.read_csv("./Vehicle.csv")
print(df)
