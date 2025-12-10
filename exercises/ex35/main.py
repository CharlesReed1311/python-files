import streamlit as st
import glob
from pathlib import Path 
import plotly.express as px
from nltk.sentiment import SentimentIntensityAnalyzer

st.title("Diary Tone")

diaries = glob.glob("diary/*.txt")
sorted_diaries = sorted(diaries)

dates = []
for diary in sorted_diaries:
    diary = diary.strip("diary\\")
    diary = diary.strip(".txt")
    dates.append(diary)

entries = []
analyser = SentimentIntensityAnalyzer()
neg_scores = []
pos_scores = []
for diary in diaries:
    with open(diary,'r') as file:
        entry = file.read()
    score = analyser.polarity_scores(entry)
    neg_scores.append(score['neg'])
    pos_scores.append(score['pos'])

st.subheader("Positivity")
figure = px.line(x=dates, y=pos_scores, labels={"x":"Date","y":"Score"})
st.plotly_chart(figure)

st.subheader("Negativity")
figure = px.line(x=dates, y=neg_scores, labels={"x":"Date","y":"Score"})
st.plotly_chart(figure)