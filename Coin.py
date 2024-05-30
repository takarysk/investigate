import requests
import time
from datetime import datetime
import json
import matplotlib.pyplot as plt
from matplotlib import animation


url = "https://coincheck.com/api/exchange/orders/rate"


rate_list = []
time_list = []


def _update(frame):
    plt.cla()

    response = requests.get(
        url, params={"order_type": "buy", "pair": "btc_jpy", "amount": "0.1"}, timeout=1
    )
    time_list.append(datetime.now())
    res_dict = json.loads(response.text)
    rate_list.append(res_dict["rate"])
    print(res_dict["rate"])
    print(rate_list)

    plt.plot(time_list, rate_list)


fig, ax = plt.subplots()

params = {"fig": fig, "func": _update, "frames": 1, "interval": 5000, "repeat": True}


anime = animation.FuncAnimation(**params)
plt.plot(time_list, rate_list)
plt.xticks(rotation=90)
plt.show()
