#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import seaborn as sn
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

import plotly.graph_objects as go
import plotly.express as px

from dash import dcc
from dash import html
from jupyter_dash import JupyterDash

template='plotly_white'



# In[13]:


data_2 = pd.read_csv('../Data/Data 2/owid-covid-data.csv')
data_3 = pd.read_csv('../Data/Data 3/data_PIB.csv', skiprows=6, header=None)
data_4 = pd.read_csv('../Data/Data 3/CPMNACSCAB1GQFR.csv')
data_5 = pd.read_csv('../Data/Data 3/avia_paoc__custom_92836_page_linear.csv') # Air passenger transport
data_6 = pd.read_csv('../Data/Data 3/apro_mk_colm__custom_89820_page_linear.csv')
data_7 = pd.read_csv('../Data/Data 3/avia_gooc__custom_93212_page_linear.csv')
data_8 = pd.read_csv('../Data/Donnees_Europe/Europe_expenditure_travels.csv.gz')



data_2 = data_2[['location', 'date', 'total_cases', 'total_deaths', 'human_development_index', 'population', 'stringency_index', 'gdp_per_capita', 'extreme_poverty']]
data_2.columns = ['COUNTRY', 'DATE', 'TC', 'TD', 'HDI', 'POP', 'STI', 'GDPCAP', 'POVERTY']
data_2 = data_2[data_2.COUNTRY == 'France']
data_2['DATE'] = pd.to_datetime(data_2['DATE'])
data_2['Quarter'] = data_2['DATE']
data_2['Quarter'] = pd.PeriodIndex(data_2['Quarter'], freq='Q').to_timestamp()
#data_2 = data_2[data_2.Quarter.isin(pd.PeriodIndex(['2020Q1', '2020Q2', '2020Q3', '2020Q4', '2021Q1', '2021Q2',
#       '2021Q3', '2021Q4', '2022Q1', '2022Q2', '2022Q3', '2022Q4'], freq='Q'))]
data_2.drop(['COUNTRY'], axis=1, inplace=True)

data_3.drop([2], axis=1, inplace=True)
data_3 = data_3[data_3[0] >= '2020Q1']
data_3.rename(
    columns={0: "Quarter", 1: "PBI_var"},
    inplace=True,
)
data_3.sort_values(by='Quarter', ascending=True, inplace=True)
data_3['Quarter'] = pd.PeriodIndex(data_3['Quarter'], freq='Q').to_timestamp()

data_4.rename(
    columns={'CPMNACSCAB1GQFR': "GDP"},
    inplace=True,
)
data_4['Quarter'] = pd.PeriodIndex(data_4['DATE'], freq='Q').to_timestamp()

data_5['Quarter'] = pd.PeriodIndex(data_5['TIME_PERIOD'], freq='Q').to_timestamp()
data_5.rename(
    columns={'OBS_VALUE': "APT"}, # Air passengers transport
    inplace=True,
)

data_6['Quarter'] = pd.PeriodIndex(data_6['TIME_PERIOD'], freq='Q').to_timestamp()
data_6.rename(
    columns={'OBS_VALUE': "MILK"}, # Cows'milk collection and products obtained
    inplace=True,
)

data_7['Quarter'] = pd.PeriodIndex(data_7['TIME_PERIOD'], freq='Q').to_timestamp()
data_7.rename(
    columns={'OBS_VALUE': "AFT"}, # Cows'milk collection and products obtained
    inplace=True,
)

data_8['Quarter'] = pd.PeriodIndex(data_8['TIME_PERIOD'], freq='Q').to_timestamp()
data_8.rename(
    columns={'OBS_VALUE': "EXPENDITURE"}, # Cows'milk collection and products obtained
    inplace=True,
)


# In[67]:


""" donnees = [data_2, data_3, data_4, data_5, data_6]
for i, b in enumerate(donnees):
    print(f"base_{i} columns : ", list(b.columns))
    print('####################################################"') """



# In[15]:


data = data_2.merge(data_3, on='Quarter', how='outer')
data = data.merge(data_4, on='Quarter', how='inner')
data = data.merge(data_5, on='Quarter', how='inner')
data = data.merge(data_6, on='Quarter', how='inner')
#data = data.merge(data_7, on='Quarter', how='left')
#data = data.merge(data_8, on='Quarter', how='left')
#data = data.set_index('Quarter').join(data_4.set_index('Quarter'))
data = data.reset_index()
#data.DATE = pd.to_datetime(data.DATE, format='%Y%M%D')
data = data.fillna(0)
#data.head(5)


# In[16]:


data_quarterly = data.groupby('Quarter').agg({
                            'TC' : 'sum',
                            'TD' : 'sum',
                            'POP' : 'sum',
                            'HDI' : 'mean',
                            'STI' : 'mean',
                            'PBI_var' : 'mean',
                            'GDP' : 'mean',
                            'POVERTY' : 'mean',
                            'APT' : 'sum',
                            'MILK' : 'sum',
#                            'AFT' : 'mean',
#                            'EXPENDITURE' : 'mean'
}).reset_index()

data_quarterly['log_GDP'] = np.log(data_quarterly.GDP)

#data_quarterly


# In[18]:


data_quarterly_sorted = data_quarterly.sort_values(by="STI")

fig_1 = px.line(data_quarterly_sorted, x="STI", y="GDP", title='PIB en fonction de l\'intensité de confinement', template=template)
#fig_1.show()


# In[19]:


fig_2 = px.scatter(data_quarterly, x="STI", y="GDP", template=template)
fig_2.update_layout(
    title='PIB en fonction de l\'intensité de confinement',
    xaxis_title="Stringency Index : mesure l'intensité de confinement",
    yaxis_title="PIB"
)
#fig_2.show()


# In[20]:


#data_quarterly["Quarter"].to_timestamp()

fig_3 = px.line(data_quarterly, x="Quarter", y="GDP", title='PBI', template=template)
#fig_3.show()


# In[21]:


fig_4 = px.line(data_quarterly, x="Quarter", y="STI", title='STI', template=template)
#fig_4.show()


# In[22]:


data_quarterly['GDP_normalized'] = (data_quarterly['GDP']-data_quarterly['GDP'].mean())/data_quarterly['GDP'].std()
data_quarterly['STI_normalized'] = (data_quarterly['STI']-data_quarterly['STI'].mean())/data_quarterly['STI'].std()


# In[23]:


data['GDP_normalized'] = (data['GDP']-data['GDP'].mean())/data['GDP'].std()
data['STI_normalized'] = (data['STI']-data['STI'].mean())/data['STI'].std()


# In[24]:


fig_5 = px.line(data_quarterly, x='Quarter' , y=['STI_normalized', 'GDP_normalized'], template=template)
#fig = px.line(data_quarterly, x="Quarter", y="STI", title='STI')
fig_5.update_layout(
    title='Evolution du PIB et de l\'indice d\'intensité de confinement',
    xaxis_title="Date",
    yaxis_title="PIB/STI"
)

series_names = ["Stringency Index", "PIB"]

for idx, name in enumerate(series_names):
    fig_5.data[idx].name = name
    fig_5.data[idx].hovertemplate = name

#fig_5.show()


# In[25]:


data_quarterly['APT_normalized'] = (data_quarterly['APT']-data_quarterly['APT'].mean())/data_quarterly['APT'].std()
data_quarterly['STI_normalized'] = (data_quarterly['STI']-data_quarterly['STI'].mean())/data_quarterly['STI'].std()


# In[26]:


data['APT_normalized'] = (data['APT']-data['APT'].mean())/data['APT'].std()
data['STI_normalized'] = (data['STI']-data['STI'].mean())/data['STI'].std()


# In[27]:


#data.columns


# In[28]:


data['month'] = pd.PeriodIndex(data['DATE_x'], freq='M').to_timestamp()
data_monthly = data[['month', 'STI', 'APT', 'MILK']].groupby('month').agg(sum).reset_index()

data_monthly= data_monthly[data_monthly['STI'] != 0]
data_monthly= data_monthly[data_monthly['APT'] != 0]
data_monthly= data_monthly[data_monthly['MILK'] != 0]


# In[29]:


data_monthly['APT_normalized'] = (data_monthly['APT']-data_monthly['APT'].mean())/data_monthly['APT'].std()
data_monthly['STI_normalized'] = (data_monthly['STI']-data_monthly['STI'].mean())/data_monthly['STI'].std()
data_monthly['MILK_normalized'] = (data_monthly['MILK']-data_monthly['MILK'].mean())/data_monthly['MILK'].std()


# In[31]:


fig_6 = px.line(data_monthly, x='month', y=['STI_normalized', 'APT_normalized'], template=template)

fig_6.update_layout(
    title='Evolution de nombre de vols passagers et de l\'intensité de confinement',
    xaxis_title="Date"
)

series_names = ["Stringency Index normalisé", "Nombre de vols passagers normalisé"]

for idx, name in enumerate(series_names):
    fig_6.data[idx].name = name
    fig_6.data[idx].hovertemplate = name

#fig_6.show()


# In[32]:


fig_7 = px.scatter(data_quarterly, x='TC', y=['STI_normalized', 'GDP_normalized'], template=template)

fig_7.update_layout(
    title='Intensité de confinement et PIB en fonction du nombre total des cas',
    xaxis_title="Nombre total des cas"
)

series_names = ["Stringency Index normalisé", "PIB normalisé"]

for idx, name in enumerate(series_names):
    fig_7.data[idx].name = name
    fig_7.data[idx].hovertemplate = name

#fig_7.show()


# In[33]:


fig_8 = px.scatter(data_quarterly, x='TD', y=['STI_normalized', 'GDP_normalized'], title='', template=template)
#fig_8.show()


# In[34]:


fig_9 = px.scatter(data_quarterly, x='TC', y=['MILK'], title='', template=template)
#fig_9.show()


# In[35]:


#fig_10 = px.scatter(data_quarterly, x='Quarter', y=['AFT'], title='', template=template)
#fig_10.show()


# In[36]:


#fig_10 = px.scatter(data_quarterly, x='Quarter', y=['EXPENDITURE'], title='', template=template)
#fig_10.show()


# In[37]:


#print("data_quarterly columns : ", data_quarterly.columns)
#print("################################")
#print("data_monthly columns : ", data_monthly.columns)


# # Partie WEB :

# In[129]:




# In[141]:


#get_ipython().system('jupyter nbconvert France_Data.ipynb --to python')


# In[ ]:

Commentaire_France_1 = "Le PIB a tendance de diminuer en fonction de l'indice Stringency, ce qui reflète le fait que le \
    PIB a diminué chaque fois la France a passé d'une période de confinement."
Commentaire_France_2 = ""
Commentaire_France_3 = ""
Commentaire_France_4 = ""

Commentaire_EU_1 = ""
Commentaire_EU_2 = ""
Commentaire_EU_3 = ""
Commentaire_EU_4 = ""

Commentaire_Monde_1 = ""
Commentaire_Monde_2 = ""
Commentaire_Monde_3 = ""
Commentaire_Monde_4 = ""