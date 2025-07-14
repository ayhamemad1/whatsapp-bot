#!/usr/bin/env python3
import sys
import os
import subprocess

# Add current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, '/opt/render/project/src')

# Install packages at runtime if needed
try:
    import flask
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--user', 'flask'])
    import flask

try:
    from flask import Flask, request, jsonify
    from dotenv import load_dotenv
    import google.generativeai as genai
except ImportError as e:
    print(f"Import error: {e}")
    # Install missing packages
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--user', 'flask', 'python-dotenv', 'google-generativeai'])
    from flask import Flask, request, jsonify
    from dotenv import load_dotenv
    import google.generativeai as genai

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize the model
model = genai.GenerativeModel('gemini-1.5-pro')

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "WhatsApp Gemini Bot is running!"})

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        # Get the incoming message data
        data = request.get_json()
        
        # Extract message and phone number (adjust based on your webhook format)
        message = data.get("message", "")
        phone_number = data.get("phone_number", "")
        
        if not message:
            return jsonify({"error": "No message provided"}), 400
        
        # Generate response using Gemini
        response = model.generate_content(message)
        ai_response = response.text
        
        # Return the response
        return jsonify({
            "response": ai_response,
            "phone_number": phone_number,
            "status": "success"
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)