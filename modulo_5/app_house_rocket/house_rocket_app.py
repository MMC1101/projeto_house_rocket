import pandas as pd 
import streamlit as st
import numpy as np
import plotly.express as px 





st.title('House Rocket Company')

st.markdown('Welcome to House Rocker Data Analysis')

def title_dash(text):
    text = st.header(text)
    return text



title_dash('Company')
## read data 

@st.cache(allow_output_mutation= True)

def get_data(path):
    data = pd.read_csv(path)
    data['date'] = pd.to_datetime(data['date'])

    return data


## load data 

data = get_data('C:\\Users\\mathe\\Desktop\\PowerBi\\Comunidade_DS\\curso_python_zero_ds\\modulo_5\\kc_house_data.csv')

st.write(data.head())

# filter bedrooms


bedrooms = st.sidebar.multiselect('Number of bedrooms', data['bedrooms'].unique(), default= None)





if (len(bedrooms) == 0):
   st.write('Select Number of bedrooms')
else:
    st.write('You chosen', bedrooms[0])


## plot map 

title_dash('House Rocket Map')
is_check = st.checkbox('Display Map')

## filters 

price_min = int(data['price'].min())
price_max = int(data['price'].max())
price_avg = int(data['price'].mean())

price_slider = st.slider('Price Range',
                        price_min,
                        price_max,
                        price_avg )

# st.write('Prices', price_slider)


if (is_check == True):
    
## select rows

    houses = data[data['price'] < price_slider][['id','lat', 'long', 'price']].copy()
## draw map 
    fig = px.scatter_mapbox(houses, 
                        lat="lat", 
						lon="long",
                        size = 'price',
						hover_name = 'id', 
                        color_continuous_scale= px.colors.cyclical.IceFire, 
					    size_max = 15, 
						zoom=10)

    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    st.plotly_chart(fig)