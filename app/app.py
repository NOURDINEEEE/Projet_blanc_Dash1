from dash import Dash, dcc, html, Input, Output, callback

from layouts import *
import callbacks
import dash_bootstrap_components as dbc
from styles import *

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
server = app.server

sidebar = html.Div(
    [
        html.H6("Projet Blanc", className="display-4"),
        html.Hr(),
        html.P(
            "Analyse de l'effet économique du COVID sur 3 niveaux :", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("France", href="./France", active="exact"),
                dbc.NavLink("EU", href="./EU", active="exact"),
                dbc.NavLink("Monde", href="./Monde", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

#app.layout = dbc.Container([
#    dcc.Location(id='url', refresh=False),
#    html.Div(id='page-content')
#])

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