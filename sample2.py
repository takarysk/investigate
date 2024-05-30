import json
import folium

data = None
# Navya_sample.jsonの呼び出し
with open("Navya_sample.json", "r") as Nav:
    data = json.load(Nav)

map_osm = folium.Map(
    location=[data[0]["geoPosition"]["lat"], data[0]["geoPosition"]["lon"]],
    zoom_start=16,
    tiles="OpenStreetMap",
)

points = [[43.181803611597374, 141.43170456594424]]

points = []
for point in data:
    location_point = [point["geoPosition"]["lat"], point["geoPosition"]["lon"]]
    folium.Marker(
        location=location_point,
        popup=f"Altitude: {point['geoPosition']['high']}",
    ).add_to(map_osm)
    points.append(location_point)

print(points)

folium.PolyLine(points, weight=5, color="#0000ff").add_to(map_osm)

map_osm.save("sample2.html")
