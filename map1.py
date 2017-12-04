import folium
import pandas

data = pandas.read_csv("nola.txt")
lat = list(data["LAT"])
lon = list(data["LONG"])
name = list(data['NAME'])
num = list(data['ID'])
icon = list(data['ICON'])

def change_color(num):
    if int(num)%2 == 0:
        return 'purple'
    elif int(num)%3 == 0:
        return 'orange'
    elif int(num)%5 == 0:
        return 'orange'
    else:
        return 'green'

attr = ('Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>')
tiles = 'https://stamen-tiles-{s}.a.ssl.fastly.net/watercolor/{z}/{x}/{y}.png'
#for more on custon tiles: http://nbviewer.jupyter.org/github/python-visualization/folium/blob/master/examples/TilesExample.ipynb

map = folium.Map(location=[29.9576213,-90.0731579], zoom_start=13, tiles=tiles, attr=attr)

#fgv=folium.FeatureGroup(name="My Population")
fgp=folium.FeatureGroup(name="My NOLA")

for lt, ln, nm, i, ic in zip(lat, lon, name, num, icon):
    fgp.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(nm, parse_html=True), icon=folium.Icon(color=change_color(i),icon=ic, angle=0, prefix="fa")))

#fgv.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
#else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

#map.add_child(fgv)
map.add_child(fgp)
#map.add_child(folium.LayerControl())
map.save("map1.html")
