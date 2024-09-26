import dash
import dash_core_components as dcc
import dash_html_components as html


app = dash.Dash()


app.layout = html.Div([
dcc.Markdown(
    '''
    ### Dash and Markdown
    Dash supports [Markdown](https://github.com/koushik309).
    Clicking the link will be forwarded to my github.
    Markdown is a simple way to write and format text.
    It includes a syntax for things like **bold text** and *italics*,
    [links](https://github.com/koushik309), line 'code' snippets, lists, quotes, and more.
    '''
)

])



if __name__ == '__main__':
    app.run_server()