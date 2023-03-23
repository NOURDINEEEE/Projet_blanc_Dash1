from dash import Dash, dcc, html, Input, Output, callback

from layouts import *
import callbacks

app = Dash(__name__, suppress_callback_exceptions=True)
server = app.server

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/France':
         return layout1
    elif pathname == '/EU':
         return layout2
    else:
        return layout1

if __name__ == '__main__':
    app.run_server(debug=True)