# data_loader.py

import streamlit as st
import pandas as pd

class DataLoader:
    @staticmethod
    @st.cache_data
    def load_data():
        year_on_year = pd.read_excel('1900_2021_DISASTERS.xlsx.xls', sheet_name='Year on Year comparison')
        type_subtype = pd.read_excel('1900_2021_DISASTERS.xlsx.xls', sheet_name='1900_2021_DISASTERS.xlsx - emda')
        type_subtype = type_subtype[['Year','Disaster Subgroup','Disaster Subtype','Event Name']]
        earth_quake =  pd.read_excel('1900_2021_DISASTERS.xlsx.xls', sheet_name='1900_2021_DISASTERS.xlsx - emda')
        earth_quake = earth_quake.loc[earth_quake['Disaster Type']=='Earthquake']
        earth_quake = earth_quake[['Year','Disaster Subtype','Country','Dis Mag Value','Latitude','Longitude']]
        return year_on_year, type_subtype, earth_quake

    @staticmethod
    @st.cache_data
    def load_country_wise_data():
        country_wise = pd.read_excel('1900_2021_DISASTERS.xlsx.xls', sheet_name='CountryWise')
        country_wise.set_index('Country', inplace=True)
        return country_wise
