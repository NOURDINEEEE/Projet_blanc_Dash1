#!/usr/bin/env python
# coding: utf-8

# In[1]:


from math import *
import pandas as pd
import numpy as np


# In[2]:


Taux_de_croissance_Amerique_du_nord = pd.read_csv('../Data/Donnee_monde/GDP_growth_Amerique_du_nord/API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_5179002.csv', sep=',', skiprows=4)
#Taux_de_croissance_Amerique_du_nord


# In[3]:


Taux_de_croissance_Afrique_sub_sahara = pd.read_csv('../Data/Donnee_monde/GDP_growth_Sub_sahara/API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_5179002.csv', sep=',', skiprows=4)
Taux_de_croissance_Asie_Est = pd.read_csv('../Data/Donnee_monde/GDP_growth_Asia_Est/API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_5179002.csv', sep=',', skiprows=4)
Taux_de_croissance_Asie_Sud = pd.read_csv('../Data/Donnee_monde/GDP_growth_Asia_South/API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_5179002.csv', sep=',', skiprows=4)
Taux_de_croissance_Moyen_orient_Afrique_Nord = pd.read_csv('../Data/Donnee_monde/GDP_growth_Moyen_orient_afrique_du_nord\API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_5179002.csv', sep=',', skiprows=4)
Taux_de_chomage_Asie_Sud = pd.read_csv('../Data/Donnee_monde/Taux_de_chomage_Asie_du_sud/API_SL.UEM.TOTL.ZS_DS2_en_csv_v2_5180900.csv', sep=',', skiprows=4)
Taux_de_chomage_Amerique_du_nord = pd.read_csv('../Data/Donnee_monde/Taux_de_chomage_Amerique_du_nord/API_SL.UEM.TOTL.ZS_DS2_en_csv_v2_5180900.csv', sep=',', skiprows=4)
Taux_de_chomage_Amerique_du_sud = pd.read_csv('../Data/Donnee_monde/Taux_de_chomage_Amerique_du_sud/API_SL.UEM.TOTL.ZS_DS2_en_csv_v2_5180900.csv', sep=',', skiprows=4)
IDE_Amerique_du_nord = pd.read_csv('../Data/Donnee_monde/IDE_Amerique_du_nord/API_BX.KLT.DINV.WD.GD.ZS_DS2_en_csv_v2_5179098.csv', sep=',', skiprows=4)
IDE_sub_sahara = pd.read_csv('../Data/Donnee_monde/IDE_sub_sahara/API_BX.KLT.DINV.WD.GD.ZS_DS2_en_csv_v2_5179098.csv', sep=',', skiprows=4)
Inflation_Amerique_du_nord = pd.read_csv('../Data/Donnee_monde/Inflation_Amerique_du_nord/API_FP.CPI.TOTL.ZG_DS2_en_csv_v2_5180386.csv', sep=',', skiprows=4)


# In[4]:


Stringency_Index = pd.read_csv('../Data/Donnee_monde/owid_covid_data.csv', sep=',')


# In[5]:


#Stringency_Index["continent"].unique()


# In[6]:


X = Stringency_Index["location"] == "Asia"
#X.value_counts(dropna=False)


# In[7]:


#list(Stringency_Index)


# In[8]:


Stringency_Index.groupby([Stringency_Index['location'] == 'Afghanistan'])['stringency_index'].unique()[True][:100]
#print(Stringency_Index.groupby([Stringency_Index['location'] == 'Afghanistan'])['stringency_index'].unique()[True][:100]
#)


# In[9]:


#print(Stringency_Index.groupby([Stringency_Index['location'] == 'France'])['new_cases'].unique()[True][:100])
Stringency_Index.groupby([Stringency_Index['location'] == 'France'])['new_cases'].unique()[True][:100].dtype


# In[10]:


#print(Stringency_Index.groupby([Stringency_Index['location'] == 'France'])['hosp_patients'].unique()[True][:100])


# In[11]:


#print(Stringency_Index.groupby([Stringency_Index['location'] == 'France'])['new_people_vaccinated_smoothed_per_hundred'].unique()[True][:100])


# In[12]:


#Stringency_Index[['stringency_index', 'new_cases', 'hosp_patients']], type(Stringency_Index[['stringency_index', 'new_cases', 'hosp_patients']])


# In[13]:


#Stringency_Index


# In[14]:


#Stringency_Index.groupby(['location'])['stringency_index'].mean().unique()


