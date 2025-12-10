import streamlit as st
import plotly.express as px
import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

cursor.execute("SELECT date FROM temps")
dates = cursor.fetchall()
dates = [item[0] for item in dates]

cursor.execute("SELECT temp FROM temps")
temps = cursor.fetchall()
temps = [item[0] for item in temps]

graph = px.line(x=dates, y=temps, labels={'x': 'Date', 'y': 'Temperature'})

st.plotly_chart(graph)