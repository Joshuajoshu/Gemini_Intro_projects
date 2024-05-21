import gemini_utility as genai

models=genai.getGeminiModels()

for model in models:
    if'generateContent' in model.supported_generation_methods:
        print(model.name)