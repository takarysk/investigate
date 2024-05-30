import pandas as pd
import japanize_matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt

df = pd.read_parquet("C:/Users/takah/investigate/Navya-202311-date.parquet")

# df = df.drop(range(0, 4))

x = "timestamp"
y = "geo_position_high"

df.plot(x=x, y=y, figsize=(10, 6))
plt.title("geo_position_high")
plt.xlabel(x, fontsize=15)
plt.ylabel(y, fontsize=15)
plt.xlim("2023-11-02 00:00:00", "2023-11-19 23:59:59")
plt.ylim()
plt.grid(color="b", linestyle=":", linewidth="0.3")
plt.show()
