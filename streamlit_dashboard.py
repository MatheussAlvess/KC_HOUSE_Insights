import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import folium
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster


st.set_page_config( layout='wide' )

@st.cache( allow_output_mutation=True )
def get_data( path ):
    data = pd.read_csv( path )
    return data


def overview_data(data):
    st.title('KC Housing Dashboard')

    if st.checkbox('Show KC dataset'):
        st.dataframe(data)


    df = data.select_dtypes(include=['int64', 'float64'])

    df_min = pd.DataFrame(df.apply(min)).T
    df_max = pd.DataFrame(df.apply(max)).T
    df_range = pd.DataFrame(df.apply(lambda x: x.max() - x.min())).T
    df_mean = pd.DataFrame(df.apply(np.mean)).T
    df_median = pd.DataFrame(df.apply(np.median)).T
    df_std = pd.DataFrame(df.apply(np.std)).T
    df_skew = pd.DataFrame(df.apply(lambda x: x.skew())).T
    df_kurtosis = pd.DataFrame(df.apply(lambda x: x.kurtosis())).T

    summary = pd.concat([df_min, df_max, df_range, df_mean, df_median, df_std, df_skew, df_kurtosis]).T
    summary.columns = ['Min', 'Max', 'Range', 'Mean', 'Median', 'Standard Deviation', 'Skewness', 'Kurtosis']

    aux = data.select_dtypes(['int64', 'float64'])
    aux = aux.drop('id', axis=1)
    aux1 = aux.groupby('zipcode').mean().reset_index()

    c1, c2 = st.columns(2)
    c1.subheader('Table of Statistical Descriptives')
    with c1:
        st.write(summary)

    c2.subheader('Average Values by Zipcode')
    with c2:
        st.write(aux1)


    return None

def region_overview(data):
    min_price = int(data['price'].min())
    max_price = int(data['price'].max())
    avg_price = int(data['price'].mean())
    f_waterview = st.sidebar.checkbox('Only House with Water View')

    if f_waterview:
        df = data[data['waterfront'] == 1]
    else:
        df = data.copy()


    price_slider = st.sidebar.slider('Select Price Range', min_price, max_price, avg_price + 20000)
    houses = data[(data['price'] < price_slider) & (data['waterfront'] == f_waterview)][
        ['price', 'id', 'lat', 'long', 'floors']]
    mapa = px.scatter_mapbox(houses, lat='lat', lon='long', size='price', color='floors', zoom=10,
                             mapbox_style='open-street-map')
    mapa.update_layout(margin={'r': 5, 'l': 5, 't': 5, 'b': 5})

    # Folium
    fl_map = folium.Map(location=[data['lat'].mean(), data['long'].mean()],
                        default_zoom_start=14)

    marker_cluster = MarkerCluster().add_to(fl_map)

    for name, row in data.iterrows():
        folium.Marker([row['lat'], row['long']],
                      popup='Sold R${0} on: {1}. Features: {2} sqft, {3}bedrooms,{4} bathrooms, year built: {5}'.format(
                          row['price'], row['date'], row['sqft_living'], row['bedrooms'],
                          row['bathrooms'], row['yr_built'])).add_to(marker_cluster)

    c1, c2 = st.columns(2)
    c1.subheader('Map of Houses by Prices and Floors')
    c1.write(mapa)
    c2.subheader('Map of Portfolio Density')
    with c2:
        folium_static(fl_map)


    min_year_built = int(data['yr_built'].min())
    max_year_built = int(data['yr_built'].max())
    # st.sidebar.subheader('Select Max Year Built')
    f_year_built = st.sidebar.slider('Year Built', min_year_built,
                                     max_year_built,
                                     min_year_built+25)

    st.header('Commercial Attributes')
    df = data.loc[data['yr_built'] < f_year_built]
    df = df[['yr_built', 'price']].groupby('yr_built').mean().reset_index()
    fig = px.line(df, x='yr_built', y='price')
    st.plotly_chart(fig, use_container_width=True)

    bedrooms = st.sidebar.selectbox('Max Number of Bedrooms', sorted(set(data['bedrooms'].unique())))
    bathrooms = st.sidebar.selectbox('Max Number of Bathrooms', sorted(set(data['bathrooms'].astype(int).unique())))
    f_floors = st.sidebar.selectbox('Max Number of Floors', sorted(set(data['floors'].unique())))


    st.header('Price Distribuition')
    df = data[data['price'] < price_slider]
    fig = px.histogram(df, x='price', nbins=50)
    st.plotly_chart(fig, use_container_width=True)

    c1, c2 = st.columns(2)
    # Houses per bedrooms

    c1.header('Houses per Number of Bedrooms')
    df = data[data['bedrooms'] < bedrooms]

    fig = px.histogram(df, x='bedrooms', nbins=19)
    c1.plotly_chart(fig, use_containder_width=True)

    # Houses per bathrooms
    c2.header('Houses per Number of Bathrooms')
    df = data[data['bathrooms'].astype(int) < bathrooms]
    fig = px.histogram(df, x='bathrooms', nbins=10)
    c2.plotly_chart(fig, use_containder_width=True)

    c1, c2 = st.columns(2)
    # Houses per floors
    c1.header('Houses per Floors')
    df = data[data['floors'] < f_floors]
    fig = px.histogram(df, x='floors', nbins=19)
    c1.plotly_chart(fig, use_containder_width=True)



    fig = px.histogram(df, x='waterfront', nbins=10)
    c2.header('Houses per Water View')
    c2.plotly_chart(fig, use_containder_width=True)


if __name__ == '__main__':
    path = 'kc_house.csv'
    path2 = 'dados2'


    f_buy = st.sidebar.checkbox('Only Houses to Buy')

    if f_buy:
        data = get_data(path2)
        data = data[data['status'] == 'buy']
        data['yr_built'] = pd.to_datetime(data['yr_built'])
        data['yr_built'] = data['yr_built'].dt.year
    else:
        data = get_data(path)


    overview_data(data)
    region_overview(data)
