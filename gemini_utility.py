from dotenv import load_dotenv

import os
import google.generativeai as genai

load_dotenv()
apiKey=os.getenv("GEMINI_API_KEY")
genai.configure(api_key=apiKey)

def getGeminiModels():
    return genai.list_models()

def get_gemini_pro_response(prompt):
    model=genai.GenerativeModel("gemini-pro")
    response=model.generate_content(prompt)
    return response.text

def get_gemini_pro_vision_response(input,image):
    model = genai.GenerativeModel("gemini-pro-vision")
    response= model.generate_content([input,image])
    return response.text
