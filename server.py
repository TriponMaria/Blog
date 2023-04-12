from flask import Flask, render_template
import os
import requests

API_URL = os.environ['API_URL']

app = Flask(__name__)
response = requests.get(API_URL)
all_posts = response.json()


@app.route('/')
def home():
    return render_template('index.html', posts=all_posts)


@app.route(f'/post/<id>')
def article(id):
    return render_template(f'article.html', posts=all_posts, id_post=int(id))


if __name__ == "__main__":
    app.run(debug=True)
