import streamlit as st
import gemini_utility as genai

from PIL import Image

st.title("Image to text llm APP")
upload = st.file_uploader("Choose a file ",type=['jpg','png','jpeg'])
image=""
if upload is not None:
    image=Image.open(upload)
    st.image(image,caption="Uploaded file",use_column_width=True)

prompt= """
    you are an expert in advertising . you are given a advertising image.
    please provide the click through rate in the form of percentage with succeded percentage symbol
    and give some improvement/suggestion  to increase in the CTR 
"""
input=st.text_input("Enter your prompt")
button=st.button("Generate")
if button:
    resp=genai.get_gemini_pro_vision_response(input + prompt,image)
    st.subheader("Response is:")
    st.write(resp)