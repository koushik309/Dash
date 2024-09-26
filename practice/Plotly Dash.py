import dash
from dash import dcc, html
import plotly.graph_objs as go
import pandas as pd
import numpy as np

app = dash.Dash(__name__)

np.random.seed(50)
x_rand = np.random.randint(1, 61, 60)
y_rand = np.random.randint(1, 61, 60)

orders = pd.read_excel('sales.xls')


colors = {
    'text': '#ff0000',
    'plot_color': '#D3D3D3',
    'paper_color': '#00FFFF'
}

app.layout = html.Div([
    html.H1(children='Hello Dash!!!',
            style={
                'textAlign': 'center',
                'color': colors['text']
            }
            ),
    html.Div(children='Dash - A data product development framework from display',
             style={
                 'textAlign': 'center',
                 'color': colors['text']
             }
             ),
    dcc.Graph(
        id='sample-graph',
        figure={
            'data': [
                {'x': [4, 6, 8], 'y': [12, 16, 18], 'type': 'bar', 'name': 'first chart'},
                {'x': [4, 5, 6], 'y': [20, 24, 26], 'type': 'bar', 'name': 'second chart'}
            ],
            'layout': {
                'plot_bgcolor': colors['plot_color'],
                'paper_bgcolor': colors['paper_color'],
                'font': {
                    'color': colors['text']
                },
                'title': 'Simple Bar Chart'
            }
        }
    ),
    dcc.Graph(
        id='Scatter_chart',
        figure={
            'data': [
                go.Scatter(
                    x=orders.S,
                    y=orders.P,
                    mode='markers'
                )
            ],
            'layout': go.Layout(
                title='Scatter plot of random 60 points',
                xaxis={'title': 'Sales'},
                yaxis={'title': 'Profit'},
                hovermode = 'closest'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(port=4050)
    