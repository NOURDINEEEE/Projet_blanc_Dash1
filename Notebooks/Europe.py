"""
Etude de l'effet de la COVID sur l'economie 
des 19 pays de la zone economique europeenne 
(19 pays avant le 01/01/2023)

CDL Printemps 2023
Groupe 2
"""


#%%     OUTILS


#%%         Librairies

import pandas as pd
import gzip
import numpy as np
import seaborn as sn
from datetime import datetime
import matplotlib.pyplot as plt

import plotly.graph_objects as go
import plotly.express as px


#%%         Fonctions

def annuel_to_quart (data_frame, col_dates, col_values, col_pays = '') :
        
    df_values = []
    df_dates = []
    
    if col_pays == '' :
        
        years_series = data_frame[col_dates]
        values_series = data_frame[col_values]
        
        for i in range (len(years_series)-1) :
            d = np.linspace(values_series[i], values_series[i+1], 5)
            for j in range (4) :
                df_values.append(d[j])
                df_dates.append(str(years_series[i].year)+'-Q'+str(j+1))
        
        df_values.append(values_series[len(years_series)-1])
        df_dates.append(str(years_series[len(years_series)-1].year)+'-Q'+str(1))
    
    
        df = pd.DataFrame()
        df['Quarter'] = df_dates  
        df['Quarter'] = pd.PeriodIndex(df['Quarter'], freq='Q').to_timestamp()
        df[col_values] = df_values
    
        return (df)
    
    else :
        
        loc = []
        
        for pays in list(data_frame[col_pays].unique()) : 
            years_series = data_frame.loc[data_frame[col_pays] == pays][col_dates].reset_index(drop = True)
            values_series = data_frame.loc[data_frame[col_pays] == pays][col_values].reset_index(drop = True)
        
            for i in range (len(years_series)-1) :
                d = np.linspace(values_series[i], values_series[i+1], 5)
                for j in range (4) :
                    loc.append(pays)
                    df_values.append(d[j])
                    df_dates.append(str(years_series[i].year)+'-Q'+str(j+1))
        
            loc.append(pays)
            df_values.append(values_series[len(years_series)-1])
            df_dates.append(str(years_series[len(years_series)-1].year)+'-Q'+str(1))
    
        df = pd.DataFrame()
        df[col_pays] = loc
        df['Quarter'] = df_dates  
        df['Quarter'] = pd.PeriodIndex(df['Quarter'], freq='Q').to_timestamp()
        df[col_values] = df_values
    
        return (df)

def moy_pond_par_population ( vdata_frame , vcol_valeurs , vcol_dates , vcol_pays , pdata_frame , pcol_dates) :
    
    df = pd.DataFrame(columns = [vcol_dates, vcol_valeurs])
    
    vDate = []
    MP = []
    
    for date in list(vdata_frame[vcol_dates].unique()) :
        if date in pdata_frame[pcol_dates].values :
            
            vals = vdata_frame.loc[vdata_frame[vcol_dates] == date][[vcol_valeurs, vcol_pays]].reset_index(drop = True)
            pop = pdata_frame.loc[pdata_frame[pcol_dates] == date]
            
            X = []
            P = []
            
            Spond = 0
            Spop = 0
            
            for pays in list(vals[vcol_pays].unique()) :
                if pays in list(pdata_frame.columns) : 
                    
                    Spond += (vals.loc[vals[vcol_pays] == pays][vcol_valeurs].mean()) * (pop[pays])
                    Spop += (pop[pays])
                    
                    X.append(vals.loc[vals[vcol_pays] == pays][vcol_valeurs].mean())
                    P.append(pays)
            
            if len (P) == (len(pdata_frame.columns)-2) : 
                moy_pond = float(Spond / Spop)
            else :
                moy_pond = np.nan
            
            vDate.append(date)
            MP.append(moy_pond)
            
    df[vcol_dates] = vDate
    df[vcol_valeurs] = MP

    return (df)


#%%         Listes des pays de la zone euro (avant 2023) 

_euro_area_19 = ['Austria', 'Belgium', 'Cyprus', 'Estonia', 'Finland', 'France', 'Germany', 'Ireland', 'Italy', 'Latvia', 'Lithuania', 'Luxembourg', 'Malta', 'Netherlands', 'Portugal', 'Slovakia', 'Slovenia', 'Spain', 'Greece']
_euro_area_19_ISO = ['AT', 'BE', 'CY', 'EE', 'FI', 'FR', 'DE', 'IE', 'IT', 'LV', 'LT', 'LU','MT', 'NL', 'PT', 'SK', 'SI', 'ES', 'GR' , 'EL']


#%%     EXTRACTION DES DONNEES


#%%         Chemins et colonnes a utiliser

_chemin_fichier_covid = '../Data/Data 2/owid-covid-data.csv'
_chemin_europe = '../Data/Donnees_Europe/'

_cols_covid_eur = ['location', 'date', 'total_cases_per_million', 
                    'new_cases_per_million', 'total_deaths_per_million', 
                    'new_deaths_per_million', 'reproduction_rate', 
                    'stringency_index']


#%%         Donnees relatives a la population de la Zone Euro 19 (avant 2023)

