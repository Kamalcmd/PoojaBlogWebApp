from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about_page():
    return render_template('about.html')


@app.route('/contact')
def contact_page():
    return render_template('contact.html')


@app.route('/blog')
def blog():
    return render_template('blog.html')    



app.run(debug=True, port=8000, host='127.0.0.1')
