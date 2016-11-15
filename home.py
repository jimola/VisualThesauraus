from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def render_main():
    return render_template('home.html')
