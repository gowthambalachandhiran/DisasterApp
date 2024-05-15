# disaster_dashboard.py

import streamlit as st
import pandas as pd
import folium
import json
import altair as alt
import matplotlib.pyplot as plt
from streamlit_folium import folium_static
from data_loader import DataLoader
from dashboard_layout import DashboardLayout

def disaster_data_tab(year_on_year):
    selected_categories = st.sidebar.multiselect('Select categories', year_on_year.columns[1:])
    filtered_df = year_on_year[selected_categories + ['Year']]
    DashboardLayout.display_disaster_data(selected_categories, filtered_df)

def disaster_heatmap_tab():
    with open('world-countries.json') as f:
        geo_json_data = json.load(f)
    country_wise = DataLoader.load_country_wise_data()
    selected_disaster = st.sidebar.selectbox('Select a disaster type', country_wise.columns)
    filtered_df = country_wise[[selected_disaster]]
    DashboardLayout.display_disaster_heatmap(geo_json_data, filtered_df, selected_disaster)

def type_of_event_tab(type_subtype):
    selected_subgroups = st.multiselect('Disaster Subgroup', type_subtype['Disaster Subgroup'].unique())
    start_year, end_year = st.sidebar.slider('Select a range of years', 1900, 2021, (1900, 2021))
    filtered_data = type_subtype[type_subtype['Disaster Subgroup'].isin(selected_subgroups) & 
                                 (type_subtype['Year'] >= start_year) & (type_subtype['Year'] <= end_year)]
    applicable_subtypes = filtered_data['Disaster Subtype'].unique()
    selected_subtypes = st.multiselect('Disaster Subtype', applicable_subtypes)
    filtered_data = filtered_data[filtered_data['Disaster Subtype'].isin(selected_subtypes)]
    event_counts = filtered_data['Event Name'].value_counts()
    DashboardLayout.display_type_of_event(filtered_data, event_counts, applicable_subtypes)

def earthquake_tab(earth_quake):
    start_year, end_year = st.sidebar.slider('Select a range of years', 1900, 2021, (1900, 2021))
   
    disaster_type = st.sidebar.toggle('Disaster Type: Ground movement', True, 'Ground movement', 'Disable for Tsunami with earthquake')
    dis_mag_value = st.sidebar.slider('Select Dis Mag Value', min_value=0, max_value=10, value=(0, 10))
    filtered_data = earth_quake[(earth_quake['Year'] >= start_year) & (earth_quake['Year'] <= end_year)]
    if disaster_type == 'Ground movement':
        filtered_data = filtered_data[filtered_data['Disaster Subtype'] == 'Ground movement']
    else:
        filtered_data = filtered_data[filtered_data['Disaster Subtype'] == 'Tsunami']
    filtered_data = filtered_data[(filtered_data['Dis Mag Value'] >= dis_mag_value[0]) &
                                  (filtered_data['Dis Mag Value'] <= dis_mag_value[1])]
    DashboardLayout.display_earthquake_map(filtered_data, disaster_type, dis_mag_value)
