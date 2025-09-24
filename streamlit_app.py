import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

title="Cross Asset Regime Monitor"
st.set_page_config(title,layout="wide")
st.title(title)

data = pd.read_csv("all_data.csv", index_col=0, parse_dates=True)
data = data.ffill().dropna()
returns = data.pct_change()
cum_returns = (1 + returns).cumprod()
assets = cum_returns.columns

min_date=cum_returns.index[0]
max_date=cum_returns.index[-1]

with st.sidebar:
    selected_assets=st.multiselect("Please select your assets",assets)
    range_start, range_end = st.date_input("Date Range", value=(min_date, max_date))

fig1=plt.figure(figsize=(10,5))
plt.plot(cum_returns,label=cum_returns.columns)
plt.legend()
plt.xlabel("Date")
plt.ylabel("Cumulative Return")
plt.title(title)

st.dataframe(cum_returns)
st.pyplot(fig1)

fig2=plt.figure(figsize=(10,5))
plt.plot(cum_returns[selected_assets],label=cum_returns[selected_assets].columns)
plt.legend()
plt.xlabel("Date")
plt.ylabel("Cumulative Return")
plt.title(title)

st.pyplot(fig2)