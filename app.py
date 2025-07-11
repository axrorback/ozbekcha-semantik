from flask import Flask, request, render_template
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from deep_translator import GoogleTranslator
import torch
import torch.nn.functional as F

app = Flask(__name__)

# Model yuklash
model_name = "nlptown/bert-base-multilingual-uncased-sentiment"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)


# Sentiment aniqlash funksiyasi
def analyze_uzbek_sentiment(text_uz):
    # Tarjima
    text_en = GoogleTranslator(source='uz', target='en').translate(text_uz)

    # Sentiment tahlil
    inputs = tokenizer(text_en, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    probs = F.softmax(logits, dim=1)
    score = torch.argmax(probs, dim=1).item() + 1  # 1–5

    # Natijani oddiy ko‘rinishda chiqarish
    if score <= 2:
        return "Negative"
    elif score == 3:
        return "Neutral"
    else:
        return "Positive"


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        user_text = request.form["text"]
        label = analyze_uzbek_sentiment(user_text)
        result = {
            "text": user_text,
            "label": label
        }
    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
