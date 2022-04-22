import streamlit as st
import pandas as pd

from ticker import Ticker

spy = Ticker("spy")
spy.SMA200
spy.PRICE
spy.CROSSED



st.title("HFEA & 200MA Strategy WebApp")


st.write(f"Ticker: SPY")
st.write(f"IS_CROSSED: {spy.CROSSED}")
st.write(f"SMA200: {spy.SMA200}")
st.write(f"PRICE: {spy.PRICE}")

st.write("Next: E-Mail & PushUp Notfications")
