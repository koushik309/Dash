import dash
from dash import dcc
from dash import html
import time
import random
from collections import deque
import plotly.graph_objs as go
from dash.dependencies import Input, Output  # Updated dependencies

app = dash.Dash('vehicle-data')

# Deques to store data with a max length of 50
max_length = 50
times = deque(maxlen=max_length)
oil_temps = deque(maxlen=max_length)
intake_temps = deque(maxlen=max_length)
coolant_temps = deque(maxlen=max_length)
rpms = deque(maxlen=max_length)
speeds = deque(maxlen=max_length)
throttle_pos = deque(maxlen=max_length)

data_dict = {
    "Oil Temperature": oil_temps,
    "Intake Temperature": intake_temps,
    "Coolant Temperature": coolant_temps,
    "RPM": rpms,
    "Speed": speeds,
    "Throttle Position": throttle_pos,
}

# Function to update OBD values
def update_obd_values(times, oil_temps, intake_temps, coolant_temps, rpms, speeds, throttle_pos):
    times.append(time.time())
    if len(times) == 1:
        # Starting relevant values
        oil_temps.append(random.randrange(180, 230))
        intake_temps.append(random.randrange(95, 115))
        coolant_temps.append(random.randrange(170, 220))
        rpms.append(random.randrange(1000, 9500))
        speeds.append(random.randrange(30, 140))
        throttle_pos.append(random.randrange(10, 90))
    else:
        for data_of_interest in [oil_temps, intake_temps, coolant_temps, rpms, speeds, throttle_pos]:
            data_of_interest.append(data_of_interest[-1] + data_of_interest[-1] * random.uniform(-0.0001, 0.0001))

    return times, oil_temps, intake_temps, coolant_temps, rpms, speeds, throttle_pos

# Initialize OBD values
times, oil_temps, intake_temps, coolant_temps, rpms, speeds, throttle_pos = update_obd_values(
    times, oil_temps, intake_temps, coolant_temps, rpms, speeds, throttle_pos
)

# Layout of the dashboard
app.layout = html.Div([
    html.Div([
        html.H2('Vehicle Data', style={'float': 'left'}),
    ]),
    dcc.Dropdown(
        id='vehicle-data-name',
        options=[{'label': s, 'value': s} for s in data_dict.keys()],
        value=['Coolant Temperature', 'Oil Temperature', 'Intake Temperature'],
        multi=True
    ),
    html.Div(children=html.Div(id='graphs'), className='row'),
    dcc.Interval(id='graph-update', interval=100),  # Use interval without Event
], className="container", style={'width': '98%', 'margin-left': 10, 'margin-right': 10, 'max-width': 50000})


# Callback to update the graphs
@app.callback(
    Output('graphs', 'children'),
    [Input('vehicle-data-name', 'value'), Input('graph-update', 'n_intervals')]  # Use Input instead of Event
)
def update_graph(data_names, n_intervals):
    graphs = []
    update_obd_values(times, oil_temps, intake_temps, coolant_temps, rpms, speeds, throttle_pos)

    # Set layout based on number of selected data points
    if len(data_names) > 2:
        class_choice = 'col s12 m6 l4'
    elif len(data_names) == 2:
        class_choice = 'col s12 m6 l6'
    else:
        class_choice = 'col s12'

    # Generate graphs for each selected data point
    for data_name in data_names:
        data = go.Scatter(
            x=list(times),
            y=list(data_dict[data_name]),
            name='Scatter',
            fill="tozeroy",
            fillcolor="#6897bb"
        )

        graphs.append(html.Div(
            dcc.Graph(
                id=data_name,
                animate=True,
                figure={
                    'data': [data],
                    'layout': go.Layout(
                        xaxis=dict(range=[min(times), max(times)]),
                        yaxis=dict(range=[min(data_dict[data_name]), max(data_dict[data_name])]),
                        margin={'l': 50, 'r': 1, 't': 45, 'b': 1},
                        title='{}'.format(data_name)
                    )
                }
            ),
            className=class_choice
        ))

    return graphs


# External CSS and JS for styling
external_css = ["https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.min.css"]
for css in external_css:
    app.css.append_css({"external_url": css})

external_js = ['https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/js/materialize.min.js']
for js in external_js:
    app.scripts.append_script({'external_url': js})


if __name__ == '__main__':
    app.run_server(debug=True)




























