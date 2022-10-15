import pandas as pd 
from matplotlib import pyplot as plt 
import seaborn as sns
import pydeck as pdk
import streamlit as st

df = pd.read_csv("listings.csv")

st.set_page_config( # head tag
    page_title="NYC Airbnb Data Demo", 
    page_icon="random",
    layout="centered",
    initial_sidebar_state='auto',
    menu_items={
        'Get Help': 'https://github.com/112523chen/NYC-Airbnb-Data-Visualization-App',
        'Report a bug': "https://github.com/112523chen/NYC-Airbnb-Data-Visualization-App/issues/new",
        'About': """
                ***Streamlit app*** that visualizes New York City Airbnb listing data
                """ #supports markdown
    })

st.title("NYC Airbnb Listing Data") # H1 tag
