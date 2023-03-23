from dash import dcc, html
import France_Data

layout1 = html.Div([
    html.H3('France'),
    dcc.Dropdown(
        {f'France - {i}': f'{i}' for i in ['PIB en fonction de l\'intensité de confinement', 'Evolution du PIB et de l\'indice d\'intensité de confinement', 'Evolution de nombre de vols passagers et de l\'intensité de confinement', 'Intensité de confinement et PIB en fonction du nombre total des cas']},
        id='page-1-dropdown'
    ),
    dcc.Graph(id='page-1-display-figure'),
    html.Div(id='page-1-display-value'),
    dcc.Link('Analyse EU', href='/EU')
])

layout2 = html.Div([
    html.H3('EU'),
    dcc.Dropdown(
        {f'EU - {i}': f'{i}' for i in ['PIB en fonction de l\'intensité de confinement', 'Evolution du PIB et de l\'indice d\'intensité de confinement', 'Evolution de nombre de vols passagers et de l\'intensité de confinement', 'Intensité de confinement et PIB en fonction du nombre total des cas']},
        id='page-2-dropdown'
    ),
    dcc.Graph(id='page-2-display-figure'),
    html.Div(id='page-2-display-value'),
    dcc.Link('Analyse France', href='/France')
])