from flask import Flask, request, render_template


app = Flask(__name__)
links = [
    {"label": "Home", "url": "/home"},
    {"label": "About", "url": "/about"},
    {"label": "List", "url": "/list"}
]


@app.route("/")
def index():
    return 'Hello, World!'
    # return render_template('index.html',navigation=links)

@app.route("/home")
def home():
    return render_template('home.html',navigation = links)

@app.route("/about")
def about():
    return render_template('about.html',navigation = links)



