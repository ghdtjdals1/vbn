import streamlit as st
from PIL import Image, ImageOps

def run():
    st.write("This page is place of alhambra")
    image = Image.open('Figure_1.jpg')

    border = 2
    image_with_border = ImageOps.expand(image, border=border, fill='white')

    st.image(image_with_border, use_column_width=True)