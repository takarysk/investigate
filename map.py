import pandas as pd
import folium
import japanize_matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta
from folium.features import CustomIcon

df = pd.read_parquet("C:/Users/takah/investigate/Navya-202311-date.parquet")

start_time = pd.to_datetime("2023-11-02 10:00:00")
end_time = pd.to_datetime("2023-11-02 16:00:00")
df = df[(df["timestamp"] >= start_time) & (df["timestamp"] <= end_time)]

# df = df[df.index.second % 10 == 0]

df = df[::10]
print(df)

map_osm = folium.Map(
    location=[df.iloc[0]["geo_position_lat"], df.iloc[0]["geo_position_lon"]],
    zoom_start=16.9,
)

for index, row in df.iterrows():
    popup = folium.Popup(max_width=200)
    if row["robot_mode_mode"] == "MANUAL":
        folium.Marker(
            [row["geo_position_lat"], row["geo_position_lon"]],
            icon=folium.Icon(color="orange", size=100),
        ).add_to(map_osm)
    # if row["robot_mode_mode"] == "AUTO":
    #     folium.Marker(
    #         [row["geo_position_lat"], row["geo_position_lon"]],
    #         icon=folium.Icon(color="blue"),
    #     ).add_to(map_osm)

# bus_stop = [["JR四日市駅前", "裁判所前", "近鉄四日市駅前", "市役所前"], []]


# JR_yokkaiti = [34.965835], [136.618572]
# folium.Marker(
#     location=[34.965835, 136.618572],
#     icon=CustomIcon(
#         icon_image="C:/Users/takah/investigate/bus_stop2.png", icon_size=(55, 65)
#     ),
# ).add_to(map_osm)


df["geo_position_lat"] = df["geo_position_lat"].astype(float)
df["geo_position_lon"] = df["geo_position_lon"].astype(float)
geo_position = [
    (lat, lon) for lat, lon in zip(df["geo_position_lat"], df["geo_position_lon"])
]

folium.PolyLine(geo_position, weight=2, color="blue").add_to(map_osm)

map_osm.save("plot_map.html")
