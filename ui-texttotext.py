import gemini_utility as genai
import streamlit as st

st.set_page_config(page_title="Text to Text")
st.title("text 2 text llm application")
input = st.text_input("ENter your Prompt here")
button=st.button("Generate")

if button:
    resp=genai.get_gemini_pro_response(input)
    st.subheader("Response :")
    st.write(resp)