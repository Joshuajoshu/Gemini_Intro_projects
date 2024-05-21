import streamlit as st
import gemini_utility as genai

from PIL import Image

st.title("Image to text llm APP")
upload = st.file_uploader("Choose a file ",type=['jpg','png','jpeg'])
image=""
if upload is not None:
    image=Image.open(upload)
    st.image(image,caption="Uploaded file",use_column_width=True)
input=st.text_input("Enter your prompt")
button=st.button("Generate")
if button:
    resp=genai.get_gemini_pro_vision_response(input,image)
    st.subheader("Response is:")
    st.write(resp)