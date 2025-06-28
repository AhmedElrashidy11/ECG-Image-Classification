import gradio as gr
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image

model = load_model("ecg_model.h5")
class_names = ['class1', 'class2', 'class3']

def classify_ecg(img):
    img = img.resize((224, 224))
    img_array = np.expand_dims(np.array(img), axis=0) / 255.0
    prediction = model.predict(img_array)
    return {class_names[i]: float(prediction[0][i]) for i in range(len(class_names))}

gr.Interface(fn=classify_ecg, inputs=gr.Image(type="pil"), outputs=gr.Label(num_top_classes=3)).launch()
