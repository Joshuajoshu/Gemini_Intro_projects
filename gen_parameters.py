from dotenv  import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

apikey=os.getenv("GEMINI_API_KEY")
genai.configure(api_key=apikey)
model=genai.GenerativeModel("gemini-pro")
 
# print(genai.get_model("models/gemini-pro"))
# print("-"*100)
# print(genai.get_model("models/gemini-pro-vision"))
# generation_config= genai.types.GenerationConfig(candidate_count=1,stop_sequences=[';'])

# model=genai.GenerativeModel("gemini-pro",generation_config=generation_config)
prompt="what is the meaning of life "
# resp=model.generate_content(prompt)
# print(resp.text)
#print(generation_config)

config_temp0= genai.types.GenerationConfig(temperature=0.0)
config_temp1= genai.types.GenerationConfig(temperature=1.0)

resp_temp0=model.generate_content(prompt,generation_config=config_temp0)
print(resp_temp0.text)

print("*"*100)
resp_temp1=model.generate_content(prompt,generation_config=config_temp1)
print(resp_temp1.text)




