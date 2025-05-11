import pandas as pd
import streamlit as st

df = pd.read_csv("data/EoC_Final.csv")
st.title('Test')
st.write("Does it work?", df['Date'][0])