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
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Daily Motivation</title>
      <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
          font-family: sans-serif;
          min-height: 100vh;
          display: flex;
          align-items: center;
          justify-content: center;
          background: #f5f4ff;
        }}
        .card {{
          background: white;
          border-radius: 16px;
          padding: 2.5rem 2rem;
          max-width: 560px;
          width: 90%;
          text-align: center;
          box-shadow: 0 4px 24px rgba(83,74,183,0.10);
        }}
        h1 {{
          font-size: 1.6rem;
          font-weight: 600;
          color: #2d2a5e;
          margin-bottom: 1.5rem;
        }}
        .quote-box {{
          border-left: 4px solid #7F77DD;
          background: #EEEDFE;
          border-radius: 0 10px 10px 0;
          padding: 1rem 1.25rem;
          margin-bottom: 1.5rem;
          text-align: left;
        }}
        .quote-box p {{
          font-size: 1.1rem;
          color: #3C3489;
          font-style: italic;
          line-height: 1.7;
        }}
        .btn {{
          display: inline-block;
          padding: 10px 28px;
          background: #534AB7;
          color: white;
          border-radius: 8px;
          text-decoration: none;
          font-size: 0.95rem;
          font-weight: 500;
          transition: background 0.2s;
        }}
        .btn:hover {{ background: #3C3489; }}
        footer {{
          margin-top: 2rem;
          font-size: 0.78rem;
          color: #aaa;
        }}
      </style>
    </head>
    <body>
      <div class="card">
        <h1> Daily Motivation</h1>
        <div class="quote-box">
          <p>"{quote}"</p>
        </div>
        <a class="btn" href="/">Get another quote</a>
        <footer>Cloud Computing Lab &nbsp;·&nbsp; Deployed on Render</footer>
      </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)