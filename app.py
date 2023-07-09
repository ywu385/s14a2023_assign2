from flask import Flask, request, render_template, redirect
import json


app = Flask(__name__)
links = [
    {"label": "Home", "url": "/home"},
    {"label": "About", "url": "/about"},
    {"label": "List", "url": "/list"}
]

app.debug = True

@app.route("/")
def index():
    # return 'Hello, World!'
    return render_template('index.html',navigation=links, header='Home')
    # return render_template('test.html')


@app.route("/home")
def home():
    return render_template('index.html',navigation = links, header='Home')

@app.route("/about")
def about():
    return render_template('about.html',navigation = links, header='About')

@app.route("/list")
def list():
    with open('data/comment_table.json','r') as f:
        data = json.load(f)
    return render_template('table.html',data = data, header = 'Who has been here?')

@app.route('/success')
def success():
    return render_template('success.html',header='Success!')

@app.route("/contact", methods = ['GET','POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        comments = request.form.get('comments')

        data = {'name':name,
                'email':email,
                'comments':comments}
        
        # Adding data into JSON file
        with open('data/comment_table.json', 'a+') as f:
            f.seek(0)
            try:
                old_data = json.load(f)
            except ValueError:
                old_data = []

            # old_data.append(data)
            f.seek(0)
            json.dump(data,f)

        return redirect('/success')
    
    return render_template('Form.html', header='Post Your Comments')

# @app.route("/registration")
# def registration():
#     return

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
