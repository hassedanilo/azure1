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
def ventures():
  return render_template('ventures.html')

@app.route('/contatos')
def contatos():
  return render_template('contatos.html')

@app.route('/home')
def home():
  return render_template('home.html')

@app.route('/contato')
def contato():
  return render_template('contato.html')

@app.route('/usuarios')
def usuarios():
  return render_template('usuarios.html', lista_usuarios=lista_usuarios)

if __name__ == "__main__":
 app.run(debug=True)
