#!/usr/bin/env python
# coding: utf-8

# Python Project Using Streamlit the fastest way to build data apllication

# Simple stock price

# In[6]:


import yfinance as yf
import streamlit as st
import pandas as pd

st.write(""""
# Simple Stock Price App
Shown are the stock closing price and volume of Google

"""")


#define the ticker symbol
tickerSymbol = "GOOGL"
#get data on this thicker
tickerData = yf.Ticker(tickerSymbol)
#get the historical price of this data
tickerDf = tickerData.history(period="1d",start='2010-5-31',end="2020-5-31")
#Open High Low Close Volume Dividends Stock Splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)


# In[ ]:




