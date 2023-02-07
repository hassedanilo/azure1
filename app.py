from flask import Flask, render_template

import folium

app = Flask(__name__)

lista_usuarios = ['Lira', 'Danilo', 'Alon', 'Fernanda']

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

m = folium.Map(location=[-27.695489, -48.465843], zoom_start=15)

m.save('templates/my_map2.html')

@app.route('/mapa')
def mapa():
    start_coords = (-27.695489, -48.465843)
    folium_map = folium.Map(location=start_coords, zoom_start=14)
    return folium_map._repr_html_()

@app.route('/mapa-arq2')
def mapa_arq():
    return render_template('my_map2.html')


if __name__ == "__main__":
 app.run(debug=True)
