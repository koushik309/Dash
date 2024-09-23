import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

colors = {
    'text': '#ff0000',
    'plot_color':'#D3D3D3',
    'paper_color':'#00FFFF'
}

app.layout = html.Div([
    html.H1(children = 'Hello Dash!!!',
            style ={
                'textAlign': 'center',
                'color': colors['text'] #RED
            }
            ),
    html.Div(children = 'Dash - A data product developement framework from display',
             style ={
                'textAlign': 'center',
                'color': colors['text']
            }
            ),
    dcc.Graph(
        id = 'sample-graph',
        figure={
            'data': [
                {'x':[4,6,8],'y':[12,16,18],'type':'bar','name': 'first chart'},
                {'x':[4,5,6],'y':[20,24,26],'type':'bar','name': 'second chart'}
            ],
            'layout': {
                'plot_bgcolor': colors['plot_color'],
                'paper_bgcolor' : colors['paper_color'],
                'font': {
                  'color': colors['text']  
                },
                'title': 'simple bar chart'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(port= 4050)  