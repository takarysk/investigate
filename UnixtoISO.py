import pandas as pd
from datetime import datetime, timezone, timedelta

JST = timezone(timedelta(hours=+9), "JST")

df = pd.read_parquet("C:/Users/takah/investigate/Navya-data-202311-all.parquet")

# df = table.to_pandas()

df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms").apply(
    lambda x: x.strftime("%Y-%m-%dT%H:%M:%SZ")
)

print(df)
