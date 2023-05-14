import pandas as pd
import streamlit as st
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error
import plotly.express as px
import plotly.io as pio
import plotly.colors as pc
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from collections import Counter
import pmdarima as pm
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf
import statsmodels.api as sm
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split
from streamlit_toggle import st_toggle_switch
from streamlit_extras.app_logo import add_logo

import warnings
warnings.filterwarnings('ignore')

url1="https://drive.google.com/file/d/1TIqwO2-GbPuWXg07G64j-Qi4IzfudqCq/view?usp=sharing"
ipsoslogo='https://drive.google.com/uc?export=download&id='+url1.split('/')[-2]
st.set_page_config(
     page_title="Ipsos Analytical Tool",
     layout="wide",
     page_icon= ipsoslogo,
    initial_sidebar_state="expanded")

add_logo(ipsoslogo,height=270)
#################################################################################################################
# Load and prepare the data
#file_path = "C:\\Users\\User\\Desktop\\Streamlit\\streamlit_data.csv"
file_path = r"C:\Users\User\Desktop\Capstone\Streamlit\streamlit_data.csv"
important_channels = pd.read_csv(file_path)
important_channels = important_channels[~important_channels['Channel'].str.contains("ABU DHABI")]


#Get channel; input from user
channel = st.sidebar.selectbox('Select Channel:', important_channels['Channel'].unique())
#Get target
#Get channel; input from user
target = st.sidebar.selectbox('Select Target:', important_channels['Target'].unique())
#####################################################################################3
#Filter the data based on the above selected variables 
filtered_data = important_channels[(important_channels['Channel']==channel) & (important_channels['Target']==target)].sort_values(by='Date').dropna()
filtered_data['Date'] = pd.to_datetime(filtered_data['Date'])

#Set the Date as an index for better access in forecasting
filtered_data.set_index('Date', inplace=True)
ts_filtered_data = filtered_data['TRP'].asfreq('MS')

#Get forecast horizon input from user
forecast_horizon = st.sidebar.number_input("Select forecast horizon (in months)", min_value=6,step=6)

FORECAST_STEPS = forecast_horizon

def sarimax_forecast(df):
    # Fit the SARIMAX model
    sarimax_model = SARIMAX(df, order=(3, 1, 0), seasonal_order=(0, 1, 0, 12), enforce_stationarity=True, enforce_invertibility=True)
    sarimax_results = sarimax_model.fit()

    # Get the forecasted values
    sarimax_forecast = sarimax_results.forecast(steps=FORECAST_STEPS)

    # Create the plotly figure
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df, name='Actual'))
    fig.add_trace(go.Scatter(x=sarimax_forecast.index, y=sarimax_forecast.values, name='SARIMAX Forecast', marker=dict(color='#12BAAC')))
    fig.update_layout(title=f'SARIMAX Forecast for {channel}', xaxis_title='Year', yaxis_title='TRP')
    st.plotly_chart(fig)

    # Show the forecasted values in a table
    # Create a range of dates based on the forecast horizon
    forecast_dates = pd.date_range(start=df.index[-1], periods=FORECAST_STEPS + 1, freq='M')[1:]

    # Create a new DataFrame for the forecasted values
    forecast_df = pd.DataFrame({'Date': forecast_dates, 'Forecast': sarimax_forecast})
    forecast_df['Date'] = forecast_df['Date'].dt.strftime('%B %Y')
    forecast_df.set_index('Date', inplace=True)
    st.subheader("Forecasted Values")
    st.dataframe(forecast_df)
 

    return sarimax_forecast


# Call the sarimax_forecast function and apply it to the sliced data
sarimax_forecast(ts_filtered_data)
