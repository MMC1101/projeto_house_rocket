from unicodedata import decimal
import geopandas
#from turtle import width
import streamlit as st 
import pandas as pd 
import numpy as np
import folium
import plotly.express as px
from streamlit_folium import folium_static
from folium.plugins   import MarkerCluster
from traitlets import default
from datetime import datetime, time 



st.set_page_config(layout= 'wide')

@st.cache (allow_output_mutation= True)

def get_data(path):
    data = pd.read_csv(path , sep = ',')
    return data

@st.cache (allow_output_mutation= True)

def get_geofile(url):
    geofile = geopandas.read_file(url)

    return geofile



def create_filter(name_filter, data_of_filter):
    str_namefilter = str(name_filter)
    return st.sidebar.multiselect(str_namefilter, data_of_filter, default= None)

def set_feature(data):
    ## add new features 
    data['price_m2'] = data['price'] / data['sqft_lot']
    return data

def overview_data( data ):
    f_atribuites = create_filter('Enter Columns', data.columns)
    f_zipcode = create_filter('Enter zipcode', data['zipcode'].unique())

#df = data.loc[data['zipcode'].isin(f_zipcode), f_atribuites]


    st.title('Data Overview')

    if (f_atribuites != []) & (f_zipcode != []):
        dfa = data.loc[data['zipcode'].isin(f_zipcode), f_atribuites]

    elif (f_atribuites == []) & (f_zipcode != []):
        dfa = data.loc[data['zipcode'].isin(f_zipcode), :]

    elif (f_atribuites != []) & (f_zipcode == []):
        dfa = data.loc[:, f_atribuites]

    else:
        dfa = data.copy()


    st.dataframe(dfa.head())


    c1 , c2 = st.columns((1, 1))

## average metrics

    df1 = data.loc[:, ['id','zipcode']].groupby('zipcode').count().reset_index()
    df2 = data.loc[:, ['price','zipcode']].groupby('zipcode').mean().reset_index()
    df3 = data.loc[:, ['sqft_living','zipcode']].groupby('zipcode').mean().reset_index()
    df4 = data.loc[:, ['price_m2','zipcode']].groupby('zipcode').mean().reset_index()

## merge of dataframes 

    m = pd.merge(df1, df2, on = 'zipcode', how = 'inner')
    m1 = pd.merge(m, df3, on = 'zipcode', how = 'inner')
    dfx = pd.merge(m1 ,df4 , on = 'zipcode', how = 'inner')

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

    return None

def create_map(data, geofile):

 
# ======================
# portfolio density
# =======================


    st.title('Region Overview')
    c1, c2 = st.columns((1,1))
    c1.header('Portifolio Density')   

## Base Map - Folium

    density = folium.Map(location= [ data['lat'].mean(), data['long'].mean()] , default_zoom_start = 15 ) 


    marker_cluster = MarkerCluster().add_to(density)

    for name, row in data.iterrows():
         folium.Marker( [row['lat'], row['long'] ], 
        popup='Sold R${0} on: {1}. Features: {2} sqft, {3} bedrooms, {4} bathrooms, year built: {5}'.format( row['price'],
                                     row['date'],
                                     row['sqft_living'],
                                     row['bedrooms'],
                                     row['bathrooms'],
                                     row['yr_built'] ) ).add_to( marker_cluster )


    with c1: 
        folium_static(density)

## Region price map 

    c2.header('Price Density')

    df3 = data[['zipcode', 'price']].groupby('zipcode').mean().reset_index()
# rename dataframe

    df3.columns = ['ZIP', 'PRICE']

    geofile = geofile[geofile['ZIP'].isin(df3['ZIP'].tolist())]
  
    region_price_map  = folium.Map(location= [data['lat'].mean(), data['long'].mean()] , default_zoom_start = 15 )

    region_price_map.choropleth(geo_data = geofile,
                            data = df3,
                            columns = ['ZIP', 'PRICE'],
                            Key_on = 'feature.properties.ZIP',
                            fill_color='YlGnBu', fill_opacity=.7, line_opacity=.2,
                            legend_name = 'AVG PRICE')
    with c2:
        folium_static(region_price_map)

    return None


def commercial_distribuition(data):

#===================================================
# distribuicao dos imoveis por categorias comerciais
#===================================================

    st.sidebar.title('Commercial Options')
    st.title('Commercial attributes')

## Average price per year 

    data['date'] = pd.to_datetime(data['date']).dt.strftime('%Y-%m-%d')



