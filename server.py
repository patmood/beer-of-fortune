from flask import Flask, url_for, render_template
from os.path import abspath, dirname
app = Flask(__name__)
app.root_path = abspath(dirname(__file__))

@app.route('/')
def hello_world():
    return render_template('index')
