import geopandas
from turtle import width
import streamlit as st 
import pandas as pd 
import numpy as np
import folium
import plotly.express as px
from streamlit_folium import folium_static
from traitlets import default


st.set_page_config(layout= 'wide')

@st.cache (allow_output_mutation= True)

def get_data(path):
    df= pd.read_csv(path)
    return df

@st.cache (allow_output_mutation= True)
def get_geofile(url):
    geofile = geopandas.read_file(url)

    return geofile



def create_filter(name_filter, data_of_filter):
    str_namefilter = str(name_filter)
    return st.sidebar.multiselect(str_namefilter, data_of_filter, default= None)
    


data = get_data('C:\\Users\\mathe\\Desktop\\PowerBi\\Comunidade_DS\\curso_python_zero_ds\\modulo_5\\kc_house_data.csv')
 

## get geofile
URL = 'https://opendata.arcgis.com/datasets/83fc2e72903343aabff6de8cb445b81c_2.geojson'
get_geofile(URL)


## add new features

data['price_m2'] = ((data['price'] / data['sqft_lot']) * 0.09290304 )

# =================================
# Data Overviwew
# =================================

f_atribuites = create_filter('Enter Columns', data.columns)

f_zipcode = create_filter('Enter zipcode', data['zipcode'].unique())

df = data.loc[data['zipcode'].isin(f_zipcode), f_atribuites]


st.title('Data Overview')



if (f_atribuites != []) & (f_zipcode != []):
    data = data.loc[data['zipcode'].isin(f_zipcode), f_atribuites]

elif (f_atribuites == []) & (f_zipcode != []):
    data = data.loc[data['zipcode'].isin(f_zipcode), :]

elif (f_atribuites != []) & (f_zipcode == []):
    data = data.loc[:, f_atribuites]

else:
    data = data.copy()


st.dataframe(data)


c1 , c2 = st.columns((1, 1))

## average metrics

df1 = data[['id','zipcode']].groupby('zipcode').count().reset_index()
df2 = data[['price','zipcode']].groupby('zipcode').mean().reset_index()
df3 = data[['sqft_living','zipcode']].groupby('zipcode').mean().reset_index()
df4 = data[['price_m2','zipcode']].groupby('zipcode').mean().reset_index()

## merge of dataframes 

m = pd.merge(df1, df2, on = 'zipcode', how = 'inner')
m1 = pd.merge(m, df3, on = 'zipcode', how = 'inner')
dfx = pd.merge(m1 ,df4 , on= 'zipcode', how = 'inner')

## rename columns 
dfx.columns = ['ZIPCODE','TOTAL HOUSES ','PRICE','SQRT LIVING','PRICE/M2']

c1.header('Average Values')
c1.dataframe(dfx , height= 600)


### statistic descriptive 

num_attribuites = data.select_dtypes(include= ['int64', 'float64'])
media = pd.DataFrame(num_attribuites.apply(np.mean))
median = pd.DataFrame(num_attribuites.apply(np.median))
std = pd.DataFrame(num_attribuites.apply(np.std))

max_ = pd.DataFrame(num_attribuites.apply(np.max))
min_ = pd.DataFrame(num_attribuites.apply(np.min))


dfx1 = pd.concat([ max_, min_ , media , median , std], axis= 1).reset_index()

dfx1.columns = ['attribuites','max','min', 'media', 'median','std']

c2.header("Descriptives Analysis")
c2.dataframe(dfx1 , height= 600)



# ======================
# portfolio density
# =======================

st.title('Region Overview')

c1, c2 = st.columns((1,1))
c1.header('Portifolio Density')


#df = data.sample(10)

## Base Map - Folium

density = folium.Map(location= [ data['lat'].mean(), data['long'].mean()] , default_zoom_start = 15 ) 


marker_cluster = MarkerCluster().add_to(density)

for name, row in df.iterrows():
    folium.Marker([row['lat'], row['long']],
    popup = 'Sold R${0} on: {1}. Features: {2} sqft , {3} bedrooms , {4} bathrooms , year built: {5}'.format
    ( row['price'] , row['date'] , row['sqft_living'], row['bedrooms'], row['bathrooms'], row['yr_built'])).add_to(marker_cluster)


with c1: 
    folium_static(density)


## Region price map 

c2.header('Price Density')

df = data[['zipcode', 'price']].groupby('zipcode').mean().reset_index()
# rename dataframe

df.columns = ['ZIP', 'PRICE']

geofile = folium.Map(location= [ data['lat'].mean(), data['long'].mean()] , default_zoom_start = 15 )

with c2:
    folium_static(geofile)




#===================================================
# distribuicao dos imoveis por categorias comerciais
#===================================================

st.sidebar.title('Commercial Options')
st.title('Commercial attributes')

## Average price per year 

df = data[['yr_built','price']].groupby('yr_built').mean().reset_index()

fig = px.line(df , x = 'yr_built', y = 'price' ,
 title= 'Change in the average price of real estate by year of construction')

st.plotly_chart(fig, use_container_width= True)


## Average price per day
data['date'] = pd.to_datetime(data['date']).dt.strftime('%Y-%m-%d')


df = data[['date','price']].groupby('date').mean().reset_index()

fig = px.line(df , x = 'date', y = 'price' ,
 title= 'Change in the average price of real estate by day')

st.plotly_chart(fig, use_container_width= True)