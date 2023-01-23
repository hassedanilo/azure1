from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')

def hello():
    return_template('index.html')

@app.route('/templates')

def index():
    return_template('index.html')
    
