import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

df = pd.read_excel("C:/Users/takah/investigate/percent.xlsx")

plt.figure(figsize=(7, 5))
plt.plot(
    df["日付"],
    df["取得率"],
    marker="o",
    linestyle="-",
)

plt.title("データの取得率")
plt.xlabel("日付")
# plt.xlim("2023-11-02", "2023-11-19")

plt.show()
