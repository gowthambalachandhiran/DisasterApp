# dashboard_layout.py

import streamlit as st
import altair as alt
import matplotlib.pyplot as plt
import folium
from streamlit_folium import folium_static

class DashboardLayout:
    @staticmethod
    def display_image_and_title(selected_tab, image_path):
        col1, col2 = st.columns([1, 4])
        with col1:
            st.image(image_path, use_column_width=False, width=200, caption=selected_tab)
        with col2:
            if selected_tab == "Disaster Data":
                st.markdown(
    """
    <div style='text-align: right;'>
        <h1 style='font-size: 24px;'>Exploring Decades of Disasters: A Journey from 1901 to 2021</h1>
        <p>Step into the realm of historical catastrophes as we embark on a fascinating exploration spanning over a century, 
        from the dawn of the 20th century to the present day. Our interactive dashboard offers a unique opportunity to delve into the evolution of disasters, comparing their impact, frequency, and patterns across decades.
        Uncover the stories behind each era's calamities, from natural phenomena to human-made crises, and witness how societies have adapted and responded over time. With rich data visualizations and insightful analyses, our platform illuminates the changing landscape of disaster management and resilience, empowering users to glean valuable insights from the past to shape a more prepared future. Join us as we chart the course through history's trials and triumphs, exploring the ebb and flow of disaster through the decades.</p>
    </div>
    """,
    unsafe_allow_html=True
)
            if selected_tab == "Disaster Heatmap":
                st.markdown(
    """
    <div style='text-align: right;'>
        <h2 style='font-size: 20px;'>Global Impact: Mapping Disaster Hotspots Across the Globe</h2>
        <p>Explore the dynamic landscape of disaster occurrences worldwide, from 1901 to 2021. Dive into the interactive heatmap feature, where you can select a specific disaster type and witness its geographical distribution unfold on a global scale. From earthquakes to floods, visualize the intensity and frequency of disasters, empowering better preparedness and response strategies for a safer, more resilient world.</p>
    </div>
    """,
    unsafe_allow_html=True
)



            if selected_tab == "Type of Event":
               st.markdown(
    """
    <div style='text-align: right;'>
        <h1 style='font-size: 24px;'>Disaster Dynamics: Exploring Nature's Varied Arsenal</h1>
        <p>Delve into the intricacies of natural disasters by subgroup – biological, climatological, hydrological, and more. Select your desired timeframe and specific disaster subtype, whether it's a virus outbreak, landslide, or volcanic activity. Witness the frequency and distribution of these events unfold through an interactive bar graph, providing insights into the patterns and trends shaping our environment. Gain a deeper understanding of nature's unpredictable forces and inform proactive measures for resilience and adaptation.</p>
    </div>
    """,
    unsafe_allow_html=True
)


            if selected_tab == "Earthquake":
              st.markdown(
    """
    <div style='text-align: right;'>
        <h1 style='font-size: 24px;'>Unveiling Earth's Tremors: Mapping the Richter Scale</h1>
        <p>Embark on a seismic journey through time with our earthquake exploration tab. Choose your desired time range and set the Richter scale magnitude to witness the Earth's dynamic activity unfold. As you adjust the parameters, a heatmap of the globe materializes, highlighting regions affected by seismic events of varying magnitudes. Gain insights into the distribution and intensity of earthquakes worldwide, empowering you to comprehend and mitigate the impact of these natural phenomena.</p>
    </div>
    """,
    unsafe_allow_html=True
)


    @staticmethod
    def display_disaster_data(selected_categories, filtered_df):
        if len(selected_categories) > 0:
            melted_df = filtered_df.melt(id_vars='Year', var_name='Category', value_name='Count')
            chart = alt.Chart(melted_df).mark_line().encode(
                x='Year:N',
                y='Count:Q',
                color='Category:N'
            ).properties(
                width=600,
                height=400
            )
            st.altair_chart(chart, use_container_width=True)
        else:
            st.write('Select at least one category.')

    @staticmethod
    def display_disaster_heatmap(geo_json_data, filtered_df, selected_disaster):
        m = folium.Map(location=[0, 0], zoom_start=2)
        folium.Choropleth(
            geo_data=geo_json_data,
            name='choropleth',
            data=filtered_df,
            columns=[filtered_df.index, selected_disaster],
            key_on='feature.properties.name',
            fill_color='YlOrRd',
            fill_opacity=0.7,
            line_opacity=0.2,
            legend_name=f'{selected_disaster} Count',
            tooltip=folium.features.GeoJsonTooltip(fields=['name', selected_disaster],
                                                   aliases=['Country', selected_disaster], labels=True)
        ).add_to(m)
        folium.LayerControl().add_to(m)
        folium_static(m)

    @staticmethod
    def display_type_of_event(filtered_data, event_counts, applicable_subtypes):
        if len(event_counts) > 0:
            if len(event_counts) > 10:
                st.info("Only showing top 10 due to too many options.")
                event_counts = event_counts.head(10)
            colors = ['blue', 'green', 'red', 'purple', 'orange', 'yellow', 'brown', 'pink', 'gray', 'cyan']
            plt.figure(figsize=(10, 6))
            event_counts.plot(kind='bar', color=colors[:len(event_counts)])
            plt.title('Event Name Counts')
            plt.xlabel('Event Name')
            plt.ylabel('Count')
            plt.xticks(rotation=90)
            st.pyplot()
            st.subheader('Filtered Data')
            st.write(filtered_data)
        else:
            st.warning("No data available for the selected criteria.")

    @staticmethod
    def display_earthquake_map(filtered_data, disaster_type, dis_mag_value):
        m = folium.Map()
        folium.Choropleth(
            geo_data='world-countries.json',
            name='choropleth',
            data=filtered_data,
            columns=['Country', 'Dis Mag Value'],
            key_on='feature.properties.name',
            fill_color='YlOrRd',
            fill_opacity=0.7,
            line_opacity=0.2,
            legend_name='Disaster Magnitude',
            highlight=True,
            line_weight=2,
            line_color='black',
        ).add_to(m)
        folium.LayerControl().add_to(m)
        folium_static(m)
