import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# --------- Import data
df = pd.read_csv('creditcard.csv')

# -------- Fig
fig = px.histogram(df, x='Class', color='Class')

# -------- App layout

app.layout = html.Div([
    dcc.Graph(figure=fig)
])

# -------- Run server
if __name__ == '__main__':
    app.run_server(debug=True)