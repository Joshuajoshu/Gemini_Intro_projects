from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai
from PIL import Image

load_dotenv()
apiKey=os.getenv("GEMINI_API_KEY")
genai.configure(api_key=apiKey)
model= genai.GenerativeModel("gemini-pro-vision")
chat=model.start_chat(history=[])

def get_gemini_response(input,image):
    model = genai.GenerativeModel("gemini-pro-vision")
    response= model.generate_content([input,image])
    return response.text

#prepare ui


st.title("Talk with an image")
if 'chat_history' not in st.session_state:
    st.session_state['chat_history']=[]
upload = st.file_uploader("Choose a file ",type=['jpg','png','jpeg'])
image=""
if upload is not None:
    image=Image.open(upload)
    st.image(image,caption="Uploaded file",use_column_width=True)
input= st.text_input("enter a query",key="input")
button= st.button("Generate")
if button and input:
        response=get_gemini_response(input,image)
        st.session_state['chat_history'].append(("you", input))
        st.subheader("response is:")
        
        st.write(response)
        st.session_state['chat_history'].append(("Bot",response))
        st.subheader("chat History is:")
        for role,text in st.session_state['chat_history']:
            st.write(f"{role}:{text}")
        







































# import streamlit as st
# import gemini_utility as genai

# from PIL import Image

# st.title("Image to text llm APP")
# upload = st.file_uploader("Choose a file ",type=['jpg','png','jpeg'])
# image=""
# if upload is not None:
#     image=Image.open(upload)
#     st.image(image,caption="Uploaded file",use_column_width=True)

# def get_gemini_response(input,image):
#     model = genai.GenerativeModel("gemini-pro-vision")
#     response= model.generate_content([input,image])
#     return response.text

# input=st.text_input("Enter your prompt")
# button=st.button("Generate")
# if button:
#     resp=genai.get_response(input,image)
#     st.subheader("Response is:")
#     st.write(resp)

# st.title("Talk with an image")
# if 'chat_history' not in st.session_state:
#     st.session_state['chat_history']=[]
