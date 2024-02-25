import streamlit as st
import tensorflow as tf
from PIL import Image

# Load the pre-trained TensorFlow model
model = tf.keras.models.load_model('your_model.h5')  # Replace with your model path

# Define a function to preprocess the image
def preprocess_image(image):
    image = image.resize((224, 224))  # Adjust dimensions as needed
    image = tf.keras.applications.mobilenet_v2.preprocess_input(image)
    return image

# Title and instructions
st.title("COVID-19 Detection Tool")
st.write("Upload a chest X-ray image to check for potential COVID-19 infection.")

# File uploader
uploaded_file = st.file_uploader("Choose an image")

if uploaded_file is not None:
    # Read the image
    image = Image.open(uploaded_file)

    # Preprocess the image
    image = preprocess_image(image)

    # Expand dimensions to match model input
    image = tf.expand_dims(image, axis=0)

    # Make prediction
    prediction = model.predict(image)
    covid_probability = prediction[0][0]  # Assuming model outputs a single probability

    # Display results
    st.image(image, caption="Uploaded Image")
    st.write("Prediction:",
             f"COVID-19 positive with {covid_probability:.2%} probability")

else:
    st.warning("Please upload an image to proceed.")