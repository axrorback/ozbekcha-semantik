# 🇺🇿 Uzbek Sentiment Analysis Web App

A professional web application built with Flask for sentiment analysis of Uzbek-language text. The app seamlessly translates user input from Uzbek to English in the background, classifies the sentiment using a multilingual BERT model, and returns the result as either **Positive**, **Negative**, or **Neutral**. The frontend is styled with Bootstrap 5 for a clean and responsive user experience.

---

## 🚀 Features

* 🔄 Automatic translation from Uzbek to English (invisible to user)
* 💬 Sentiment classification using HuggingFace Transformers
* 🖥️ Simple and elegant web interface with Bootstrap 5
* 🌐 Ready to deploy as a web-based NLP tool

---

## 🧰 Tech Stack

* **Backend:** Python (Flask)
* **NLP Model:** `nlptown/bert-base-multilingual-uncased-sentiment`
* **Translation:** `deep-translator` (Google Translate)
* **ML Frameworks:** Transformers, Torch
* **Frontend:** HTML5, Bootstrap 5

---

## 📦 Installation

```bash
# (Optional) Create a virtual environment
python3 -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows

# Install required dependencies
pip install flask transformers torch deep-translator
```

---

## 🏁 Running the App

```bash
python app.py
```

Then, open your browser and navigate to:

```
http://127.0.0.1:5000
```

---

## 📁 Project Structure

```
ozbek_sentiment/
├── app.py
└── templates/
    └── index.html
```

---

## 🧠 How It Works

1. The user enters a sentence in Uzbek.
2. The backend translates it into English using Google Translate.
3. The translated text is passed into a pre-trained multilingual BERT model.
4. The model predicts a sentiment score from 1 to 5:

   * **1–2:** Negative
   * **3:** Neutral
   * **4–5:** Positive
5. The app renders the result with visual labels (badges).

---

## ⚠️ Notes

* Internet access is required for translation and model inference.
* Translation is backend-only and not visible to users.
* Python 3.13 compatibility is ensured via `deep-translator`, avoiding deprecated modules.

---

## 🌱 Future Improvements

* ✅ Telegram bot integration
* 📊 Sentiment trend analytics and history logging
* 🧩 REST API support for external integrations
* 🚢 Dockerized deployment option

---

## 👤 Author

**Axrorbek Ibrohimjonov**
Developer | NLP Enthusiast | Pythonista

> If you find this project helpful, feel free to ⭐ it and share with the community!
