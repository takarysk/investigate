import json
import folium

data = None
# Navya_sample.jsonの呼び出し
with open("Navya_sample.json", "r") as Nav:
    data = json.load(Nav)

print(type(data[0]))
map_osm = folium.Map(
    location=[data[0]["geoPosition"]["lat"], data[0]["geoPosition"]["lon"]],
    zoom_start=16,
    tiles="OpenStreetMap",
)

for point in data:
    folium.Marker(
        location=[point["geoPosition"]["lat"], point["geoPosition"]["lon"]],
        popup=f"Altitude: {point['geoPosition']['high']}",
    ).add_to(map_osm)

map_osm.save("sample1.html")
