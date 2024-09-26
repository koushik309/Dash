import dash
from dash import dcc
from dash import html
import yfinance as yf # install yfinance- 'pip install yfinance'
import datetime
from dash.dependencies import Input,Output

# Initialize the Dash app
app = dash.Dash()

# Define the app layout
app.layout = html.Div(children=[
    html.Div(
        children='symbol to graph.'
    ),
    dcc.Input(
    id ='input',
    value='',
    type= 'text'
),
    html.Div(id='output-graph'),
   
]),
@app.callback(
    Output(component_id='output-graph', component_property = 'children'),
    [Input(component_id='input', component_property='value')]
)
def update_graph(input_data):
    # Define the date range
    start = datetime.datetime(2015, 1, 1)
    end = datetime.datetime.now()
    # Fetch data using yfinance
    df = yf.download(input_data, start=start, end=end)
    return dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {
                    'x': df.index,
                    'y': df['Close'],
                    'type': 'line',
                    'name': input_data
                },
            ],
            'layout': {
                'title': input_data
            }
        }
    )


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