# Columns : ['TIME_PERIOD', 'OBS_VALUE']
# Periodicite : 'A'
# Unite : 'Millions of persons'
# Zone Geo : 'EuroArea19'
# Dates : 1995 -> 2022

population_Europe = pd.read_csv(_chemin_europe+'Europe_Population.csv', sep = ',', skiprows=5, usecols=[0,1])
population_Europe.columns = ['TIME_PERIOD', 'Europe']
population_Europe = population_Europe[::-1].reset_index(drop = True)
population_Europe['TIME_PERIOD'] = pd.to_datetime(population_Europe['TIME_PERIOD'], format = "%Y")

bd_population_eur = annuel_to_quart(population_Europe, 'TIME_PERIOD', 'Europe')
bd_population_eur = bd_population_eur.loc[pd.Timestamp('2000-01-01') <= bd_population_eur.Quarter].reset_index(drop = True)

del population_Europe

# -----------------------------------------------------------------------------------------------------

# Population par pays de la Zone Euro 19 (avant 2023)

population_Austria = pd.read_csv(_chemin_europe+'Population_Austria.csv', skiprows=5, usecols=[0,1])
population_Austria.columns = ['TIME_PERIOD', 'Austria']
population_Austria = population_Austria[::-1].reset_index(drop = True)
population_Austria['TIME_PERIOD'] = pd.to_datetime(population_Austria['TIME_PERIOD'], format = "%Y")

bd_pop_Austria = annuel_to_quart(population_Austria, 'TIME_PERIOD', 'Austria')
bd_pop_Austria = bd_pop_Austria.loc[pd.Timestamp('2000-01-01') <= bd_pop_Austria.Quarter].reset_index(drop = True)

data_eur_population = bd_population_eur.merge(bd_pop_Austria, on = 'Quarter', how = 'outer')

del population_Austria, bd_pop_Austria, bd_population_eur

# -----------------------------------------------------------------------------------------------------

population_Belgium = pd.read_csv(_chemin_europe+'Population_Belgium.csv', skiprows=5, usecols=[0,1])
population_Belgium.columns = ['TIME_PERIOD', 'Belgium']
population_Belgium = population_Belgium[::-1].reset_index(drop = True)
population_Belgium['TIME_PERIOD'] = pd.to_datetime(population_Belgium['TIME_PERIOD'], format = "%Y")

bd_pop_Belgium = annuel_to_quart(population_Belgium, 'TIME_PERIOD', 'Belgium')
bd_pop_Belgium = bd_pop_Belgium.loc[pd.Timestamp('2000-01-01') <= bd_pop_Belgium.Quarter].reset_index(drop = True)

data_eur_population = data_eur_population.merge(bd_pop_Belgium, on = 'Quarter', how = 'outer')

del population_Belgium, bd_pop_Belgium

# -----------------------------------------------------------------------------------------------------

population_Cyprus = pd.read_csv(_chemin_europe+'Population_Cyprus.csv', skiprows=5, usecols=[0,1])
population_Cyprus.columns = ['TIME_PERIOD', 'Cyprus']
population_Cyprus = population_Cyprus[::-1].reset_index(drop = True)
population_Cyprus['TIME_PERIOD'] = pd.to_datetime(population_Cyprus['TIME_PERIOD'], format = "%Y")

bd_pop_Cyprus = annuel_to_quart(population_Cyprus, 'TIME_PERIOD', 'Cyprus')
bd_pop_Cyprus = bd_pop_Cyprus.loc[pd.Timestamp('2000-01-01') <= bd_pop_Cyprus.Quarter].reset_index(drop = True)

data_eur_population = data_eur_population.merge(bd_pop_Cyprus, on = 'Quarter', how = 'outer')

del population_Cyprus, bd_pop_Cyprus

# -----------------------------------------------------------------------------------------------------

population_Estonia = pd.read_csv(_chemin_europe+'Population_Estonia.csv', skiprows=5, usecols=[0,1])
population_Estonia.columns = ['TIME_PERIOD', 'Estonia']
population_Estonia = population_Estonia[::-1].reset_index(drop = True)
population_Estonia['TIME_PERIOD'] = pd.to_datetime(population_Estonia['TIME_PERIOD'], format = "%Y")

bd_pop_Estonia = annuel_to_quart(population_Estonia, 'TIME_PERIOD', 'Estonia')
bd_pop_Estonia = bd_pop_Estonia.loc[pd.Timestamp('2000-01-01') <= bd_pop_Estonia.Quarter].reset_index(drop = True)

data_eur_population = data_eur_population.merge(bd_pop_Estonia, on = 'Quarter', how = 'outer')

del population_Estonia, bd_pop_Estonia

# -----------------------------------------------------------------------------------------------------

population_Finland = pd.read_csv(_chemin_europe+'Population_Finland.csv', skiprows=5, usecols=[0,1])
population_Finland.columns = ['TIME_PERIOD', 'Finland']
population_Finland = population_Finland[::-1].reset_index(drop = True)
population_Finland['TIME_PERIOD'] = pd.to_datetime(population_Finland['TIME_PERIOD'], format = "%Y")