# In[15]:


#type(Stringency_Index[['stringency_index']])
#Stringency_Index['stringency_index'].unique()


# In[16]:


#Taux_de_croissance_Afrique_sub_sahara['Country Name'].describe()


# In[17]:


#Taux_de_croissance_Afrique_sub_sahara['Country Name'].value_counts(dropna=False)


# In[18]:


#Taux_de_croissance_Afrique_sub_sahara['2019'].describe(percentiles=[0.1, 0.9])


# In[19]:


#Taux de croissance
#list(Taux_de_croissance_Amerique_du_nord)
#Taux_de_croissance_Amerique_du_nord[['Country Name', '1961', '1970', '1980', '1990', '2000', '2005', '2010', '2015', '2018', '2019', '2020', '2021']]


# In[20]:


#Taux_de_croissance_Amerique_du_nord.groupby([Taux_de_croissance_Amerique_du_nord['Country Name'] == 'North America'])[['1961', '1970', '1980', '1990', '2000', '2005', '2010', '2015', '2018', '2019', '2020', '2021']].mean()


# In[21]:


#print(Taux_de_croissance_Afrique_sub_sahara.groupby([Taux_de_croissance_Afrique_sub_sahara['Country Name'] == 'South Africa'])[['1961', '1970', '1980', '1990', '2000', '2005', '2010', '2015', '2018', '2019', '2020', '2021']].mean())


# In[22]:


#print(Taux_de_croissance_Asie_Est.groupby([Taux_de_croissance_Asie_Est['Country Name'] == 'Japon'])[['1961', '1970', '1980', '1990', '2000', '2005', '2010', '2015', '2018', '2019', '2020', '2021']].mean())


# In[23]:


#print(Taux_de_croissance_Asie_Sud.groupby([Taux_de_croissance_Asie_Sud['Country Name'] == 'Indonesia'])[['1961', '1970', '1980', '1990', '2000', '2005', '2010', '2015', '2018', '2019', '2020', '2021']].mean())


# In[24]:


condition = Taux_de_croissance_Moyen_orient_Afrique_Nord['Country Name'] == 'Tunisia'
data1 = Taux_de_croissance_Moyen_orient_Afrique_Nord.groupby(
    [condition])[['1961', '1970', '1980', '1990', '2000', '2005', '2010', '2015', '2018', '2019', '2020', '2021']].mean()

#print(data1)


# In[25]:


#Taux_de_croissance_Moyen_orient_Afrique_Nord[['1961', '1970', '1980', '1990', '2000', '2005', '2010', '2015', '2018', '2019', '2020', '2021']]


# In[26]:


Var1 = Stringency_Index.groupby(Stringency_Index['location'])['stringency_index'].mean().dropna()
#print(Var1), type(Var1)


# In[27]:


data2 = pd.DataFrame(data=Var1, columns=['STI'], index=[Stringency_Index['location'].unique()[:181]])

#data2["years"] = ['1961', '1970', '1980', '1990', '2000', '2005', '2010', '2015', '2018', '2019', '2020', '2021']
#print(data2)
#data_court = data2.index.shape("Africa", "Asia", "North America", "Europe", "Oceania", "South America").dropna()
#print(data_court)


# In[28]:


import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns


# In[29]:


D1 = Taux_de_croissance_Amerique_du_nord[['Country Name', 'Country Code', '1961', '1970', '1980', '1990', '2000', '2005', '2010', '2015', '2018', '2019', '2020', '2021']]
D2 = Taux_de_croissance_Afrique_sub_sahara[['Country Name', 'Country Code', '1961', '1970', '1980', '1990', '2000', '2005', '2010', '2015', '2018', '2019', '2020', '2021']]
D3 = Taux_de_croissance_Asie_Est[['Country Name', 'Country Code', '1961', '1970', '1980', '1990', '2000', '2005', '2010', '2015', '2018', '2019', '2020', '2021']]
D4 = Taux_de_croissance_Asie_Sud[['Country Name', 'Country Code', '1961', '1970', '1980', '1990', '2000', '2005', '2010', '2015', '2018', '2019', '2020', '2021']]
D5 = Taux_de_chomage_Amerique_du_nord[['Country Name', 'Country Code', '1961', '1970', '1980', '1990', '2000', '2005', '2010', '2015', '2018', '2019', '2020', '2021']]
D6 = Taux_de_croissance_Moyen_orient_Afrique_Nord[['Country Name', 'Country Code', '1961', '1970', '1980', '1990', '2000', '2005', '2010', '2015', '2018', '2019', '2020', '2021']]
D7 = Taux_de_chomage_Amerique_du_sud[['Country Name', 'Country Code', '1961', '1970', '1980', '1990', '2000', '2005', '2010', '2015', '2018', '2019', '2020', '2021']]
D8 = IDE_Amerique_du_nord[['Country Name', 'Country Code', '1961', '1970', '1980', '1990', '2000', '2005', '2010', '2015', '2018', '2019', '2020', '2021']]
D9 = IDE_sub_sahara[['Country Name', 'Country Code', '1961', '1970', '1980', '1990', '2000', '2005', '2010', '2015', '2018', '2019', '2020', '2021']]
D10 = Inflation_Amerique_du_nord[['Country Name', 'Country Code', '1961', '1970', '1980', '1990', '2000', '2005', '2010', '2015', '2018', '2019', '2020', '2021']]

