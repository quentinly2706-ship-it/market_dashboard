# Dashboard with equity (SPY), forex (USD), commodities (Gold ($GC=F), crude oil ($WTI, or $USD), wheat ($ZW=F)), bonds ($^TNX) (Inflation-linked bonds).
# Data about growth, inflation, volatility, and yield.
# Data goes back as far as possible, with widget slider to choose time frame.

# import streamlit as st 
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Getting the data for SPY (daily)
# Closing prices only
# spy = yf.download("SPY")['Close']
# spy.to_csv("spy_data.csv")
# print(spy.index)
# print('\n\n\n\n')

# df.fillna(method'fill") this fills in the missing values with the previous day's value

# Data Download
def data_download(ticker, filename, period="max", interval="1d"):
    data = yf.download(ticker, period=period, interval=interval)['Close']
    data.to_csv(filename)

# Create dictionary
ticker_filname={
    "SPY": "spy.csv",
    "DX-Y.NYB": "usd.csv",
    "GC=F": "gold.csv",
    "WTI": "wti.csv",
    "ZW=F": "wheat.csv",
    "^TNX": "bonds.csv"
}

# Download data for each ticker
# for ticker, filename in ticker_filname.items():
    #data_download(ticker, filename)

# Sanity checks
# Check for missing values
def check_na(data):
    null_sum=data.isna().sum()
    null_percentage = null_sum/len(data)
    print(f"Ratio of missing values: {null_percentage}\nCount of missing values: {null_sum}")

spy=pd.read_csv('spy.csv', index_col=0, parse_dates=True)
check_na(spy)

# Check for missing values
# missing_values = data.isnull().sum() # number is zero, no missing values

# Plot the data
# spy.plot(label='SPY')
#plt.ylabel("SPY Closing Price")
#plt.title("SPY Closing Price Over Time")
#plt.yscale('log')

# forex using USD index
# usd['DX-Y.NYB'].plot(label='USD Index')


#plt.legend()
#plt.show()

# ----- Future Work -----
# Write a short function to deal witht he missing values
# Scale the data
# Write a small functions for each of the data processing steps and the one main function ton call them all
# Streamlit dashboard
# Create a functio that does plotting in a systematic way