bd_pop_Finland = annuel_to_quart(population_Finland, 'TIME_PERIOD', 'Finland')
bd_pop_Finland = bd_pop_Finland.loc[pd.Timestamp('2000-01-01') <= bd_pop_Finland.Quarter].reset_index(drop = True)

data_eur_population = data_eur_population.merge(bd_pop_Finland, on = 'Quarter', how = 'outer')

del population_Finland, bd_pop_Finland

# -----------------------------------------------------------------------------------------------------

population_France = pd.read_csv(_chemin_europe+'Population_France.csv', skiprows=5, usecols=[0,1])
population_France.columns = ['TIME_PERIOD', 'France']
population_France = population_France[::-1].reset_index(drop = True)
population_France['TIME_PERIOD'] = pd.to_datetime(population_France['TIME_PERIOD'], format = "%Y")

bd_pop_France = annuel_to_quart(population_France, 'TIME_PERIOD', 'France')
bd_pop_France = bd_pop_France.loc[pd.Timestamp('2000-01-01') <= bd_pop_France.Quarter].reset_index(drop = True)

data_eur_population = data_eur_population.merge(bd_pop_France, on = 'Quarter', how = 'outer')

del population_France, bd_pop_France

# -----------------------------------------------------------------------------------------------------

population_Germany = pd.read_csv(_chemin_europe+'Population_Germany.csv', skiprows=5, usecols=[0,1])
population_Germany.columns = ['TIME_PERIOD', 'Germany']
population_Germany = population_Germany[::-1].reset_index(drop = True)
population_Germany['TIME_PERIOD'] = pd.to_datetime(population_Germany['TIME_PERIOD'], format = "%Y")

bd_pop_Germany = annuel_to_quart(population_Germany, 'TIME_PERIOD', 'Germany')
bd_pop_Germany = bd_pop_Germany.loc[pd.Timestamp('2000-01-01') <= bd_pop_Germany.Quarter].reset_index(drop = True)

data_eur_population = data_eur_population.merge(bd_pop_Germany, on = 'Quarter', how = 'outer')

del population_Germany, bd_pop_Germany

# -----------------------------------------------------------------------------------------------------

population_Greece = pd.read_csv(_chemin_europe+'Population_Greece.csv', skiprows=5, usecols=[0,1])
population_Greece.columns = ['TIME_PERIOD', 'Greece']
population_Greece = population_Greece[::-1].reset_index(drop = True)
population_Greece['TIME_PERIOD'] = pd.to_datetime(population_Greece['TIME_PERIOD'], format = "%Y")

bd_pop_Greece = annuel_to_quart(population_Greece, 'TIME_PERIOD', 'Greece')
bd_pop_Greece = bd_pop_Greece.loc[pd.Timestamp('2000-01-01') <= bd_pop_Greece.Quarter].reset_index(drop = True)

data_eur_population = data_eur_population.merge(bd_pop_Greece, on = 'Quarter', how = 'outer')

del population_Greece, bd_pop_Greece

# -----------------------------------------------------------------------------------------------------

population_Ireland = pd.read_csv(_chemin_europe+'Population_Ireland.csv', skiprows=5, usecols=[0,1])
population_Ireland.columns = ['TIME_PERIOD', 'Ireland']
population_Ireland = population_Ireland[::-1].reset_index(drop = True)
population_Ireland['TIME_PERIOD'] = pd.to_datetime(population_Ireland['TIME_PERIOD'], format = "%Y")

bd_pop_Ireland = annuel_to_quart(population_Ireland, 'TIME_PERIOD', 'Ireland')
bd_pop_Ireland = bd_pop_Ireland.loc[pd.Timestamp('2000-01-01') <= bd_pop_Ireland.Quarter].reset_index(drop = True)

data_eur_population = data_eur_population.merge(bd_pop_Ireland, on = 'Quarter', how = 'outer')

del population_Ireland, bd_pop_Ireland

# -----------------------------------------------------------------------------------------------------

population_Italy = pd.read_csv(_chemin_europe+'Population_Italy.csv', skiprows=5, usecols=[0,1])
population_Italy.columns = ['TIME_PERIOD', 'Italy']
population_Italy = population_Italy[::-1].reset_index(drop = True)
population_Italy['TIME_PERIOD'] = pd.to_datetime(population_Italy['TIME_PERIOD'], format = "%Y")

bd_pop_Italy = annuel_to_quart(population_Italy, 'TIME_PERIOD', 'Italy')
bd_pop_Italy = bd_pop_Italy.loc[pd.Timestamp('2000-01-01') <= bd_pop_Italy.Quarter].reset_index(drop = True)

data_eur_population = data_eur_population.merge(bd_pop_Italy, on = 'Quarter', how = 'outer')

del population_Italy, bd_pop_Italy

# -----------------------------------------------------------------------------------------------------

population_Latvia = pd.read_csv(_chemin_europe+'Population_Latvia.csv', skiprows=5, usecols=[0,1])
population_Latvia.columns = ['TIME_PERIOD', 'Latvia']
population_Latvia = population_Latvia[::-1].reset_index(drop = True)
population_Latvia['TIME_PERIOD'] = pd.to_datetime(population_Latvia['TIME_PERIOD'], format = "%Y")

