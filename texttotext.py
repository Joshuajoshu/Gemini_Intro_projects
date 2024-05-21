import gemini_utility as genai

prompt="tell me a joke?"
print("Loading..")
try:
    resp = genai.get_gemini_pro_response(prompt)
    print(f"Response is: {resp}")
except:
    print("response error")
