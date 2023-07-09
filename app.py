from flask import Flask, request, render_template


app = Flask(__name__)
links = [
    {"label": "Home", "url": "/home"},
    {"label": "About", "url": "/about"},
    {"label": "List", "url": "/list"}
]

app.debug = True

@app.route("/")
def index():
    return 'Hello, World!'
    # return render_template('index.html',navigation=links)
    # return render_template('test.html')


# @app.route("/home")
# def home():
#     return render_template('index.html',navigation = links)

# @app.route("/about")
# def about():
#     return render_template('about.html',navigation = links)

# @app.route("/list")
# def list():
    return render_template('table.html')

# @app.route("/contact", methods = ['GET','POST'])
# def contact():
#     if request.method == 'POST':
#         email = request.form.get('email')
#         comments = request.form.get('comments')


#     return render_template('Form.html')

# @app.route("/registration")
# def registration():
#     return

