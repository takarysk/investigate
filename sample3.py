import json
import folium

data = None
# Navya_sample.jsonの呼び出し
with open("Navya_sample.json", "r") as Nav:
    data = json.load(Nav)

map_osm = folium.Map(
    location=[data[0]["geoPosition"]["lat"], data[0]["geoPosition"]["lon"]],
    zoom_start=14,
    tiles="OpenStreetMap",
)

points = [[43.181803611597374, 141.43170456594424]]

points = []
for point in data:
    location_point = [point["geoPosition"]["lat"], point["geoPosition"]["lon"]]
    popup = folium.Popup(
        f"Altitude: {point['geoPosition']['high']}"
        + "<br />"
        + f"Vehicle_Id: {point['vehicle_id']}",
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

map_osm.save("sample3.html")
