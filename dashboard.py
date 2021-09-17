import streamlit as st
import pandas as pa
import numpy as np
import talib
import yfinance as yf
from datetime import date
import mpl_finance as mpf
import plotly.graph_objects as go


today = date.today()
option = st.sidebar.selectbox("Which Dashboard?", ('pattern','chart'))
stocks = st.sidebar.selectbox("Which Stock?", (
'RELIANCE.NS',
'METROPOLIS.NS',
'ALKYLAMINE.NS',
'MANINFRA.NS',
'ONGC.NS',
'COALINDIA.NS',
'TITAN.NS',
'IOC.NS',
'HEROMOTOCO.NS',
'BPCL.NS',
'EICHERMOT.NS',
'BAJAJ-AUTO.NS',
'MARUTI.NS',
'TATASTEEL.NS',
'ASIANPAINT.NS',
'KOTAKBANK.NS',
'HINDALCO.NS',
'DRREDDY.NS',
'GRASIM.NS',
'JSWSTEEL.NS',
'INFY.NS',
'BRITANNIA.NS',
'TATAMOTORS.NS',
'DIVISLAB.NS',
'LT.NS',
'WIPRO.NS',
'ITC.NS',
'TECHM.NS',
'NTPC.NS',
'BAJFINANCE.NS',
'SHREECEM.NS',
'SBIN.NS',
'BAJAJFINSV.NS',
'HCLTECH.NS',
'ADANIPORTS.NS',
'SBILIFE.NS',
'POWERGRID.NS',
'TCS.NS',
'ICICIBANK.NS',
'NESTLEIND.NS',
'SUNPHARMA.NS',
'UPL.NS',
'M&M.NS',
'AXISBANK.NS',
'TATACONSUM.NS',
'ULTRACEMCO.NS',
'INDUSINDBK.NS',
'HDFCBANK.NS',
'HDFC.NS',
'HINDUNILVR.NS',
'BHARTIARTL.NS',
'CIPLA.NS',
'HDFCLIFE.NS'))


st.header(option)
if option == 'pattern':
    pattern = st.sidebar.selectbox(
        "Which Pattern?",
        ("engulfing", "morning star")
    )

    if pattern == 'engulfing':
        
        today = date.today()
        data = yf.download({stocks}, start="2010-09-01", end=today)
        engulfing = talib.CDLENGULFING(data['Open'], data['High'], data['Low'], data['Close'])
        data['Engulfing'] = engulfing
        engulfing_days = data[data['Engulfing'] != 0]
        st.write(engulfing_days)

    elif pattern == 'morning star':
        
        
        data = yf.download({stocks}, start="2010-09-01", end=today)
        morning_star = talib.CDLMORNINGSTAR(data['Open'], data['High'], data['Low'], data['Close'])
        data['Morning_Star'] = morning_star
        star_days = data[data['Morning_Star'] != 0]
        st.write(star_days)


elif option == 'chart':
    
    data = yf.download({stocks}, start="2010-09-01", end=today)
    fig = go.Figure(data=[go.Candlestick(
                    open=data['Open'], 
                    high=data['High'], 
                    low=data['Low'], 
                    close=data['Close'], 
                    name=stocks)])
    fig.update_xaxes(type='category')
    fig.update_layout(height=750,width=850)
    st.plotly_chart(fig)
   

    

