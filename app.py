import streamlit as st
import pandas as pd

st.title("TEAM MARVIN INTAKE DASHBOARD")

df = pd.read_excel("TEAM MARVIN INTAKE FILE New app.xlsx",header=4)

st.dataframe(df)
