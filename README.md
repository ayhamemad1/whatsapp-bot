# WhatsApp Gemini Bot

A lightweight AI-powered chatbot built using **Flask** and **Google Gemini (Generative AI)**. This app is designed to receive messages (e.g., from WhatsApp or Twilio) and respond using a Gemini language model.

---

## Features

- Receives incoming messages through a webhook.
- Generates intelligent responses using Gemini 1.5 Pro.
- Flask-based API server.
- `.env` support for secret keys and environment variables.
- Deployable on Render with minimal configuration.

---

## How it Works

1. The app receives a POST request containing the user's message.
2. It extracts the message and phone number.
3. The Gemini API is used to generate a response.
4. The response is returned as a JSON object (for integration with WhatsApp or other services).

---

## Local Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/ayhamemad1/whatsapp-bot.git
   cd whatsapp-bot
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory:

   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

4. Run the app:

   ```bash
   python src/app.py
   ```

---

## Deployment (Render)

This project is ready for deployment on [Render](https://render.com).

- Set **Build Command**:

  ```bash
  pip install -r requirements.txt
  ```

- Set **Start Command**:

  ```bash
  python3 src/app.py
  ```

- Add `GEMINI_API_KEY` as an environment variable in Render.

---

## File Structure

```
whatsapp-bot/
├── src/
│   └── app.py
├── requirements.txt
├── render.yaml
├── .env
└── .gitignore
```

---

## Dependencies

- Flask
- python-dotenv
- google-generativeai

---

## License

MIT © AyhamEmad1
