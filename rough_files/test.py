import plotly.graph_objects as go
import plotly
import plotly.express as px
import numpy as np
import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

df = pd.read_csv('../creditcard.csv')

fig = go.Figure()

# add traces
fig.add_trace(go.Scatter(x=df.Time[df.Class == 0], y=df.Amount[df.Class == 0], mode='markers', name='Class 0'))
fig.add_trace(go.Scatter(x=df.Time[df.Class == 1], y=df.Amount[df.Class == 1], mode='markers', name='Class 1'))

fig.update_layout(
    updatemenus=[go.layout.Updatemenu(
        active=0,
        buttons=list(
            [dict(label='All',
                  method='update',
                  args=[{'visible': [True, True]},
                        {'title': 'All',
                         'showlegend': True}]),
             dict(label='Class 0',
                  method='update',
                  args=[{'visible': [True, False]},
                        {'title': 'Class 0',
                         'showlegend': True}]),
             dict(label='Class 1',
                  method='update',
                  args=[{'visible': [False, True]},
                        {'title': 'Class 1',
                         'showlegend': True}]),
             ]
        )
    )]
)

fig.show()


