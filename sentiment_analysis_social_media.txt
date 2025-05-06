from flask import Flask, request
from textblob import TextBlob
import textwrap

app = Flask(_name_)

@app.route('/')
def index():
    return '''
        <html>
        <head>
            <title>Emotion & Sentiment Analyzer</title>
            <style>
                body { font-family: Arial; margin: 50px; }
                textarea { width: 100%; height: 150px; font-size: 16px; }
                input[type="submit"] { font-size: 18px; padding: 10px 20px; }
                .result { margin-top: 30px; padding: 20px; border: 1px solid #ccc; }
            </style>
        </head>
        <body>
            <h1>Analyze Emotions in Social Media Text</h1>
            <form method="POST" action="/analyze">
                <textarea name="text" placeholder="Enter or paste conversation here..."></textarea><br><br>
                <input type="submit" value="Analyze">
            </form>
        </body>
        </html>
    '''

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    # Simple emotion mapping
    if polarity > 0.1:
        sentiment = "Positive"
        emotion = "Happy / Excited"
    elif polarity < -0.1:
        sentiment = "Negative"
        emotion = "Angry / Sad"
    else:
        sentiment = "Neutral"
        emotion = "Calm / Uncertain"

    return f'''
        <html>
        <head>
            <title>Result</title>
            <style>
                body {{ font-family: Arial; margin: 50px; }}
                .result {{ margin-top: 30px; padding: 20px; border: 1px solid #ccc; }}
                a {{ text-decoration: none; color: blue; }}
            </style>
        </head>
        <body>
            <h1>Analysis Result</h1>
            <div class="result">
                <p><strong>Text:</strong> {textwrap.fill(text, width=100)}</p>
                <p><strong>Sentiment:</strong> {sentiment}</p>
                <p><strong>Emotion:</strong> {emotion}</p>
                <p><strong>Polarity Score:</strong> {polarity:.2f}</p>
                <p><strong>Subjectivity Score:</strong> {subjectivity:.2f}</p>
            </div>
            <br><a href="/">Analyze Another</a>
        </body>
        </html>
    '''

if _name_ == '_main_':
    app.run(debug=True)
