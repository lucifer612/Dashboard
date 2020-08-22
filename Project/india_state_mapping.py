# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 16:34:43 2020

@author: HK
"""

import pandas as pd
# For Regular Expressions
# For working with geographical data
import json
import plotly.express as px
import plotly.io as io
io.renderers.default = 'firefox'

df = pd.read_csv("E:\Study\sem7\BDAD\Covid-19\data\latest_stats.csv")

indian_state = json.load(open("E:/Study/sem7/BDAD/Covid-19/data/indian_states.json",'r'))
#print(indian_state["features"][2]['properties'])


stat_id_map = {}

for feature in indian_state["features"]:
    feature['id'] = feature['properties']['ID_1']
    stat_id_map[feature['properties']['NAME_1']] = feature['id']
    
df["id"] = df["Location"].apply(lambda x: stat_id_map[x])

print(df)


fig1 = px.choropleth(df , locations="id" , geojson="indian_state" , color = "Active" , scope=("asia"))
fig1.show()





