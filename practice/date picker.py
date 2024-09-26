import dash
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime as dt

app = dash.Dash()


app.layout = html.Div([
dcc.DatePickerSingle(
    id = 'dt-pick-single',
    date = dt(2024,9,25) #yyyy,mm,dd
    
),

html.Br(),
dcc.DatePickerRange(
    id = 'dt-pick-range',
    start_date=dt(2015,5,10),
    end_date_placeholder_text='Select the date'
)

])



if __name__ == '__main__':
    app.run_server()