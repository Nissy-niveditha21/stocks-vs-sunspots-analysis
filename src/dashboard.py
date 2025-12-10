import streamlit as st
import pandas as pd
import plotly.express as px

from data_loader import load_stock_data, load_sunspot_data
from transform import convert_stock_daily_to_monthly, clean_sunspots, merge_stock_sunspots

st.title("MAANG Stocks vs Sunspot Activity Dashboard")

# File paths
STOCK_PATH = "data/stock_monthly.csv"  # rename after monthly conversion
SUNSPOT_PATH = "data/sunspots_monthly.csv"

# Load data
daily_stock = load_stock_data(STOCK_PATH)
sunspots = load_sunspot_data(SUNSPOT_PATH)

# Convert daily -> monthly
monthly_stock = convert_stock_daily_to_monthly(daily_stock)

# Clean sunspot dataset
clean_sun = clean_sunspots(sunspots)

# Merge
merged_df = merge_stock_sunspots(monthly_stock, clean_sun)

st.subheader("Merged Dataset (Preview)")
st.dataframe(merged_df.head())

# Stock graph
st.subheader("Monthly Stock Price Trend")
stock_fig = px.line(merged_df, x="Date", y="Close", title="MAANG Stock Price (Monthly)")
st.plotly_chart(stock_fig)

# Sunspot graph
st.subheader("Monthly Sunspot Number Trend")
sunspot_fig = px.line(merged_df, x="Date", y="SunspotNumber", title="Sunspot Activity (Monthly)")
st.plotly_chart(sunspot_fig)

# Combined overlay
st.subheader("Overlay: Stock Prices vs Sunspot Activity")
overlay_fig = px.line(merged_df, x="Date", y=["Close", "SunspotNumber"], title="Correlation Overlay")
st.plotly_chart(overlay_fig)

st.write("Observations:")
st.write("""
- Peaks in sunspot cycles occur roughly every 11 years.
- You can examine if market volatility increases near solar maxima.
- This dashboard helps visualize temporal alignment.
""")
