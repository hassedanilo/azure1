from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def index():
  return render_template('index.html')

@app.route('/teste')
def teste():
  return render_template('teste.html')

@app.route('/servicos')
def servicos():
  return render_template('servicos.html')

@app.route('/inventure')
def inventure():
  return render_template('inventure.html')

@app.route('/ventures')
def venture():
  return render_template('ventures.html')

if __name__ == "__main__":
 app.run()
