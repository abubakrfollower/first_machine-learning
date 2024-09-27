import streamlit as st
import pandas as pd

st.title('Machine Learning Appp')
st.info("This is my first app")


with st.expander("data"):
  st.write("**Raw data**")
  df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv")
  df

