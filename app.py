import pandas as pd 
import numpy as np
from matplotlib import pyplot as plt 
import seaborn as sns
import streamlit as st

df = pd.read_csv("listings.csv")
df['price'] = df['price'].str.replace('$', '')
df['price'] = df['price'].str.replace(',', '')
df['price'] = pd.to_numeric(df['price'])
borough_values = np.insert(df['neighbourhood_group_cleansed'].unique(),0,values="All")
nyc_average_list_price = df['price'].mean()

#helper functions
def create_map(df,borough,neighborhoods):
    if borough != "All":
        if neighborhoods:
            df = df[df['neighbourhood_cleansed'].isin(neighborhoods)]
            st.map(df)
        else:
            df = df[df['neighbourhood_group_cleansed'] == borough]
            st.map(df)
    else:
        if neighborhoods:
            df = df[df['neighbourhood_cleansed'].isin(neighborhoods)]
            st.map(df)
        else:
            st.map(df)

def create_means(df, borough, neighborhoods):
    st.subheader("Average Price for Listings")
    col1, col2, col3 = st.columns(3)
    if (borough == "All"):
        if neighborhoods:
            col2.metric("New York City", f"${round(nyc_average_list_price,2)}")
            col11, col12, col13 = st.columns(3)
            for idx, neighborhood in enumerate(neighborhoods):
                idx += 1
                if idx % 3 == 1:
                    col11.metric(
                        f"{neighborhood}",
                        f"${round(df[df['neighbourhood_cleansed'] == neighborhood]['price'].mean(),2)}",
                        round(df[df['neighbourhood_cleansed'] == neighborhood]['price'].mean() - nyc_average_list_price, 2 )
                    )
                elif idx % 3 == 2:
                    col12.metric(
                        f"{neighborhood}",
                        f"${round(df[df['neighbourhood_cleansed'] == neighborhood]['price'].mean(),2)}",
                        round(df[df['neighbourhood_cleansed'] == neighborhood]['price'].mean() - nyc_average_list_price, 2 )
                    )
                else:
                    col13.metric(
                        f"{neighborhood}",
                        f"${round(df[df['neighbourhood_cleansed'] == neighborhood]['price'].mean(),2)}",
                        round(df[df['neighbourhood_cleansed'] == neighborhood]['price'].mean() - nyc_average_list_price, 2 )
                    )
        else:
            col2.metric("New York City", f"${round(nyc_average_list_price,2)}")

    elif borough != "All":
        if neighborhoods:
            col11, col12, col13 = st.columns(3)
            for idx, neighborhood in enumerate(neighborhoods):
                idx += 1
                if idx % 3 == 1:
                    col11.metric(
                        f"{neighborhood}",
                        f"${round(df[df['neighbourhood_cleansed'] == neighborhood]['price'].mean(),2)}",
                        round(df[df['neighbourhood_cleansed'] == neighborhood]['price'].mean() - nyc_average_list_price, 2 )
                    )
                elif idx % 3 == 2:
                    col12.metric(
                        f"{neighborhood}",
                        f"${round(df[df['neighbourhood_cleansed'] == neighborhood]['price'].mean(),2)}",
                        round(df[df['neighbourhood_cleansed'] == neighborhood]['price'].mean() - nyc_average_list_price, 2 )
                    )
                else:
                    col13.metric(
                        f"{neighborhood}",
                        f"${round(df[df['neighbourhood_cleansed'] == neighborhood]['price'].mean(),2)}",
                        round(df[df['neighbourhood_cleansed'] == neighborhood]['price'].mean() - nyc_average_list_price, 2 )
                    )
        else:
            col1.metric(
                "New York City", 
                f"${round(nyc_average_list_price,2)}")
            col3.metric(
                label = f"{str.title(borough)}", 
                value = f"${round(df[df['neighbourhood_group_cleansed'] == borough]['price'].mean(),2)}",
                delta = round(df[df['neighbourhood_group_cleansed'] == borough]['price'].mean() - nyc_average_list_price, 2 ))


def create_chart(df,borough, neighborhoods):
    if (borough == "All"):
        if neighborhoods:
            fig, ax = plt.subplots()
            for n in neighborhoods:
                ax.hist(df[df['neighbourhood_cleansed'] == n]['price'], 100, histtype='bar', label=f"{n}")
            ax.set_title(f"Distribution of Airbnb Listings in Certain Neighbourhood")
            ax.set_ylabel('Frequency')
            ax.set_xlabel('Prices')
            ax.legend()
            st.pyplot(
                fig
            )
        else:
            min_value = df['price'].min()
            max_value = df['price'].max()
            fig, ax = plt.subplots(figsize=(10,10))
            for b in list(df['neighbourhood_group_cleansed'].unique()):
                ax.hist(df[df['neighbourhood_group_cleansed'] == b]['price'], 100, range=(min_value,max_value), histtype='bar', label=f"{b}")
            ax.set_title("Distribution of Airbnb Listings in NYC")
            ax.set_ylabel('Frequency')
            ax.set_xlabel('Prices')
            ax.legend()
            st.pyplot(
                fig
            )
    else:
        if neighborhoods:
            fig, ax = plt.subplots()
            for n in neighborhoods:
                ax.hist(df[df['neighbourhood_cleansed'] == n]['price'], 100, histtype='bar', label=f"{n}", alpha=0.2)
            ax.set_title(f"Distribution of Airbnb Listings in Certain Neighbourhood")
            ax.set_ylabel('Frequency')
            ax.set_xlabel('Prices')
            ax.legend()
            st.pyplot(
                fig
            )
        else:
            min_value = df[df["neighbourhood_group_cleansed"] == borough]['price'].min()
            max_value = df[df["neighbourhood_group_cleansed"] == borough]['price'].max()
            # print(min_value,max_value)
            fig, ax = plt.subplots(figsize=(10,10))
            for n in list(df[df['neighbourhood_group_cleansed'] == borough]['neighbourhood_cleansed'].unique()):
                ax.hist(df[df['neighbourhood_cleansed'] == n]['price'], 100, range=(min_value,max_value), histtype='bar')
            ax.set_title(f"Distribution of Airbnb Listings in {borough}")
            ax.set_ylabel('Frequency')
            ax.set_xlabel('Prices')
            ax.legend()
            st.pyplot(
                fig
            )



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


with st.sidebar: # creates side bar
    borough = st.selectbox(
        label = "Select Borough Below",
        options = borough_values
    )
    if borough != "All":
        neighborhood_values = df[df['neighbourhood_group_cleansed'] == borough]['neighbourhood_cleansed'].unique()
        neighborhoods = st.multiselect(
            label="Select Neighborhood",
            options = neighborhood_values
        )
    else:
        neighborhood_values = df['neighbourhood_cleansed'].unique()
        neighborhoods = st.multiselect(
            label="Select Neighborhood",
            options = neighborhood_values
        )



#run helper functions
create_map(df, borough, neighborhoods)
create_means(df, borough, neighborhoods)
with st.expander("See Price Distribution"):
    create_chart(df, borough, neighborhoods)