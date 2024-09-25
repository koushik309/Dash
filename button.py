import dash
import dash_core_components as dcc
import dash_html_components as html


app = dash.Dash()


app.layout = html.Div([
html.Br(),
    dcc.Textarea(
        placeholder = 'Input Your feedback',
        value = 'Place holder for Text',
        style = {'width': '50%'}
    ),
    html.Br(),
    html.Button('Submit',id = 'submit-form'),
    html.Br()
])



if __name__ == '__main__':
    app.run_server()