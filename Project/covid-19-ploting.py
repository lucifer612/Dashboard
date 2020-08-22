# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 18:41:11 2020

@author: HK
"""

from matplotlib import pyplot as plt
import pandas as pd
# For Regular Expressions
# For working with geographical data
import json

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio
import plotly.express as px
import plotly
from plotly.offline import iplot

#### ----- Step 1 (import data)----
df1 = pd.read_csv("E:\Study\sem7\BDAD\Covid-19\data\latest_stats.csv")
df2 = pd.read_csv("E:\Study\sem7\BDAD\Covid-19\data\date_wise_totals.csv")

#### ----- Step 2 (Plot data)----

trace = go.Pie(labels = df1["Location"], values = df1["TotalConfirmed"])
data1 = [trace]
fig = go.Figure(data = data1)
iplot(fig)

fig1 = px.bar(df2,  x = 'Day', y = 'TotalConfirmed' , title="Covid Confirmed Cases")

        dash_table.DataTable(
            id='datatable_id',
            data=latest_stat.to_dict('records'),
            columns=[
                {"name": i, "id": i, "deletable": False, "selectable": False} for i in latest_stat.columns
            ]
        )