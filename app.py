import os
from flask import Flask, request
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Set up Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Select a working Gemini model
model = genai.GenerativeModel("models/gemini-1.5-pro")

# Home route (for testing)
@app.route('/')
def home():
    return "WhatsApp Bot is Live!"

# Webhook route for WhatsApp
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    
    try:
        message = data['message']
        phone = data['from']
        
        print(f"📩 Incoming from {phone}: {message}")
        
        # Generate response
        response = model.generate_content(message)
        reply = response.text
        
        print(f"🤖 Gemini Response: {reply}")
        
        # You'd return this to Twilio/Meta if integrated
        return {'reply': reply}, 200

    except Exception as e:
        print("🔥 Gemini Error:", str(e))
        return {'error': str(e)}, 500

# Run app (Render uses PORT environment variable)
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
