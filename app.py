# app.py

import streamlit as st
from data_loader import DataLoader
from disaster_dashboard import disaster_data_tab, disaster_heatmap_tab, type_of_event_tab, earthquake_tab
from dashboard_layout import DashboardLayout

# Set page config to dark theme
st.set_page_config(
    page_title="Disaster Dashboard",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown('<div style="text-align: left"><a href="https://www.linkedin.com/in/gowtham-balachandhiran-47260273/">My LinkedIn Profile</a></div>', unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: black;'>Disaster Analysis App</h1>", unsafe_allow_html=True)

# Load data
year_on_year, type_subtype, earth_quake = DataLoader.load_data()

# Define images for each tab
tab_images = {
    "Disaster Data": "disaster_data_image.jpg",
    "Disaster Heatmap": "disaster_heatmap_image.jpg",
    "Type of Event": "type_of_event_image.jpg",
    "Earthquake": "earthquake_image.jpg"
}

# Get selected tab from user
selected_tab = st.sidebar.selectbox("Select Tab", list(tab_images.keys()), index=0, format_func=lambda x: x)

# Load the image corresponding to the selected tab
image_path = tab_images[selected_tab]

# Display image and title
DashboardLayout.display_image_and_title(selected_tab, image_path)

# Display the content based on the selected tab
if selected_tab == "Disaster Data":
    disaster_data_tab(year_on_year)
elif selected_tab == "Disaster Heatmap":
    disaster_heatmap_tab()
elif selected_tab == "Type of Event":
    type_of_event_tab(type_subtype)
elif selected_tab == "Earthquake":
    earthquake_tab(earth_quake)

# Add "Buy me a coffee" link at the bottom of every page
st.markdown('<a href="https://buymeacoffee.com/gowthambalx" target="_blank">☕ Buy me a coffee if you like what you are seeing</a>', unsafe_allow_html=True)
