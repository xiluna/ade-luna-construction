from flask import Flask, app, render_template
from flask_mail import Mail

app = Flask(__name__)
mail = Mail(app)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
