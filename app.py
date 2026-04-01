from flask import Flask
import random

app = Flask(__name__)

quotes = [
    "The best way to predict the future is to create it.",
    "Every expert was once a beginner.",
    "Cloud computing is not just a technology, it's a mindset.",
    "Done is better than perfect.",
    "Keep learning, keep building."
]

@app.route('/')
def home():
    quote = random.choice(quotes)
    return f'''
    <h1> Daily Motivation </h1>
    <p style="font-size: 1.5rem;">"{quote}"</p>
    <p><a href="/">Get another quote</a></p>
    <hr>
    <small>Cloud Computing Lab | Deployed on Railway/Render</small>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)