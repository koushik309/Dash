import dash
import dash_core_components as dcc
import dash_html_components as html


app = dash.Dash()


app.layout = html.Div([
    #html.Label('Choose a City'),
    
    dcc.Dropdown(
        id = 'first-dropdown',
        options= [
            {'label': 'Sanfranciso','value':'SF'},
            {'label': 'New York City','value':'NYC'},
            {'label': 'Rayleigh Durham','value':'RDU','disabled':True}
        ],
        value = 'NYC',
        multi= True, #selecting multiple in the drop down
        placeholder='select a City'
    ),
    html.Label('This is a Slider'),
    dcc.Slider(
        min =1,
        max=10,
        value=5,
        step=0.5,
        marks = {i:i for i in range(10)} 
    ),
    html.Label('This is a range Slider'),
    dcc.Slider(
        min =1,
        max=10,
        step=0.5,
        value=[3,7],
        marks = {i:i for i in range(10)} 
    )
])



if __name__ == '__main__':
    app.run_server()