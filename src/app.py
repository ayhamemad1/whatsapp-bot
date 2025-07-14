import os
from flask import Flask, request
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-1.5-pro")

@app.route('/')
def home():
    return "WhatsApp Bot is Live!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    try:
        message = data['message']
        phone = data['from']
        print(f"📩 Incoming from {phone}: {message}")
        response = model.generate_content(message)
        reply = response.text
        print(f"🤖 Gemini Response: {reply}")
        return {'reply': reply}, 200
    except Exception as e:
        print("🔥 Gemini Error:", str(e))
        return {'error': str(e)}, 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
