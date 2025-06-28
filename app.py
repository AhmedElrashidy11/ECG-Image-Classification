import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import json

st.set_page_config(page_title="ECG Classification", layout="centered")


st.title("🩺 ECG Image Classification")

model = load_model("ecg_model.h5")

with open("class_names.json", "r") as f:
    class_indices = json.load(f)

class_names = [None] * len(class_indices)
for label, index in class_indices.items():
    class_names[index] = label

uploaded_file = st.file_uploader("Upload an ECG image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    image_resized = image.resize((224, 224))
    image_array = img_to_array(image_resized) / 255.0
    image_array = np.expand_dims(image_array, axis=0)

    st.image(image, caption="Uploaded ECG Image", use_column_width=True)

    predictions = model.predict(image_array)

    if predictions.shape[1] != len(class_names):
        st.error("❌ Prediction shape mismatch with class names. Check your model and class_names.json.")
    else:
        predicted_class = class_names[np.argmax(predictions)]
        confidence = np.max(predictions)

        st.success(f"✅ Predicted Class: **{predicted_class}**")
        st.info(f"🔢 Confidence: {confidence:.2%}")

