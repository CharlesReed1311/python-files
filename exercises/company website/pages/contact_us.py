import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Your Email Address:")

    with open("topics.csv",'r') as file:
        topics_list = file.readlines()

    topic = st.selectbox(label="What topics do you want to discuss?", options=topics_list)

    raw_message = st.text_area("Your message:")
    message = f"""\
Subject:New message from {user_email}

From:{user_email}
Topic: {topic}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Email sent successfully")

