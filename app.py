from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"
@app.route('/templates')
def index():
    return_template('index.html')
    
