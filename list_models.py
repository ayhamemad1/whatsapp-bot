import google.generativeai as genai

genai.configure(api_key="AIzaSyCgEhoTEITrwufs4PwGERScFrqeQ9OA4N4")

models = genai.list_models()
for m in models:
    print(m.name)
