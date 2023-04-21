import requests
import json
import random
import datetime
import time
import pandas as pd
import numpy as np
import math
import folium
from folium import plugins
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.colorbar
import seaborn as sns

df_mexico = pd.read_csv('1_min.csv')
df_mexico.dropna()

with open('municipality_geo-json_shapes.json') as f:
    json_mexico = json.load(f)



latitud = 25.00
longitud = -100.00

ind = 'Percentage of Females of 15 to 29: 2010'

Col = list(df_mexico.columns[4:])
sns.heatmap(df_mexico.corr(),cmap='Reds')
plt.show()
sns.violinplot(data=df_mexico, x = 'State', y = 'Female Births: 1995', palette='winter')
plt.show()
sns.boxplot(data = df_mexico.sort_values(by=['Male Births: 2017'], ascending = False), x = 'Male Births: 2017', y = 'State')
plt.show()


mapa_mexico = folium.Map(location=[latitud, longitud], width=1000, height=700, zoom_start=3, min_zoom=5, max_zoom=15)

mapa_mexico.choropleth(geo_data=json_mexico, data=df_mexico,
    columns=['Code', ind],
    key_on='feature.properties.mun_code',
    fill_color='YlGnBu', fill_opacity=1, 
    line_opacity=0.1
)
mapa_mexico