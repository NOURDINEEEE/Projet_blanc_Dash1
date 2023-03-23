from dash import Input, Output, callback
from France_Data import *

input_list = ['PIB en fonction de l\'intensité de confinement', 'Evolution du PIB et de l\'indice d\'intensité de confinement', 'Evolution de nombre de vols passagers et de l\'intensité de confinement', 'Intensité de confinement et PIB en fonction du nombre total des cas']

@callback(
    Output('page-1-display-value', 'children'),
    Output('page-1-display-figure', 'figure'),
    Input('page-1-dropdown', 'value'))
def display_value(value):
    if value == 'France - PIB en fonction de l\'intensité de confinement' :
        return (f'Analyse de la figure : "{value}"', fig_2)
    elif value == 'France - Evolution du PIB et de l\'indice d\'intensité de confinement' :
        return (f'Analyse de la figure : "{value}"', fig_5)
    elif value == 'France - Evolution de nombre de vols passagers et de l\'intensité de confinement' :
        return (f'Analyse de la figure : "{value}"', fig_6)
    elif value == 'France - Intensité de confinement et PIB en fonction du nombre total des cas' :
        return (f'Analyse de la figure : "{value}"', fig_7)
    else :
        return (f'Analyse de la figure : "France - {input_list[0]}"', fig_2)
    

@callback(
    Output('page-2-display-value', 'children'),
    Input('page-2-dropdown', 'value'))
def display_value(value):
    return f'You have selected {value}'