Data_Merged1 = D1.merge(Stringency_Index[['stringency_index', 'population', 'iso_code']], how = 'left', left_on= 'Country Code', right_on = 'iso_code')
Data_Merged2 = D2.merge(Stringency_Index[['stringency_index', 'population', 'iso_code']], how = 'left', left_on= 'Country Code', right_on = 'iso_code')
Data_Merged3 = D3.merge(Stringency_Index[['stringency_index', 'population', 'iso_code']], how = 'left', left_on= 'Country Code', right_on = 'iso_code')
Data_Merged4 = D4.merge(Stringency_Index[['stringency_index', 'population', 'iso_code']], how = 'left', left_on= 'Country Code', right_on = 'iso_code')
Data_Merged5 = D5.merge(Stringency_Index[['stringency_index', 'population', 'iso_code']], how = 'left', left_on= 'Country Code', right_on = 'iso_code')
Data_Merged6 = D6.merge(Stringency_Index[['stringency_index', 'population', 'iso_code']], how = 'left', left_on= 'Country Code', right_on = 'iso_code')
Data_Merged7 = D7.merge(Stringency_Index[['stringency_index', 'population', 'iso_code']], how = 'left', left_on= 'Country Code', right_on = 'iso_code')
Data_Merged8 = D8.merge(Stringency_Index[['stringency_index', 'population', 'iso_code']], how = 'left', left_on= 'Country Code', right_on = 'iso_code')
Data_Merged9 = D9.merge(Stringency_Index[['stringency_index', 'population', 'iso_code']], how = 'left', left_on= 'Country Code', right_on = 'iso_code')
Data_Merged10 = D10.merge(Stringency_Index[['stringency_index', 'population', 'iso_code']], how = 'left', left_on= 'Country Code', right_on = 'iso_code')

TableauG = Data_Merged1.groupby([Data_Merged1['Country Name']])[['1961', '1970', '1980', '1990', '2000', '2005', '2010', '2015', '2018', '2019', '2020', '2021']].median().dropna()
Data_Merged2.groupby([Data_Merged2['Country Name']])[['1961', '1970', '1980', '1990', '2000', '2005', '2010', '2015', '2018', '2019', '2020', '2021']].median().dropna()







# In[30]:


#print(list(D1['Country Name']))


# In[46]:


