#!/usr/bin/env python
# coding: utf-8

# In[2]:


#_____Librairies importées
import requests as rq
from bs4 import BeautifulSoup as bs
import json
import pandas as pd
import numpy as np
import re
import psycopg2
import pandas as pd
from psycopg2.extensions import parse_dsn
from sqlalchemy import create_engine
import seaborn as sns
import os
import folium
import pandas as pd
from folium.plugins import MarkerCluster
import matplotlib.pyplot as plt
"""Module créeant une super carteographie en folium ."""
df = pd.read_csv('df1.csv')
df_visu = pd.DataFrame(df)
display(df)
def create_maps () :
    LAT_GRE = 45.188529
    LONG_GRE = 5.724524
    maps = folium.Map(location=[LAT_GRE, LONG_GRE],zoom_start=12)
    marker_cluster= MarkerCluster()
    for row in df_visu.itertuples():  
        folium.Marker(location=[row.latitude, row.longitude], popup= f'<a href="{row.lien}">{row.intitule_offre}</a>').add_to(marker_cluster)
        marker_cluster.add_to(maps)
        #print(row)
        # Afficher un périmètre de rayon 15km autour du centre de la carte
    folium.Circle(
    radius= 15000,
    location= [LAT_GRE, LONG_GRE],
    color= 'darkblue',
    fill=False,
    ).add_to(maps)
    display(maps)
create_maps()


# In[ ]:




