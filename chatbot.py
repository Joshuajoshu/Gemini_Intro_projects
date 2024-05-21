from dotenv import load_dotenv
import os
import google.generativeai as genAi
import streamlit as st

load_dotenv()

apikey = os.getenv("GEMINI_API_KEY")
genAi.configure(api_key = apikey)
model = genAi.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(prompt):
    response = chat.send_message(prompt, stream=True)
    return response

#prepare ui
st.title("LLM Chat Bot")
if "chat_history" not in st.session_state:
  st.session_state['chat_history'] = []

input = st.text_input("Enter your question: ", key="input")
submit = st.button("Generate") 
if submit and input:
    response = get_gemini_response(input)
    st.session_state['chat_history'].append(("you", input))
    st.subheader("The response is:")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot",chunk.text))
        
    st.subheader("Chat History is: ")
    for role, text in st.session_state['chat_history']:
        st.write(f"{role}: {text}")