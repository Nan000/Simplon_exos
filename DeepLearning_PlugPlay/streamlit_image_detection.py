import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.resnet50 import preprocess_input, ResNet50
from tensorflow.keras.applications.imagenet_utils import decode_predictions
from tensorflow.keras.preprocessing import image
import tempfile


st.write("# ¿ What's on your picture ?")

# Function to Read and Manipulate Images
def load_image(img):
    image = Image.open(img)
    image = np.array(image)
    return image

def predict(img):
    img = image.load_img(img,target_size=(224,224))
    resizedImage = image.img_to_array(img)
    imagewithmoredimension = np.expand_dims(resizedImage, axis = 0)
    # Prétraiter l'image pour la passer au modèle de classification
    image_processed = preprocess_input(imagewithmoredimension)
    # Faire une prédiction avec le modèle de classification
    model = ResNet50()
    prediction = model.predict(image_processed)
    results = decode_predictions(prediction, top=3)
    i= 1
    for result in results:
        for res in result:
            st.write(f'''prediction {i} : {res[1]} with probability = {'%.4f' % res[2]}''')
            i=i+1



# Uploading the File to the Page


st.set_option('deprecation.showfileUploaderEncoding', False)

buffer = st.file_uploader(label="Upload image", type=['jpg', 'png'])

if buffer:
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_file_path = f"{temp_dir}/uploaded_image.jpg"
        with open(temp_file_path, "wb") as temp_file:
            temp_file.write(buffer.read())

        st.image(buffer)
        st.write("Image Uploaded Successfully")

        if st.button('Submit'):
            predict(temp_file_path)
