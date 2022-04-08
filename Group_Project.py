# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 14:33:31 2022

@author: xXDRP
"""

import pandas as pd
import numpy as np
import plotly
import plotly.graph_objects as go
data = pd.read_csv('Dataset.csv')

data_broadband = data.dropna(subset = ['Country','Broadband Speed Rank','Broadband Mbps'])
data_mobile = data.dropna(subset = ['Country','Mobile Speed Rank','Mobile Mbps'])

data_broadband.to_csv('Broadband.csv')
data_mobile.to_csv('Mobile.csv')

from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    countries = json.load(response)

import plotly.express as px

fig = px.choropleth(data_broadband, geojson=countries)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()