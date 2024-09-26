import dash
from dash import dcc
from dash import html
from dash.dependencies import Output, Input  # Updated to use Input
import plotly.graph_objs as go
import random
from collections import deque 

# Initialize the deque to hold X and Y values
X = deque(maxlen=20)
Y = deque(maxlen=20)
X.append(1)
Y.append(1)

# Create the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    dcc.Graph(id='live-graph', animate=True),
    dcc.Interval(
        id='graph-update',
        interval=1000,  # Updates every second
        n_intervals=0   # Initial value for the intervals
    )
])

# Define the callback for updating the graph
@app.callback(Output('live-graph', 'figure'),
              Input('graph-update', 'n_intervals'))  # Trigger based on n_intervals
def update_graph(n):
    global X
    global Y
    X.append(X[-1] + 1)
    Y.append(Y[-1] + (Y[-1] * random.uniform(-0.1, 0.1)))

    data = go.Scatter(
        x=list(X),
        y=list(Y),
        name='Scatter',
        mode='lines+markers'
    )

    return {
        'data': [data],
        'layout': go.Layout(
            xaxis=dict(range=[min(X), max(X)]),
            yaxis=dict(range=[min(Y), max(Y)])
        )
    }

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
