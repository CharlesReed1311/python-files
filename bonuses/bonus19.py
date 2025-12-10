import streamlit as st 
from PIL import Image

st.title("Colored to Grayscale Converter")

with st.expander("Upload image"):
    uploaded_image = st.file_uploader("Upload Image")

with st.expander("Start Camera"):
    camera_image = st.camera_input("Camera")

if camera_image:
    img = Image.open(camera_image)
    grayimg = img.convert("L")
    st.image(grayimg)
elif uploaded_image:
    img = Image.open(uploaded_image)
    grayimg = img.convert("L")
    st.image(grayimg)