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
    
    edunatal = pd.read_csv('edunatal1.csv')
    edunatal.head()
    edunatal = edunatal.drop(columns=['Unnamed: 0', 'Type'])
    edunatal.rename(columns={'NAME':'Name', 'GEOCODE_INPUT':'Geocode_Input', 'LAT':'Lat', 'LNG':'Lng'}, inplace=True)
    edunatal.head()

    pattern = r"[Cc][Mm][Ee][Ii]"
    edunatal = edunatal[edunatal['Name'].str.contains(pattern)]
    edunatal.dropna(inplace=True)
   
    edunatal.head()

    lat = edunatal.Lat.tolist()
    lng = edunatal.Lng.tolist()
    folium_map = folium.Map(
    location=[-27.5971027, -48.5580055],
    tiles='cartodbdark_matter',
    zoom_start=5
)
   
    HeatMap(list(zip(lat, lng))).add_to(folium_map)

    
    return folium_map._repr_html_()

@app.route('/mapa-arq')
def mapa_arq():
    return render_template('my_map1.html')
  
@app.route('/mapa-arq2')
def mapa_arq2():
    return render_template('my_map2.html')


if __name__ == "__main__":
 app.run(debug=True)
