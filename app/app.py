from dash import Dash, dcc, html, Input, Output, callback

from layouts import *
import callbacks
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
server = app.server

app.layout = dbc.Container([
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
    elif pathname == '/Monde':
         return layout3
    else:
        return layout1

if __name__ == '__main__':
    app.run_server(debug=True)