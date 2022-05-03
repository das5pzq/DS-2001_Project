# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 16:42:50 2022

@author: Emma
"""

import pandas as pd
import numpy as np
#import plotly 
#import plotly.graph_objects as go
import matplotlib.pyplot as plt
#import plotly.express as px

data = pd.read_csv('Data.csv')
data_broadband = data.dropna(subset = ['Country','Broadband Speed Rank','Broadband Mbps'])
data_mobile = data.dropna(subset = ['Country','Mobile Speed Rank','Mobile Mbps'])

data_broadband.to_csv('Broadband.csv')
data_mobile.to_csv('Mobile.csv')

### Need to finish this part ###
GDPs = pd.read_csv('gdp.csv')
#https://datahub.io/core/gdp
GDPs.dropna(subset=['2020'])
for Country in GDPs['Country'] and data_broadband['Country']:
    x = GDPs['2020']/10**12
    colors = range(len(GDPs['Country']))
    y = data_broadband['Broadband Speed Rank']
    plt.scatter(x,y,c=colors)