bd_pop_Latvia = annuel_to_quart(population_Latvia, 'TIME_PERIOD', 'Latvia')
bd_pop_Latvia = bd_pop_Latvia.loc[pd.Timestamp('2000-01-01') <= bd_pop_Latvia.Quarter].reset_index(drop = True)

data_eur_population = data_eur_population.merge(bd_pop_Latvia, on = 'Quarter', how = 'outer')

del population_Latvia, bd_pop_Latvia

# -----------------------------------------------------------------------------------------------------

population_Lithuania = pd.read_csv(_chemin_europe+'Population_Lithuania.csv', skiprows=5, usecols=[0,1])
population_Lithuania.columns = ['TIME_PERIOD', 'Lithuania']
population_Lithuania = population_Lithuania[::-1].reset_index(drop = True)
population_Lithuania['TIME_PERIOD'] = pd.to_datetime(population_Lithuania['TIME_PERIOD'], format = "%Y")

bd_pop_Lithuania = annuel_to_quart(population_Lithuania, 'TIME_PERIOD', 'Lithuania')
bd_pop_Lithuania = bd_pop_Lithuania.loc[pd.Timestamp('2000-01-01') <= bd_pop_Lithuania.Quarter].reset_index(drop = True)

data_eur_population = data_eur_population.merge(bd_pop_Lithuania, on = 'Quarter', how = 'outer')

del population_Lithuania, bd_pop_Lithuania

# -----------------------------------------------------------------------------------------------------

population_Luxembourg = pd.read_csv(_chemin_europe+'Population_Luxembourg.csv', skiprows=5, usecols=[0,1])
population_Luxembourg.columns = ['TIME_PERIOD', 'Luxembourg']
population_Luxembourg = population_Luxembourg[::-1].reset_index(drop = True)
population_Luxembourg['TIME_PERIOD'] = pd.to_datetime(population_Luxembourg['TIME_PERIOD'], format = "%Y")

bd_pop_Luxembourg = annuel_to_quart(population_Luxembourg, 'TIME_PERIOD', 'Luxembourg')
bd_pop_Luxembourg = bd_pop_Luxembourg.loc[pd.Timestamp('2000-01-01') <= bd_pop_Luxembourg.Quarter].reset_index(drop = True)

data_eur_population = data_eur_population.merge(bd_pop_Luxembourg, on = 'Quarter', how = 'outer')

del population_Luxembourg, bd_pop_Luxembourg

# -----------------------------------------------------------------------------------------------------

population_Malta = pd.read_csv(_chemin_europe+'Population_Malta.csv', skiprows=5, usecols=[0,1])
population_Malta.columns = ['TIME_PERIOD', 'Malta']
population_Malta = population_Malta[::-1].reset_index(drop = True)
population_Malta['TIME_PERIOD'] = pd.to_datetime(population_Malta['TIME_PERIOD'], format = "%Y")

bd_pop_Malta = annuel_to_quart(population_Malta, 'TIME_PERIOD', 'Malta')
bd_pop_Malta = bd_pop_Malta.loc[pd.Timestamp('2000-01-01') <= bd_pop_Malta.Quarter].reset_index(drop = True)

data_eur_population = data_eur_population.merge(bd_pop_Malta, on = 'Quarter', how = 'outer')

del population_Malta, bd_pop_Malta

# -----------------------------------------------------------------------------------------------------

population_Netherlands = pd.read_csv(_chemin_europe+'Population_Netherlands.csv', skiprows=5, usecols=[0,1])
population_Netherlands.columns = ['TIME_PERIOD', 'Netherlands']
population_Netherlands = population_Netherlands[::-1].reset_index(drop = True)
population_Netherlands['TIME_PERIOD'] = pd.to_datetime(population_Netherlands['TIME_PERIOD'], format = "%Y")

bd_pop_Netherlands = annuel_to_quart(population_Netherlands, 'TIME_PERIOD', 'Netherlands')
bd_pop_Netherlands = bd_pop_Netherlands.loc[pd.Timestamp('2000-01-01') <= bd_pop_Netherlands.Quarter].reset_index(drop = True)

data_eur_population = data_eur_population.merge(bd_pop_Netherlands, on = 'Quarter', how = 'outer')

del population_Netherlands, bd_pop_Netherlands

# -----------------------------------------------------------------------------------------------------

population_Portugal = pd.read_csv(_chemin_europe+'Population_Portugal.csv', skiprows=5, usecols=[0,1])
population_Portugal.columns = ['TIME_PERIOD', 'Portugal']
population_Portugal = population_Portugal[::-1].reset_index(drop = True)
population_Portugal['TIME_PERIOD'] = pd.to_datetime(population_Portugal['TIME_PERIOD'], format = "%Y")

bd_pop_Portugal = annuel_to_quart(population_Portugal, 'TIME_PERIOD', 'Portugal')
bd_pop_Portugal = bd_pop_Portugal.loc[pd.Timestamp('2000-01-01') <= bd_pop_Portugal.Quarter].reset_index(drop = True)

data_eur_population = data_eur_population.merge(bd_pop_Portugal, on = 'Quarter', how = 'outer')

del population_Portugal, bd_pop_Portugal

# -----------------------------------------------------------------------------------------------------

