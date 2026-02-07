import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image

model = load_model("potato_disease_model.keras")

class_names = [
    "Potato Early Blight",
    "Potato Late Blight",
    "Healthy Potato Leaf"
]

st.set_page_config(page_title="Potato Disease Detection", page_icon="🌱")
st.title("🌱 Potato Disease Detection")
st.write("Upload a potato leaf image to detect disease")

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", width=400)

    image = image.resize((224, 224))
    img_array = np.array(image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    idx = np.argmax(prediction)
    confidence = np.max(prediction)

    st.success(f"Prediction: {class_names[idx]}")
    st.write(f"Confidence: **{confidence * 100:.2f}%**")
