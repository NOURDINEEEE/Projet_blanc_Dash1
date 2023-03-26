from dash import Input, Output, callback
from France_Data import *
from Projet_blanc_donnees_mondiales import Figure_STI51, Figure_STI15, Figure_STI5, Figure_STI2, Figure_STI4, Figure_STI11, Figure_STI13, Figure_STI14, Figure_STI12
from layouts import *
from Europe import *

input_list = ['PIB en fonction de l\'intensité de confinement', 'Evolution du PIB et de l\'indice d\'intensité de confinement', 'Evolution de nombre de vols passagers et de l\'intensité de confinement', 'Intensité de confinement et PIB en fonction du nombre total des cas']

@callback(
    Output("page-1-tab-content", "figure"),
    Output('page-1-tab-value', "children"),
    Input("page-1-tabs", "active_tab")
)
def display_value(tabs):
    if tabs == 'Graphe 1' :
        return (fig_2, "Analyse Graphe 1 : " + Commentaire_France_1)
    elif tabs == 'Graphe 2' :
        return (fig_5, "Analyse Graphe 2 : " + Commentaire_France_2)
    elif tabs == 'Graphe 3' :
        return (fig_6, "Analyse Graphe 3 : " + Commentaire_France_3)
    elif tabs == 'Graphe 4' :
        return (fig_7, "Analyse Graphe 4 : " + Commentaire_France_4)
    #return f'You have selected {value}'

@callback(
    Output("page-2-tab-content", "figure"),
    Output('page-2-tab-value', "children"),
    Input("page-2-tabs", "active_tab")
)
def display_value(tabs):
    if tabs == 'Graphe 1' :
        return (fig_GDP_STI_normalized, "Analyse Graphe 1 : " + commentaire_europe_gdp)
    elif tabs == 'Graphe 2' :
        return (fig_var_chomage_STI_normalized, "Analyse Graphe 2 : " + commentaire_europe_chomage)
    elif tabs == 'Graphe 3' :
        return (fig_Revenus_STI_normalized, "Analyse Graphe 3 : " + commentaire_europe_revenus)
#    elif tabs == 'Graphe 4' :
#        return (fig_7, "Analyse Graphe 4 : " + Commentaire_EU_4)

@callback(
    Output("page-3-tab-content", "figure"),
    Output('page-3-tab-value', "children"),
    Input("page-3-tabs", "active_tab")
)
def display_value(tabs):
    if tabs == 'Graphe 1' :
        return (Figure_STI51, "Analyse Graphe 1 : " + Commentaire_Monde_1)
    elif tabs == 'Graphe 2' :
        return (Figure_STI5, "Analyse Graphe 2 : " + Commentaire_Monde_2)
    elif tabs == 'Graphe 3' :
        return (Figure_STI2, "Analyse Graphe 3 : " + Commentaire_Monde_3)
    elif tabs == 'Graphe 4' :
        return (Figure_STI4, "Analyse Graphe 4 : " + Commentaire_Monde_4)
    elif tabs == 'Graphe 5' :
        return (Figure_STI15, "Analyse Graphe 5 : " + Commentaire_Monde_5)
    elif tabs == 'Graphe 6' :
        return (Figure_STI11, "Analyse Graphe 6 : " + Commentaire_Monde_6)
    elif tabs == 'Graphe 7' :
        return (Figure_STI13, "Analyse Graphe 7 : " + Commentaire_Monde_7)
    elif tabs == 'Graphe 8' :
        return (Figure_STI14, "Analyse Graphe 8 : " + Commentaire_Monde_8)
    elif tabs == 'Graphe 9' :
        return (Figure_STI12, "Analyse Graphe 9 : " + Commentaire_Monde_9)
#    elif tabs == 'Conclusion' :
#        return (Null, "Conclusion : " + Commentaire_Monde_10)

@callback(
    Output("page-4-tab-content", "children"),
    Output('page-4-tab-value', "children"),
    Input("page-4-tabs", "active_tab")
)
def display_value(tabs):
    if tabs == 'France' :
        return ("Conclusion de l'analyse au niveau de la France : ", "L'économie de la France a été affectée briefement par l'épidémie. Pourtant, cet effet n'était pas permanent, vu que le PIB, ainsi que les indicateurs économiques des différents secteurs, stabilisaient après la première période de COVID.")
    elif tabs == 'EU' :
        return ("Conclusion de l'analyse au niveau de l'Union Européenne : "+commentaire_europe_conclusion)
    elif tabs == 'Monde' :
        return ("Conclusion de l'analyse au niveau global : ", "L'afrique sub sahara (représenté par la Zambi) a un niveau de restriction (confinement) très faible par rapport au monde, ensuite l'Amérique latine (Mexique) a un niveau de restriction moyen, enfin le reste du monde a un niveau de restriction élevé (Afrique du Nord, Amérique du Nord, Asie du Sud) et voir très élevé (Chine). En conséquence l'Amérique latine et l'Asie ont eu la chute de niveau d'activité économique (chômage et croissance économique) la plus élevée dans le monde à contrario de l'Afrique en général qui a eu un plus faible impacte de la crise sanitaire (2020).")

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

@callback(
    Output('page-3-display-value', 'children'),
    Input('page-3-dropdown', 'value'))
def display_value(value):
    return f'You have selected {value}'

