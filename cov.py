import streamlit as st
import numpy as np
from PIL import Image
st.title("New Project")
img_file_buffer = st.file_uploader('Upload a PNG image', type='png')
if img_file_buffer is not None:
    image = Image.open(img_file_buffer)
    img_array = np.array(image)
    st.image(image)
st.button("Predict")