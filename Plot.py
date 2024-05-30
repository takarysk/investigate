import json
import folium
import pandas as pd

data = None


map_osm = folium.Map(
    location=[data[0]["geo_position.lat"], data[0]["geo_position.lon"]],
    zoom_start=14,
    tiles="OpenStreetMap",
)

points = [[43.1800933626798, 141.435447043045]]

points = []
table = []
for point in data:
    df = pd.DataFrame(
        [
            [point["timestamp"]],
            [point["geo_position.lat"]],
            [point["geo_position.lon"]],
        ],
        columns=["データ"],
        index=["時間", "緯度", "経度"],
    )
    location_point = [point["geo_position.lat"], point["geo_position.lon"]]
    popup = folium.Popup(
        df.to_html(),
        width=500,
        height=400,
        # f"Altitude: {point['geoPosition']['high']}"
        # + "<br />"
        # + f"Vehicle_Id: {point['vehicle_id']}",
    )
    folium.Marker(
        location=location_point,
        popup=popup,
        icon=folium.Icon(color="blue"),
        width=100,
        height=500,
    ).add_to(map_osm)
    points.append(location_point)

print(points)

folium.PolyLine(points, weight=5, color="#0000ff").add_to(map_osm)

map_osm.save("sample5.html")
