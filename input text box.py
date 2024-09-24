import dash
import dash_core_components as dcc
import dash_html_components as html


app = dash.Dash()


app.layout = html.Div([
    html.Label('This is  input box'),
    dcc.Input(
        placeholder =  'Input your name', 
        type = 'text',
        value=''
        
    ),
    
html.Br()
])



if __name__ == '__main__':
    app.run_server()