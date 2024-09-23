import dash
import dash_core_components as dcc
import dash_html_components as html


app = dash.Dash()


app.layout = html.Div([
    html.Label('Choose a City'),
    
    dcc.Dropdown(
        id = 'first-dropdown',
        options= [
            {'label': 'Sanfranciso','value':'SF'},
            {'label': 'New York City','value':'NYC'},
            {'label': 'Rayleigh Durham','value':'RDU'}
        ],
        value = 'NYC'
    )
])



if __name__ == '__main__':
    app.run_server()