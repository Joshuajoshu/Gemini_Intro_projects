import gemini_utility as genai
import streamlit as st


from PIL import Image
st.title("Chat with Bill")
uploaded_file=st.file_uploader("Choose a bill",type=['jpg','jpeg','png'])
image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption="the bill and invoice",use_column_width=True)

prompt=""" You are an expert in understanding invoices. You will receive input input image as invoice and you have to answer questions based on the input image."""

qtn_input=st.text_input("Type your questrion here abour Invoice")

submit= st.button("get me answer")
if submit:
    resp=genai.get_gemini_pro_vision_response(prompt +""+qtn_input,image)
    st.subheader("Response is")
    st.write(resp)

