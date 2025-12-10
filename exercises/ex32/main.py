import pandas as pd
import streamlit as st
import plotly.express as px

st.title("In search for happiness")

xaxis = st.selectbox("Select data for x-axis", ("GDP","Happiness","Generosity"))
yaxis = st.selectbox("Select data for y-axis", ("GDP","Happiness","Generosity"))

st.subheader(f"{xaxis} and {yaxis}")

df = pd.read_csv("happy.csv")

figure = px.scatter(x=df[f"{xaxis.lower()}"], y=df[f"{yaxis.lower()}"], labels={"x":xaxis, "y":yaxis})
st.plotly_chart(figure)