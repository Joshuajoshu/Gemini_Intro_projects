from dotenv  import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

apikey=os.getenv("GEMINI_API_KEY")
genai.configure(api_key=apikey)
model=genai.GenerativeModel("gemini-pro")
 
prompt= "who is cm of ap"
try:
    response=model.generate_content(prompt)
except:
    print("getting error because of")
else:
    print(response.text)
finally:
    print(response.prompt_feedback)