import dash
import dash_core_components as dcc
import dash_html_components as html


app = dash.Dash()


app.layout = html.Div([
html.Br(),
dcc.Textarea(
    placeholder='Input your feed back',
    value = 'Placeholder for text',
    style={'width':'50%'}
)
])



if __name__ == '__main__':
    app.run_server()