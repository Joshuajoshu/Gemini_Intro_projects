from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()
apiKey=os.getenv("GEMINI_API_KEY")
genai.configure(api_key=apiKey)
model = genai.GenerativeModel("gemini-pro")
chat=model.start_chat(history=[])
response= chat.send_message("in one para explain how the internet works to a beginner")
# print(chat.history)
# print(chat.history[0])
# print(chat.history[0].parts[0].text)
response=chat.send_message("ok. more info about the IP addresses")
for item in chat.history:
    print(f"{item.role.capitalize()}:{item.parts[0].text}")
    print("-"*100)