### Filters

    min_year_built = int(data['yr_built'].min())
    max_year_built = int(data['yr_built'].max())

    st.sidebar.subheader('Select Max Year Built')
    st.header('Average Price per Year built')

    f_year_built = st.sidebar.slider('Year Built', min_year_built , max_year_built , min_year_built)




    df = data.loc[data['yr_built'] < f_year_built]
    df = df[['yr_built', 'price']].groupby('yr_built').mean().reset_index()


## Plot
    fig = px.line(df , x = 'yr_built', y = 'price')
    st.plotly_chart(fig, use_container_width= True)




## ====================
## Average price per day
    st.header('Average Price per day')
    st.sidebar.subheader('Select Max Date')
## ===================

    min_year_date = datetime.strptime(data['date'].min() , '%Y-%m-%d')
    max_year_date = datetime.strptime(data['date'].max() , '%Y-%m-%d')
    f_date = st.sidebar.slider('Date' , min_year_date , max_year_date , min_year_date)

# data filtering 
    data['date'] = pd.to_datetime(data['date'])
    df = data.loc[data['date'] < f_date]
    df = data[['date','price']].groupby('date').mean().reset_index()


    fig = px.line(df , x = 'date', y = 'price' ,
    title= 'Change in the average price of real estate by day')

    st.plotly_chart(fig, use_container_width= True)


### Histograma 

    st.sidebar.subheader('Select Price')
    st.header('Price Distribution')

## Filter

    min_price = int(data['price'].min())
    max_price = int(data['price'].max())
    avg_price = int(data['price'].mean())

## Data filtering
    f_price = st.sidebar.slider('Price', min_price , max_price , avg_price)
    df = data.loc[data['price'] < f_price]

## data plot
    fig = px.histogram(df, x="price", nbins=50)
    st.plotly_chart(fig, use_container_width=True)
    return None

def attributes_distribution(data):


### ==========================================
## Distribuicao dos imoveis por categorias fisicas
## ===========================================

    st.sidebar.title('Attibuites Options')
    st.title('House Atributes')

## Filters 

    f_bedrooms = st.sidebar.selectbox('Max number of bedrooms', sorted(set(data['bedrooms'].unique())))

    f_bathrooms = st.sidebar.selectbox('Choose the number of bathrooms', sorted(set(data['bathrooms'].unique())) )

    f_floors = st.sidebar.selectbox('Max number of floor', data['floors'].sort_values().unique())

    f_waterview = st.sidebar.checkbox('Only Houses with water view')


    c3, c4 = st.columns(2)


## House per bedrooms 
    c3.header('Number of bedrooms')


    df = data[data['bedrooms'] < f_bedrooms] 
    fig = px.histogram(df, x= 'bedrooms', nbins=19, color_discrete_sequence=["yellow"])
    fig = fig.update_layout(plot_bgcolor="#0e1117")
    c3.plotly_chart(fig, use_container_width=True)

### House per bathrooms
    c4.header('Number of bathrooms') 
    df = data[data['bathrooms'] < f_bathrooms]
    fig = px.histogram(df, x= 'bathrooms', nbins=19, color_discrete_sequence=["yellow"])
    fig = fig.update_layout(plot_bgcolor="#0e1117")
    c4.plotly_chart(fig, use_container_width=True)


    c5, c6 = st.columns(2)


# ## House per floors 
    c5.header('Number of floor')
    df = data.loc[data['floors'] < f_floors]
    fig = px.histogram(df, x= 'floors', nbins=19, color_discrete_sequence=['red'])
    fig.update_layout( plot_bgcolor='#0e1117' )
    c5.plotly_chart(fig, use_container_width=True)

# ## House oer water view

    if f_waterview:
        df = data.loc[(data['waterfront']) == 1, 'waterfront']
    else: 
        df = data.copy()

    c6.header('water view')
    fig = px.histogram(df, x= 'waterfront', nbins=19, color_discrete_sequence=['red'])
    fig.update_layout( plot_bgcolor='#0e1117' )
    c6.plotly_chart(fig, use_container_width=True)
    return None

if __name__ == '__main__' :
 ### ETL 
## data_extration ===========================

    data = get_data('kc_house_data.csv')
    url = 'https://opendata.arcgis.com/datasets/83fc2e72903343aabff6de8cb445b81c_2.geojson'
    geofile = get_geofile(url)

## transformation 
    data = set_feature(data)

    overview_data(data)

    create_map(data, geofile)

    commercial_distribuition(data)

    attributes_distribution(data)

