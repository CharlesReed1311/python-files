import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("The Best Company")

content = """
Zadrigi dohaeriros iksos da'or
"""
st.write(content)

st.header("Our team")

col1,emptycol1, col2,emptycol2, col3 = st.columns([1.5,0.5,1.5,0.5,1.5])


df = pd.read_csv("data.csv") 

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.write(row["role"])
        st.image(rf"images\{row['image']}")

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.write(row["role"])
        st.image(rf"images\{row['image']}")

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.write(row["role"])
        st.image(rf"images\{row['image']}")