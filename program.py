#Difference between a close price and adjusted close price
# > Time serie is adjusted so that it doesn't record the actual price, it recoard the price include with the dividend

#Import the library
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import streamlit as st

#------------------------------------------------
#FUNCTION DEFINITION
#------------------------------------------------

#   Download the data
def download_data(tickers, start_date=None, end_date=None):
    data = yf.download(
        tickers, 
        start_date, 
        end_date,
        auto_adjust=True,
        progress=False
        )["Close"]
    return data

#   Save the data locally

#   Load the data
def load_data(file):
    data=pd.read_csv(file, index_col=0, parse_dates=True)
    return data
#   Preprocess the data
def preprocess(data):
    data=data.ffill().dropna()
    return data

def normalize(prices):
    returns=prices.pct_change().fillna(0)
    cum_returns=(1+returns).cumprod()
    return cum_returns

#   Create plot
def plot(data,title):
    fig=plt.figure(figsize=(8,6))
    plt.plot(data)
    plt.title(title)
    plt.xticks(rotation=45)
    plt.show()
    #plt.close()
    return fig

#   Create dashboard
def create_dashboard(data, title, fig):
    st.title(title)
    st.pyplot(fig)

#------------------------------------------------
# MAIN WORKFLOW (FUNCTION CALL)
#------------------------------------------------

#   Download the data
tickers=["ES=F","ZN=F","GC=F","CL=F","DX=F","ZW=F"]
#data = download_data(tickers)

#   Save the data locally
#data.to_csv("data.csv")

#   Load the data
prices=load_data("data.csv")
print(prices)

#   Preprocess the data
prices=preprocess(prices)
cum_returns=normalize(prices)

title="Cross-Asset Market Monitor"
fig=plot(cum_returns,title)
create_dashboard(cum_returns, title, fig)
#print(cum_returns)

#cum_returns.plot()
#plt.show()