population_Slovakia = pd.read_csv(_chemin_europe+'Population_Slovakia.csv', skiprows=5, usecols=[0,1])
population_Slovakia.columns = ['TIME_PERIOD', 'Slovakia']
population_Slovakia = population_Slovakia[::-1].reset_index(drop = True)
population_Slovakia['TIME_PERIOD'] = pd.to_datetime(population_Slovakia['TIME_PERIOD'], format = "%Y")

bd_pop_Slovakia = annuel_to_quart(population_Slovakia, 'TIME_PERIOD', 'Slovakia')
bd_pop_Slovakia = bd_pop_Slovakia.loc[pd.Timestamp('2000-01-01') <= bd_pop_Slovakia.Quarter].reset_index(drop = True)

data_eur_population = data_eur_population.merge(bd_pop_Slovakia, on = 'Quarter', how = 'outer')

del population_Slovakia, bd_pop_Slovakia

# -----------------------------------------------------------------------------------------------------

population_Slovenia = pd.read_csv(_chemin_europe+'Population_Slovenia.csv', skiprows=5, usecols=[0,1])
population_Slovenia.columns = ['TIME_PERIOD', 'Slovenia']
population_Slovenia = population_Slovenia[::-1].reset_index(drop = True)
population_Slovenia['TIME_PERIOD'] = pd.to_datetime(population_Slovenia['TIME_PERIOD'], format = "%Y")

bd_pop_Slovenia = annuel_to_quart(population_Slovenia, 'TIME_PERIOD', 'Slovenia')
bd_pop_Slovenia = bd_pop_Slovenia.loc[pd.Timestamp('2000-01-01') <= bd_pop_Slovenia.Quarter].reset_index(drop = True)

data_eur_population = data_eur_population.merge(bd_pop_Slovenia, on = 'Quarter', how = 'outer')

del population_Slovenia, bd_pop_Slovenia

# -----------------------------------------------------------------------------------------------------

population_Spain = pd.read_csv(_chemin_europe+'Population_Spain.csv', skiprows=5, usecols=[0,1])
population_Spain.columns = ['TIME_PERIOD', 'Spain']
population_Spain = population_Spain[::-1].reset_index(drop = True)
population_Spain['TIME_PERIOD'] = pd.to_datetime(population_Spain['TIME_PERIOD'], format = "%Y")

bd_pop_Spain = annuel_to_quart(population_Spain, 'TIME_PERIOD', 'Spain')
bd_pop_Spain = bd_pop_Spain.loc[pd.Timestamp('2000-01-01') <= bd_pop_Spain.Quarter].reset_index(drop = True)

data_eur_population = data_eur_population.merge(bd_pop_Spain, on = 'Quarter', how = 'outer')

del population_Spain, bd_pop_Spain


#%%         Donnees relatives a la COVID

covid_Europe = pd.read_csv(_chemin_fichier_covid, usecols= _cols_covid_eur)

bd_covid_eur = covid_Europe.loc[covid_Europe.location.isin(_euro_area_19)]
bd_covid_eur['date'] = pd.to_datetime(bd_covid_eur['date'])
bd_covid_eur['Quarter'] = bd_covid_eur['date']
bd_covid_eur['Quarter'] = pd.PeriodIndex(bd_covid_eur['Quarter'], freq='Q').to_timestamp()

quarter = []

mean_total_cases_per_million = []
mean_new_cases_per_million = []
var_new_cases = []

mean_total_deaths_per_million = []
mean_new_deaths_per_million = []
var_new_deaths = []

mean_reproduction_rate = []
var_reproduction_rate_moy = []
reproduction_rate_moy_pond = []
var_reproduction_rate_moy_pond = []

mean_stringency_index = []
var_stringency_index_moy = []
stringency_index_moy_pond = []
var_stringency_index_moy_pond = []

for q in bd_covid_eur.Quarter.unique() :

    covid_q = bd_covid_eur.loc[bd_covid_eur.Quarter == q]
    if covid_q['location'].unique().shape[0] == len(_euro_area_19) :
        
        quarter.append(q)
        
        mean_total_cases_per_million.append(covid_q.total_cases_per_million.values.mean())
        mean_new_cases_per_million.append(covid_q.new_cases_per_million.values.mean())
        
        mean_total_deaths_per_million.append(covid_q.total_deaths_per_million.values.mean())
        mean_new_deaths_per_million.append(covid_q.new_deaths_per_million.values.mean())
        
        mean_reproduction_rate.append(covid_q.reproduction_rate.values.mean())
        
        mean_stringency_index.append(covid_q.stringency_index.values.mean())
        
    else : 

        quarter.append(q)
        
        mean_total_cases_per_million.append(np.nan)
        mean_new_cases_per_million.append(np.nan)
        
        mean_total_deaths_per_million.append(np.nan)
        mean_new_deaths_per_million.append(np.nan)
        
        mean_reproduction_rate.append(np.nan)
        
        mean_stringency_index.append(np.nan)
        
del q, covid_q

data_eur_covid = pd.DataFrame()

data_eur_covid['Quarter'] = quarter

data_eur_covid['total_cases_per_million'] = mean_total_cases_per_million
data_eur_covid['new_cases_per_million'] = mean_new_cases_per_million

