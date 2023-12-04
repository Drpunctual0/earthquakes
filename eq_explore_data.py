import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Verinin yapısını incele

filename = 'data2/eq_data_30_day_m1.json'

with open(filename) as f:
    all_eq_data = json.load(f)


all_eq_dicts = all_eq_data['features']

# Büyüklük / konum seçip almak

mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties'] ['mag']
    lon = eq_dict['geometry'] ['coordinates'] [0]
    lat = eq_dict['geometry'] ['coordinates'] [1]
    title = eq_dict['properties'] ['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)

# Depremlerin haritasını çıkar
data = [{
    'type' : 'scattergeo',
    'lon' : lons,
    'lat' : lats,
    'text' : hover_texts,
    'marker' : {
        'size' : [5*mag for mag in mags],
        'color' : mags,
        'colorscale' : 'YlOrRd',
        'reversescale' : False,
        'colorbar' : {'title' : 'Magnitude'}
    }
}]
my_layout = Layout(title = 'Global Earthquakes')

fig = {'data' : data, 'layout' : my_layout}
offline.plot(fig, filename='global_earthquakes.html')

# print(mags[:10])
# print(lons[:5])
# print(lats[:5])