Tableau_croise_AN_TC = Data_Merged1.groupby([Data_Merged1['Country Name'] == 'North America'])[['1961', '1970', '1980', '1990', '2000', '2005', '2010', '2015', '2018', '2019', '2020', '2021']].mean()
Tableau_croise_ASS_TC = Data_Merged2.groupby([Data_Merged2['Country Name'] == 'Sub-Saharan Africa'])[['1961', '1970', '1980', '1990', '2000', '2005', '2010', '2015', '2018', '2019', '2020', '2021']].mean()
Tableau_croise_AEP_TC = Data_Merged3.groupby([Data_Merged3['Country Name'] == 'East Asia & Pacific'])[['1961', '1970', '1980', '1990', '2000', '2005', '2010', '2015', '2018', '2019', '2020', '2021']].mean()
Tableau_croise_AS_TC = Data_Merged4.groupby([Data_Merged4['Country Name'] == 'South Asia'])[['1961', '1970', '1980', '1990', '2000', '2005', '2010', '2015', '2018', '2019', '2020', '2021']].mean()
Tableau_croise_MO_AN_TC = Data_Merged6.groupby([Data_Merged6['Country Name'] == 'Middle East & North Africa'])[['1961', '1970', '1980', '1990', '2000', '2005', '2010', '2015', '2018', '2019', '2020', '2021']].mean()
Tableau_croise_AN_Tch = Data_Merged5.groupby([Data_Merged5['Country Name'] == 'North America'])[['1961', '1970', '1980', '1990', '2000', '2005', '2010', '2015', '2018', '2019', '2020', '2021']].mean()
Tableau_croise_LAC_Tch = Data_Merged7.groupby([Data_Merged7['Country Name'] == 'Latin America & the Caribbean (IDA & IBRD countries)'])[['1961', '1970', '1980', '1990', '2000', '2005', '2010', '2015', '2018', '2019', '2020', '2021']].mean()
Tableau_croise_AN_IDE = Data_Merged8.groupby([Data_Merged8['Country Name'] == 'North America'])[['1961', '1970', '1980', '1990', '2000', '2005', '2010', '2015', '2018', '2019', '2020', '2021']].mean()
Tableau_croise_ASS_IDE = Data_Merged9.groupby([Data_Merged9['Country Name'] == 'Sub-Saharan Africa'])[['1961', '1970', '1980', '1990', '2000', '2005', '2010', '2015', '2018', '2019', '2020', '2021']].mean()
Tableau_croise_AN_Inf = Data_Merged10.groupby([Data_Merged10['Country Name'] == 'North America'])[['1961', '1970', '1980', '1990', '2000', '2005', '2010', '2015', '2018', '2019', '2020', '2021']].mean()

#print(Tableau_croise_AN_TC, type(Tableau_croise_AN_TC))


# In[32]:


Tableau_croise_AN_STI = Data_Merged1.groupby([Data_Merged1['Country Name'] == 'Canada'])[['stringency_index']].mean()
Tableau_croise_ASS_STI = Data_Merged2.groupby([Data_Merged2['Country Name'] == 'Zambia'])[['stringency_index']].mean()
Tableau_croise_AEP_STI = Data_Merged3.groupby([Data_Merged3['Country Name'] == 'China'])[['stringency_index']].mean()
Tableau_croise_AS_STI = Data_Merged4.groupby([Data_Merged4['Country Name'] == 'Indonesia'])[['stringency_index']].mean()
Tableau_croise_MO_AN_STI = Data_Merged6.groupby([Data_Merged6['Country Name'] == 'Tunisia'])[['stringency_index']].mean()
Tableau_croise_LAC_STI = Data_Merged7.groupby([Data_Merged7['Country Name'] == 'Mexico'])[['stringency_index']].mean()


# In[33]:


Tableau_croise_AN_STI = Data_Merged1.groupby([Data_Merged1['Country Name']])[['stringency_index']].mean().dropna()
#print(Tableau_croise_AN_STI.index[:179])
#print(Tableau_croise_AN_STI)
#Tableau_croise_AN_STI.describe(percentiles=[0.1,0.9])


# In[34]:


Var2 = D1.groupby(['Country Name'])[['1961', '1970', '1980', '1990', '2000', '2005', '2010', '2015', '2018', '2019', '2020', '2021']].mean()
#print(Var2), type(Var2)


# In[117]:


import matplotlib.pyplot as plt
import pandas as pd
import seaborn
import plotly.express as px

seaborn.set_context('talk')

a = TableauG.index.to_list()
vector = np.array(a)
#print(vector)

b = Tableau_croise_AN_TC[['1961', '1970', '1980', '1990', '2000', '2005', '2010', '2015', '2018', '2019', '2020', '2021']]
vector2 = np.array(b)
#print(vector2)


#plt.figure(figsize=(50,20))
#sns.barplot(data=data2.sort_values("STI"), x=vector.flatten(), y="STI", hue="STI", width=0.8)
#Figure1

import numpy as np
fig = plt.figure(figsize=(50,20))
Figure_STI1 = sns.barplot(Tableau_croise_AN_TC)
plt.xticks(rotation=45)
plt.ylabel("Taux croissance Amerique su Nord")
plt.xlabel("Annee")
plt.ticklabel_format(style='plain', axis='y')
#Figure_STI1


Tableau_croise_AN_TC = Data_Merged3.groupby([Data_Merged3['Country Name'] == 'East Asia & Pacific'])[['1961', '1970', '1980', '1990', '2000', '2005', '2010', '2015', '2018', '2019', '2020', '2021']].median()