var_new_cases.append(np.nan)
for i in range (1,len(data_eur_covid['new_cases_per_million'])) :
    val0 = data_eur_covid['new_cases_per_million'].values[i-1]
    val1 = data_eur_covid['new_cases_per_million'].values[i]
    var_new_cases.append((val1 - val0)/val0)
del i, val0, val1
data_eur_covid['var_new_cases_per_million'] = var_new_cases

data_eur_covid['total_deaths_per_million'] = mean_total_deaths_per_million
data_eur_covid['new_deaths_per_million'] = mean_new_deaths_per_million

var_new_deaths.append(np.nan)
for i in range (1,len(data_eur_covid['new_deaths_per_million'])) :
    val0 = data_eur_covid['new_deaths_per_million'].values[i-1]
    val1 = data_eur_covid['new_deaths_per_million'].values[i]
    var_new_deaths.append((val1 - val0)/val0)
del i, val0, val1
data_eur_covid['var_new_deaths_per_million'] = var_new_deaths

data_eur_covid['reproduction_rate_moy'] = mean_reproduction_rate

var_reproduction_rate_moy.append(np.nan)
for i in range (1,len(data_eur_covid['reproduction_rate_moy'])) :
    val0 = data_eur_covid['reproduction_rate_moy'].values[i-1]
    val1 = data_eur_covid['reproduction_rate_moy'].values[i]
    var_reproduction_rate_moy.append((val1 - val0)/val0)
del i, val0, val1
data_eur_covid['var_reproduction_rate_moy'] = var_reproduction_rate_moy

data_eur_covid = data_eur_covid.merge(moy_pond_par_population(bd_covid_eur, 'reproduction_rate', 
                                                              'Quarter', 'location', data_eur_population, 'Quarter') , 
                                      on = 'Quarter', how = 'outer')
cols = list(data_eur_covid.columns[:-1])
cols.append('reproduction_rate_moy_pond')
data_eur_covid.columns = cols
del cols

var_reproduction_rate_moy_pond.append(np.nan)
for i in range (1,len(data_eur_covid['reproduction_rate_moy_pond'])) :
    val0 = data_eur_covid['reproduction_rate_moy_pond'].values[i-1]
    val1 = data_eur_covid['reproduction_rate_moy_pond'].values[i]
    var_reproduction_rate_moy_pond.append((val1 - val0)/val0)
del i, val0, val1
data_eur_covid['var_reproduction_rate_moy_pond'] = var_reproduction_rate_moy_pond

data_eur_covid['stringency_index_moy'] = mean_stringency_index

var_stringency_index_moy.append(np.nan)
for i in range (1,len(data_eur_covid['stringency_index_moy'])) :
    val0 = data_eur_covid['stringency_index_moy'].values[i-1]
    val1 = data_eur_covid['stringency_index_moy'].values[i]
    var_stringency_index_moy.append((val1 - val0)/val0)
del i, val0, val1
data_eur_covid['var_STI_moy'] = var_stringency_index_moy

data_eur_covid = data_eur_covid.merge(moy_pond_par_population(bd_covid_eur, 'stringency_index', 
                                                              'Quarter', 'location', data_eur_population, 'Quarter') , 
                                      on = 'Quarter', how = 'outer')
cols = list(data_eur_covid.columns[:-1])
cols.append('stringency_index_moy_pond')
data_eur_covid.columns = cols
del cols

var_stringency_index_moy_pond.append(np.nan)
for i in range (1,len(data_eur_covid['stringency_index_moy_pond'])) :
    val0 = data_eur_covid['stringency_index_moy_pond'].values[i-1]
    val1 = data_eur_covid['stringency_index_moy_pond'].values[i]
    var_stringency_index_moy_pond.append((val1 - val0)/val0)
del i, val0, val1
data_eur_covid['var_STI_moy_pond'] = var_stringency_index_moy_pond


del covid_Europe, bd_covid_eur
del quarter
del mean_total_cases_per_million, mean_new_cases_per_million
del mean_total_deaths_per_million, mean_new_deaths_per_million
del var_new_cases, var_new_deaths
del mean_reproduction_rate, var_reproduction_rate_moy
del reproduction_rate_moy_pond, var_reproduction_rate_moy_pond
del mean_stringency_index, var_stringency_index_moy
del stringency_index_moy_pond, var_stringency_index_moy_pond


#%%         Donnees relatives a la sante economique d'un pays 

# PIB 

gdp_Europe = pd.read_csv(_chemin_europe+'Europe_GDP.csv.gz', compression='gzip', sep = ',')

bd_gdp_eur = gdp_Europe.loc[gdp_Europe.geo == 'EA19'].reset_index(drop = True)
bd_gdp_eur['Quarter'] = pd.PeriodIndex(bd_gdp_eur.TIME_PERIOD, freq='Q').to_timestamp()

bd_gdp_eur = bd_gdp_eur.drop(columns = ['DATAFLOW', 'LAST UPDATE', 'freq', 'unit', 's_adj', 'na_item', 'geo','TIME_PERIOD', 'OBS_FLAG'])
bd_gdp_eur.columns = ['GDP', 'Quarter']

