import streamlit as st 
import requests

api_key = "kovhvaXRu77dhr5SBqmhXiWb4CsRkdxs8j7CmYw5"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

apodresponse = requests.get(url)

apodjson = apodresponse.json()

title = apodjson["title"]
image_url = apodjson["hdurl"]
description = apodjson["explanation"]

st.set_page_config(layout="wide")

st.title(title)
st.image(image_url)
st.write(description)