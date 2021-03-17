# streamlit.io
# https://www.youtube.com/watch?v=JwSS70SZdyM
import yfinance as yf
import streamlit as st
import pandas as pd

# steamlit apps are run at the command line using:
    # streamlit run [FILE_NAME] [ARGUMENTS]

# Some ports may be blocked from traffic,
# making the above command will give an error message.
# # https://discuss.streamlit.io/t/oserror-winerror-10013-an-attempt-was-made-to-access-a-socket-in-a-way-forbidden-by-its-access-permissions/1545/5

# Therfore, use

    # netstat -ao
    
# to find a open port, and use

    # streamlit run [FILE_NAME] [ARGUMENTS] --server.port ####
    
# to specify aport that can be used in place of ####.



st.write("""
# Simple Stock Price App

Shown are the stock closing price and volme of Google!

""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
# define ticker symbol
tickerSymbol = "GOOGL"
# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
# get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31',
                              end='2020-5-31')
# Open  High    Low Close   Volume  Dividendes  Stock Splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