fig = plt.figure(figsize=(50,20))
Figure_STI3 = sns.barplot(Tableau_croise_AEP_TC)
plt.xticks(rotation=45)
plt.ylabel("Taux croissance Asie de L'est")
plt.xlabel("Annee")
plt.ticklabel_format(style='plain', axis='y')
#Figure_STI3


#Taux de croissance Sud de l'Asie périodique




# In[116]:


#Taux de Croissance Sud de l'Asie

""" Figure_STI4 = sns.barplot(Tableau_croise_AS_TC)
plt.xticks(rotation=45)
plt.ylabel("Taux croissance Sud de l'Asie")
plt.xlabel("Annee")
plt.ticklabel_format(style='plain', axis='y') """
#Figure_STI4


# In[119]:


#Taux de croissance Afrique subsahara périodique
import numpy as np
""" Figure_STI2 = sns.barplot(Tableau_croise_ASS_TC)
plt.xticks(rotation=45)
plt.ylabel("Taux croissance Afrique Sub Sahara")
plt.xlabel("Annee")
plt.ticklabel_format(style='plain', axis='y') """
#Figure_STI2


# In[114]:


#Taux de Croissance Moyen Orient
Figure_STI45 = sns.barplot(Tableau_croise_MO_AN_TC)
plt.xticks(rotation=45)
plt.ylabel("Taux de croissance Moyen Orient Asie")
plt.xlabel("Annee")
plt.ticklabel_format(style='plain', axis='y')
#Figure_STI45


# In[110]:


#Taux de chomage en amerique du Nord

""" Figure_STI5 = sns.barplot(data=Tableau_croise_AN_Tch)
plt.xticks(rotation=45)
plt.ylabel("Taux de chômage Amerique du Nord")
plt.xlabel("Annee")
plt.ticklabel_format(style='plain', axis='y') """
#Figure_STI5


# In[108]:


""" fig = plt.figure(figsize=(50,20))

Figure_STI51 = sns.stripplot(Tableau_croise_LAC_Tch)
plt.xticks(rotation=45)
plt.ylabel("Taux de chomage Latin America")
plt.xlabel("Annee")
plt.ticklabel_format(style='plain', axis='y') """
#Figure_STI51


# In[111]:


#Taux de chomage en amerique latine
""" Figure_STI51 = sns.barplot(Tableau_croise_LAC_Tch)
plt.xticks(rotation=45)
plt.ylabel("Taux de chomage Latin America")
plt.xlabel("Annee")
plt.ticklabel_format(style='plain', axis='y') """
#Figure_STI51


# In[50]:


Figure_STI54 = sns.barplot(Tableau_croise_AN_IDE)
plt.xticks(rotation=45)
plt.ylabel("IDE North America")
plt.xlabel("Annee")
plt.ticklabel_format(style='plain', axis='y')
#Figure_STI54


# In[55]:


Figure_STI56 = sns.barplot(Tableau_croise_ASS_IDE)
plt.xticks(rotation=45)
plt.ylabel("IDE Afrique Sub Sahara")
plt.xlabel("Annee")
plt.ticklabel_format(style='plain', axis='y')
#Figure_STI56


# In[54]:


Figure_STI54 = sns.barplot(Tableau_croise_AN_IDE)
plt.xticks(rotation=45)
plt.ylabel("IDE North America")
plt.xlabel("Annee")
plt.ticklabel_format(style='plain', axis='y')
#Figure_STI54



# In[51]:


Figure_STI56 = sns.barplot(Tableau_croise_ASS_IDE)
plt.xticks(rotation=45)
plt.ylabel("IDE Afrique Sub Sahara")
plt.xlabel("Annee")
plt.ticklabel_format(style='plain', axis='y')


# In[112]:


Figure_STI567 = sns.barplot(Tableau_croise_AN_Inf)
plt.xticks(rotation=45)
plt.ylabel("Inflation amerique du Nord")
plt.xlabel("Annee")
plt.ticklabel_format(style='plain', axis='y')
#Figure_STI567


# In[ ]:





# In[37]:


#Stringency index pour le Canada(sans les outlyers)
Figure_STI12 = sns.boxplot(Tableau_croise_AN_STI)
plt.xticks(rotation=45)
plt.ylabel("Canada")
plt.xlabel("STI")
plt.ticklabel_format(style='plain', axis='y')
#Figure_STI12


