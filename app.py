import pandas as pd 
from matplotlib import pyplot as plt 
import seaborn as sns
import pydeck as pdk
import streamlit as st

df = pd.read_csv("listings.csv")

gb = df.groupby(['neighbourhood_group_cleansed','neighbourhood_cleansed'])

st.set_page_config(
    page_title="NYC Airbnb Data Demo", 
    page_icon="🏠",
    layout="center",
    initial_sidebar_state='auto',
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "",
        'About': "# This is a header. This is an *extremely* cool app!"
    })
st.title("NYC Airbnb Listing Data") # H1 tag
