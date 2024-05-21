from dotenv  import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

apikey=os.getenv("GEMINI_API_KEY")
genai.configure(api_key=apikey)
model=genai.GenerativeModel("gemini-pro")
 
prompt= "Translate quantum mechanics concepts into a story for teenagers"
try:
    response=model.generate_content(prompt,stream=True)
except:
    print("getting error because of")
else:
    #print(response.text)
    for chunk in response:
        print(chunk.text)
        print("-"*100)
