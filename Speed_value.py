import pandas as pd
import japanize_matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/takah/investigate/autonomous-car-1-sjis.csv")

df = df.drop(range(0, 4))
# print(df)

# df["speedValue"] = pd.to_numeric(df["speedValue"])
# df["speedValue"] = -1 * df["speedValue"]
df["speedValue"] = 3.6 * df["speedValue"]
print(df["speedValue"])

print(df["speedValue"].describe())

x = "timestamp"
y = "speedValue"

df.plot(x=x, y=y, figsize=(10, 6))
# plt.title("")
# plt.xlabel("日付", fontsize=15)
# plt.ylabel("速度" + " (km/h)", fontsize=15)
# plt.xlim("2024-01-18 11:00:00.973786+09:00", "2024-01-18 15:49:59.815283+09:00")
# plt.ylim()
# plt.grid(color="b", linestyle=":", linewidth="0.3")
# plt.show()