bd_gdp_eur = bd_gdp_eur.loc[pd.Timestamp('2018-01-01') <= bd_gdp_eur.Quarter].reset_index(drop = True)

del gdp_Europe

# ----------------------------------------------------------------------------------------------------------------

# Chomage 

chomage_Europe = pd.read_csv(_chemin_europe+'Europe_Chomage.csv.gz', compression='gzip', sep = ',')

bd_chomage_eur = chomage_Europe.loc[chomage_Europe.geo == 'EA19'].reset_index(drop = True)
bd_chomage_eur = bd_chomage_eur.loc[bd_chomage_eur.unit == 'PC_POP'].reset_index(drop = True)
bd_chomage_eur['Quarter'] = pd.PeriodIndex(bd_chomage_eur.TIME_PERIOD, freq='Q').to_timestamp()

bd_chomage_eur = bd_chomage_eur.drop(columns = ['DATAFLOW', 'LAST UPDATE', 'freq', 's_adj', 'age', 'unit', 'sex', 'geo', 'TIME_PERIOD', 'OBS_FLAG'])
bd_chomage_eur.columns = ['Chomage', 'Quarter']

bd_chomage_eur = bd_chomage_eur.loc[pd.Timestamp('2018-01-01') <= bd_chomage_eur.Quarter].reset_index(drop = True)

del chomage_Europe

# ----------------------------------------------------------------------------------------------------------------

# Variations du taux de chomage

bd_var_chom = pd.DataFrame(columns = ['Quarter', 'var_chomage'])
var_chom_quart = [bd_chomage_eur.Quarter.values[0]]
var_chom_val = [np.nan]

for i in range (1,len(bd_chomage_eur.Chomage)) :
    val0 = bd_chomage_eur.Chomage.values[i-1]
    val1 = bd_chomage_eur.Chomage.values[i]
    var_chom_val.append((val1 - val0)/val0)
    var_chom_quart.append(bd_chomage_eur.Quarter.values[i])
    
bd_var_chom.Quarter = var_chom_quart
bd_var_chom.var_chomage = var_chom_val

del var_chom_quart, var_chom_val, i, val0, val1

# ----------------------------------------------------------------------------------------------------------------

# Revenus par foyers 

revenus_foyers_Europe = pd.read_csv(_chemin_europe+'Europe_Revenus_foyers.csv.gz', compression='gzip', sep = ',')

bd_revenus_foyers_eur = revenus_foyers_Europe.loc[revenus_foyers_Europe.geo == 'EA19'] .reset_index(drop = True)
bd_revenus_foyers_eur['Quarter'] = pd.PeriodIndex(bd_revenus_foyers_eur.TIME_PERIOD, freq='Q').to_timestamp()

bd_revenus_foyers_eur = bd_revenus_foyers_eur.drop(columns = ['DATAFLOW', 'LAST UPDATE', 'freq', 'unit', 's_adj', 'na_item', 'sector', 'geo', 'TIME_PERIOD', 'OBS_FLAG'])
bd_revenus_foyers_eur.columns = ['Revenus', 'Quarter']

bd_revenus_foyers_eur = bd_revenus_foyers_eur.loc[pd.Timestamp('2018-01-01') <= bd_revenus_foyers_eur.Quarter].reset_index(drop = True)

del revenus_foyers_Europe

# ----------------------------------------------------------------------------------------------------------------

# Inflation 

inflation_Europe = pd.read_csv(_chemin_europe+'Europe_inflation.csv.gz', compression='gzip', sep = ',')

# ----------------------------------------------------------------------------------------------------------------

# HDI

hdi_Europe = pd.read_csv(_chemin_europe+'Europe_human-development-index.csv')

bd_hdi_eur2 = hdi_Europe.loc[hdi_Europe.Entity.isin(_euro_area_19)].reset_index(drop = True)
bd_hdi_eur2['Year'] = pd.to_datetime(bd_hdi_eur2['Year'], format = "%Y")
bd_hdi_eur = bd_hdi_eur = annuel_to_quart(bd_hdi_eur2, 'Year', 'Human Development Index', 'Entity')
bd_hdi_eur = bd_hdi_eur.loc[pd.Timestamp('2018-01-01') <= bd_hdi_eur.Quarter].reset_index(drop = True)

bd_hdi_eur_moy_pond = moy_pond_par_population(bd_hdi_eur, 'Human Development Index', 
                                              'Quarter', 'Entity', data_eur_population, 'Quarter')
bd_hdi_eur_moy_pond.columns = ['Quarter', 'HDI_moy_pond']

del hdi_Europe, bd_hdi_eur, bd_hdi_eur2

# ----------------------------------------------------------------------------------------------------------------

# Variations de l'indice HDI

bd_var_hdi = pd.DataFrame(columns = ['Quarter', 'var_HDI'])
var_hdi_quart = [bd_hdi_eur_moy_pond.Quarter.values[0]]
var_hdi_val = [np.nan]

for i in range (1,len(bd_hdi_eur_moy_pond.HDI_moy_pond)) :
    val0 = bd_hdi_eur_moy_pond.HDI_moy_pond.values[i-1]
    val1 = bd_hdi_eur_moy_pond.HDI_moy_pond.values[i]
    var_hdi_val.append((val1 - val0)/val0)
    var_hdi_quart.append(bd_hdi_eur_moy_pond.Quarter.values[i])
    
