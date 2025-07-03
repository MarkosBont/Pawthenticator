import time

import streamlit as st
from PIL import Image
from model.model import determine_breed
from utils import get_wikipedia

# Injecting Playfair Display font via Google Fonts
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    h1, h2, p, button{
        text-align: center;
    }

    .upload-instructions {
        text-align: center;
        margin-top: -10px;
        margin-bottom: 30px;
        color: #666;
    }
    </style>
""", unsafe_allow_html=True)


st.markdown("""
    <h1 style='
        text-align: center;
        font-family: "Playfair Display", serif;
        color: #B55C2B;
        font-size: 3em;
        margin-bottom: 0.5em;
    '>
        🐾 Pawthenticator
    </h1>
""", unsafe_allow_html=True)

st.markdown("""
        <h2 style ='
                text-align: center;
                font-family: "Playfair Display", serif;
                color: #B55C2B;
                font-size: 2em;
                margin-bottom: 0.5em;
        '>
            Drag and Drop Your Dog's Image Below!
        </h2>
""", unsafe_allow_html=True)

st.info("**Tip:** Upload a well-lit photo of your dog from a clear angle (ideally from the front or side). Good lighting and visibility help the model give more accurate predictions.")


file = st.file_uploader("file", type=["jpg", "jpeg", "png"], label_visibility="hidden")


if file:
    image = Image.open(file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    if st.button("DETERMINE BREED"):
        with st.spinner("Verifying your Dog's Breed..."):
            time.sleep(3)
            results = determine_breed(image)
            st.markdown("""
                <h1 style='
                    text-align: center;
                    font-family: "Playfair Display", serif;
                    color: #B55C2B;
                    font-size: 3em;
                    margin-bottom: 0.5em;
                '>
                    🐾 Prediction Results - Top 3
                </h1>
            """, unsafe_allow_html=True)
            st.info("Below are the top 3 most likely **pure breeds** your dog resembles. This does **not** indicate a mix or combination of breeds. If the model is **very confident** in it's prediction, just **one dog breed** will be shown. ")
            for (breed, confidence) in results:
                with st.expander(f"{breed} - {confidence * 100:.2f}% Confidence"):
                    if confidence > 0.9:
                        st.success(f"✅ Your Dog is likely a {breed}! ")
                        st.write(f"Here's some information about the {breed}:")
                        st.write(f"{get_wikipedia(breed)}")
                        break
                    st.markdown(f"""
                        <h3 style='
                            text-align: center;
                            font-family: "Playfair Display", serif;
                            color: #B55C2B;
                            font-size: 1.8em;
                        '>
                            {breed} — {confidence * 100:.2f}% Confidence
                        </h3>
                    """, unsafe_allow_html=True)
                    st.write(f"Here's some information about the {breed}: \n {get_wikipedia(breed)}")

