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

fig = px.histogram(df, x='Class', color='Class')
fig.show()