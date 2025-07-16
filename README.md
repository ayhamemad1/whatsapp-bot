# WhatsApp Gemini Bot (Localhost Version)

A lightweight AI-powered chatbot built with **Flask** and **Google Gemini API**. It runs locally and can be exposed to the internet using **ngrok** for testing with WhatsApp, Twilio, or any webhook service.

---

## Features

- Runs locally on Flask
- Connects to Gemini 1.5 via API key
- Responds to incoming messages via `/webhook` endpoint
- Can be publicly exposed using `ngrok`
- Uses `.env` for secure API key management

---

## Prerequisites

- Python 3.8+
- A Google Gemini API key
- ngrok (for tunneling to localhost)

---

## Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/ayhamemad1/whatsapp-bot.git
cd whatsapp-bot
```

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate      # On macOS/Linux
venv\Scripts\activate         # On Windows
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

Create a `.env` file in the root folder:

```env
GEMINI_API_KEY=your_actual_gemini_api_key
```

### 5. Run the Flask app

```bash
python src/app.py
```

### 6. Start ngrok

```bash
ngrok http 5000
```

Copy the HTTPS URL shown and set it as the webhook endpoint in your WhatsApp API/Twilio dashboard.

Example:
```
https://your-ngrok-subdomain.ngrok.io/webhook
```

---

## Webhook Endpoint

Send a POST request to `/webhook` with this JSON format:

```json
{
  "message": "Hello",
  "from": "+123456789"
}
```

The server will reply with a JSON response containing the AI-generated reply.

---

## File Structure

```
whatsapp-bot/
├── src/
│   └── app.py
├── requirements.txt
├── .env
└── .gitignore
```

---

## Notes

- Make sure `.env` is listed in `.gitignore`
- Do not commit your API key to GitHub
- Use ngrok only for development/testing — not production

---

## License

MIT © AyhamEmad1
