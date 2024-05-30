import pandas as pd
from datetime import datetime, timedelta
import pytz

df = pd.read_parquet("C:/Users/takah/investigate/Navya-data-202311-all.parquet")

# print(df["timestamp"])
# print(type(df["timestamp"]))

# Unixエポックtimeをdatetimeに変換
# df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
jp = pytz.timezone("Asia/Tokyo")
df["timestamp"] = (
    df["timestamp"]
    .apply(
        lambda x: datetime.utcfromtimestamp(int(x) / 1000.0)
        + timedelta(hours=7)
        # .astimezone(jp)
    )
    .dt.floor("S")
)

# m/secをkm/hに変換
# df["speed_value"] = df["speed_value"] * 3.6

selected_df = df["speed_value"]
print(selected_df)

# df.to_parquet("./Navya-202311-date.parquet")
