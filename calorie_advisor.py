import gemini_utility as genai
import streamlit as st

from PIL import Image

st.title("Calorie Advisor - Gemini App")
uploaded_file=st.file_uploader("upload a dish or food",type=['jpg','jpeg','png'])
image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption="Food pic",use_column_width=True)

prompt="""
You are an expert in nutritioninst where you need to see the food itesm from the image and get_gemini_pro_vision_responsecalculate the total calorie,also provide the details of every food
items with calorie intake is below format
1.Item 1-- no of calories
2. Item 2 -- no of calories
--
--
"""
submit =st.button("tell me about calories")
if submit:
    resp=genai.get_gemini_pro_vision_response(prompt,image)
    st.subheader("Response is")
    st.write(resp)