bd_var_hdi.Quarter = var_hdi_quart
bd_var_hdi.var_HDI = var_hdi_val

del var_hdi_quart, var_hdi_val, i, val0, val1

# ----------------------------------------------------------------------------------------------------------------

# Expenditure

expenditure_travels_Europe = pd.read_csv(_chemin_europe+'Europe_expenditure_travels.csv.gz', compression='gzip', sep = ',')

bd_expenditure_travels_eur2 = expenditure_travels_Europe.loc[expenditure_travels_Europe.geo == 'EA19'].reset_index(drop = True)
bd_expenditure_travels_eur2['TIME_PERIOD'] = pd.to_datetime(bd_expenditure_travels_eur2['TIME_PERIOD'], format = "%Y")

bd_expenditure_travels_eur2 = bd_expenditure_travels_eur2.drop(columns = ['DATAFLOW', 'LAST UPDATE', 'freq', 'purpose', 'duration', 'c_dest', 'expend', 'statinfo', 'unit', 'geo', 'OBS_FLAG'])
bd_expenditure_travels_eur2.columns = ['TIME_PERIOD', 'Expenditure_travels']

bd_expenditure_travels_eur = annuel_to_quart(bd_expenditure_travels_eur2, 'TIME_PERIOD', 'Expenditure_travels')

bd_expenditure_travels_eur = bd_expenditure_travels_eur.loc[pd.Timestamp('2018-01-01') <= bd_expenditure_travels_eur.Quarter].reset_index(drop = True)

del expenditure_travels_Europe, bd_expenditure_travels_eur2

# ----------------------------------------------------------------------------------------------------------------

# Variations de l'expenditure

bd_var_expenditure_travels = pd.DataFrame(columns = ['Quarter', 'var_expenditure_travels'])
var_expenditure_travels_quart = [bd_expenditure_travels_eur.Quarter.values[0]]
var_expenditure_travels_val = [np.nan]

for i in range (1,len(bd_expenditure_travels_eur.Expenditure_travels)) :
    val0 = bd_expenditure_travels_eur.Expenditure_travels.values[i-1]
    val1 = bd_expenditure_travels_eur.Expenditure_travels.values[i]
    var_expenditure_travels_val.append((val1 - val0)/val0)
    var_expenditure_travels_quart.append(bd_expenditure_travels_eur.Quarter.values[i])
    
bd_var_expenditure_travels.Quarter = var_expenditure_travels_quart
bd_var_expenditure_travels.var_expenditure_travels = var_expenditure_travels_val

del var_expenditure_travels_quart, var_expenditure_travels_val, i, val0, val1

# ----------------------------------------------------------------------------------------------------------------

# Data frame

data_eur_eco = bd_gdp_eur[['Quarter', 'GDP']].merge(bd_chomage_eur, on = 'Quarter', how = 'outer')
data_eur_eco = data_eur_eco.merge(bd_var_chom, on='Quarter', how='outer')
data_eur_eco = data_eur_eco.merge(bd_revenus_foyers_eur, on='Quarter', how='outer')
data_eur_eco = data_eur_eco.merge(bd_expenditure_travels_eur, on='Quarter', how='outer')
data_eur_eco = data_eur_eco.merge(bd_var_expenditure_travels, on='Quarter', how='outer')
data_eur_eco = data_eur_eco.merge(bd_hdi_eur_moy_pond, on = 'Quarter', how = 'outer')
data_eur_eco = data_eur_eco.merge(bd_var_hdi, on='Quarter', how='outer')

# ----------------------------------------------------------------------------------------------------------------

del bd_gdp_eur, bd_chomage_eur, bd_var_chom, bd_revenus_foyers_eur, bd_expenditure_travels_eur
del bd_var_expenditure_travels, bd_hdi_eur_moy_pond, bd_var_hdi


#%%     VISUALISATION


#%%         Les donnees 

data_eur = data_eur_eco.merge(data_eur_covid, on='Quarter', how='inner')

print ('Premieres lignes de la base de donnees : ')
print (data_eur.head(10))

print ()

stats_data_eur = data_eur.describe()
print ('Etude statistique des donnees : ')
print (stats_data_eur)

print ()

cov_data_eur = data_eur.cov()
print ('Matrice de Variance/Covariance : ')
print (cov_data_eur)

print ()

corr_data_eur = data_eur.corr()
print ('Matrice de Correlations : ')
print (corr_data_eur)


#%%         Effets de la COVID sur le PIB

# order = data_eur.corr()['GDP'].abs().sort_values(ascending = False)
# correl_sorted_GDP = data_eur.corr()['GDP'][order.index]

# print ('    Correlations avec GDP : ')
# print (correl_sorted_GDP[1:7])

# fig_europe_data = px.line(data_eur, x='Quarter', y=order.index[:7])

# fig_europe_data.update_layout(
#     title='Intensité de confinement et PIB en fonction du nombre de nouveaux cas',
#     xaxis_title="Nombre de nouveaux cas par million"
# )

# fig_europe_data.show()


#%%         Graphiques
















