from flask import Flask, request
import openai
import os
from dotenv import load_dotenv

# Load .env
load_dotenv()

# Flask app setup
app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/webhook", methods=["POST"])
def webhook():
    from_number = request.form.get("From")
    user_msg = request.form.get("Body")

    print(f"📨 Incoming from {from_number}: {user_msg}")

    # AI reply
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You're a helpful customer service bot for خلطة القوة. Respond in friendly Saudi dialect."},
                {"role": "user", "content": user_msg}
            ]
        )
        reply = response.choices[0].message['content']
    except Exception as e:
        reply = "❌ Sorry, I had trouble replying. Please try again."

    # Return TwiML
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Message>{reply}</Message>
</Response>"""

if __name__ == "__main__":
    app.run(port=5000)