# In[120]:


#STI au Zambia

""" Figure_STI13 = sns.boxplot(Tableau_croise_ASS_STI)
plt.xticks(rotation=45)
plt.ylabel("Zambia")
plt.xlabel("STI")
plt.ticklabel_format(style='plain', axis='y') """
#Figure_STI13


# In[39]:


#STI au Chine
""" Figure_STI14 = sns.boxplot(Tableau_croise_AEP_STI)
plt.xticks(rotation=45)
plt.ylabel("China")
plt.xlabel("STI")
plt.ticklabel_format(style='plain', axis='y') """
#Figure_STI14


# In[40]:


#STI au Indonésie


#Figure_STI15 = sns.boxplot(Tableau_croise_AS_STI)
#plt.xticks(rotation=45)
#plt.ylabel("Indonesia")
#plt.xlabel("STI")
#plt.ticklabel_format(style='plain', axis='y')
#Figure_STI15


# In[41]:


#STI au Tunisie

""" Figure_STI15 = sns.boxplot(Tableau_croise_MO_AN_STI)
plt.xticks(rotation=45)
plt.ylabel("Tunisia")
plt.xlabel("STI")
plt.ticklabel_format(style='plain', axis='y') """
#Figure_STI15


# In[42]:


#STI au Mexique
""" Figure_STI15 = sns.boxplot(Tableau_croise_LAC_STI)
plt.xticks(rotation=45)
plt.ylabel("Mexico")
plt.xlabel("STI")
plt.ticklabel_format(style='plain', axis='y') """
#Figure_STI15


# In[43]:


#Tableau_croise_AN_Inf


# In[44]:


b = Tableau_croise_AN_TC[['1961', '1970', '1980', '1990', '2000', '2005', '2010', '2015', '2018', '2019', '2020', '2021']][:2]
#np.array(b)


# In[ ]:

#plt.savefig(Figure_STI51)
#plt.savefig(Figure_STI15)
#plt.savefig(Figure_STI13)
#plt.savefig(Figure_STI14)



Figure_STI51 = px.strip(Tableau_croise_LAC_Tch) # Taux de chômage en Amérique Latine
Figure_STI51.update_layout(
    title='Taux de chômage en Amérique Latine',
    xaxis_title="Année",
    yaxis_title="Taux de chomage Latin America"
)

Figure_STI15 = px.box(Tableau_croise_LAC_STI) # STI au Mexique
Figure_STI15.update_layout(
    title='STI au Mexique',
    yaxis_title="STI",
    xaxis_title="Mexique"
)

#canada ??
Figure_STI5 = px.bar(Tableau_croise_AN_IDE.T[True]) # Taux de chômage en Amérique du Nord
Figure_STI5.update_layout(
    title='Taux de chômage en Amérique du Nord',
    xaxis_title="Année",
    yaxis_title="IDE North America"
)

Figure_STI2 = px.bar(Tableau_croise_ASS_TC.T[True]) # Taux de croissance Sub Sahara
Figure_STI2.update_layout(
    title='Taux de croissance Sub Sahara',
    xaxis_title="Année",
    yaxis_title="Taux de croissance"
)

Figure_STI4 = px.bar(Tableau_croise_AS_TC.T[True]) # Taux de croissance sud de l'Asie
Figure_STI4.update_layout(
    title='Taux de croissance sud de l\'Asie',
    xaxis_title="Année",
    yaxis_title="Taux de croissance"
)

Figure_STI11 = px.box(Tableau_croise_AS_STI) # STI Indonesia
Figure_STI11.update_layout(
    title='STI Indonesia',
    yaxis_title="STI",
    xaxis_title="Indonesia"
)

Figure_STI13 = px.box(Tableau_croise_ASS_STI) # STI Zambia
Figure_STI13.update_layout(
    title='STI Zambia',
    yaxis_title="STI",
    xaxis_title="Zambia"
)

Figure_STI14 = px.box(Tableau_croise_AEP_STI) # STI China
Figure_STI14.update_layout(
    title='STI China',
    yaxis_title="STI",
    xaxis_title="China"
)

Figure_STI12 = px.box(Tableau_croise_MO_AN_STI) # STI Tunisia 
Figure_STI12.update_layout(
    title='STI Tunisia',
    yaxis_title="STI",
    xaxis_title="Tunisia"
)