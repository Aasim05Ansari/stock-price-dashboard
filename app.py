import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Stock Price Dashboard", layout="wide")

st.title("📈 Stock Price Visualization Dashboard")

# Sidebar for user input
st.sidebar.header("Settings")
ticker = st.sidebar.text_input("Stock Symbol", value="AAPL")
start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2023-01-01"))
end_date = st.sidebar.date_input("End Date", pd.to_datetime("today"))

# Fetch data
data = yf.download(ticker, start=start_date, end=end_date)
data["MA50"] = data["Close"].rolling(window=50).mean()
data["MA200"] = data["Close"].rolling(window=200).mean()

# Price chart
fig = go.Figure()
fig.add_trace(go.Scatter(x=data.index, y=data["Close"], mode="lines", name="Close Price", line=dict(color="blue")))
fig.add_trace(go.Scatter(x=data.index, y=data["MA50"], mode="lines", name="50-Day MA", line=dict(color="orange")))
fig.add_trace(go.Scatter(x=data.index, y=data["MA200"], mode="lines", name="200-Day MA", line=dict(color="green")))
fig.update_layout(title=f"{ticker} Stock Price", xaxis_title="Date", yaxis_title="Price (USD)", template="plotly_white")

st.plotly_chart(fig, use_container_width=True)

# Volume chart
st.subheader("Volume Traded")
st.bar_chart(data["Volume"])
