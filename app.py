from flask import Flask, render_template
import random

app = Flask(__name__)

quotes = [
    "Push yourself, because no one else is going to do it for you.",
    "Great things never come from comfort zones.",
    "Dream it. Wish it. Do it.",
    "Success doesn’t just find you. You have to go out and get it."
]

@app.route('/')
def home():
    return render_template('index.html', quote=random.choice(quotes))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
