import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import dash_daq as daq
import plotly.express as px
import numpy as np
import datetime
from dash.dependencies import Output, Input

# ------ App

external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
        "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    }
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# ------ Read Data

df = pd.read_csv('../creditcard.csv')

df['Class'] = df['Class'].apply(str)


# convert to datetime
def to_hour(second):
    return datetime.datetime.utcfromtimestamp(second)


data_Time = df[['Time', 'Amount', 'Class']].copy()
data_Time['Date'] = data_Time.Time.apply(to_hour)
data_Time['Hour'] = data_Time.Date.dt.hour
data_Time.drop(['Time', 'Date'], axis=1, inplace=True)


# ------- Fig
fraud_split_graph = px.histogram(df, x='Class', color='Class')
day_transactions_graph = px.histogram(data_Time, x='Hour')


# ------ Layout

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.H1(
                    children="Credit Card Fraud Dashboard",
                    className="header-title"
                ),
                html.P(
                    children="Dashboard exploring the credit card fraud dataset",
                    className="header-description"
                ),
            ],
            className="header"
        ),

        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(figure=fraud_split_graph),
                    className="card"
                ),
            ],
            className="wrapper"
        ),

        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(figure=day_transactions_graph),
                    className="card"
                ),
            ],
            className="wrapper"
        ),


        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(children="Type", className="menu-title"),
                        dcc.Dropdown(
                            id="fraud-filter",
                            options=[
                                {"label": "Only Fraud", "value": "Fraud"},
                                {"label": "Only Non-Fraud", "value": "Non-Fraud"},
                                {"label": "All", "value": "All"},
                            ],
                            value="Only Fraud",
                            clearable=False,
                            className="dropdown"
                        ),
                    ],
                )
            ],
        ),
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id="transaction_amount-graph"
                    ),
                    className="card"
                ),
            ],
            className="wrapper"
        ),
    ]
)


@app.callback(
    Output("transaction_amount-graph", "figure"),
    [Input("fraud-filter", "value")]
)
def update_charts(transaction_type):
    if transaction_type == "Fraud":
        fig = px.scatter(x=df.Time[df.Class == "1"], y=df.Amount[df.Class == "1"])
    elif transaction_type == "Non-Fraud":
        fig = px.scatter(x=df.Time[df.Class == "0"], y=df.Amount[df.Class == "0"])
    else:
        fig = px.scatter(df, x="Time", y="Amount", color='Class')

    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
