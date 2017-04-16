from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
from flask import session

app = Flask(__name__)

app.secret_key = 'F12Zr47j\3yX R~X@H!jmM]Lwf/,?KT'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/iniciarTest', methods=['POST'])
def iniciar():
    if request.method == 'POST':
        session['name'] = request.form['yourname']
        respuesta = make_response(render_template('pag1.html'))
        return respuesta

@app.route('/escogerCarrera', methods=['POST'])
def test1():
    carreras=[]
    pregunta1 = request.form['pregunta1']
    pregunta2 = request.form['pregunta2']
    pregunta3 = request.form['pregunta3']
    pregunta4 = request.form['pregunta4']
    pregunta5 = request.form['pregunta5']
    pregunta6 = request.form['pregunta6']
    pregunta7 = request.form['pregunta7']
    pregunta8 = request.form['pregunta8']
    pregunta9 = request.form['pregunta9']
    pregunta10 = request.form['pregunta10']
    pregunta11 = request.form['pregunta11']
    pregunta12 = request.form['pregunta12']
    pregunta13 = request.form['pregunta13']
    pregunta14 = request.form['pregunta14']
    pregunta15 = request.form['pregunta15']
    pregunta16 = request.form['pregunta16']
    pregunta17 = request.form['pregunta17']
    pregunta18 = request.form['pregunta18']
    pregunta19 = request.form['pregunta19']
    pregunta20 = request.form['pregunta20']
    pregunta21 = request.form['pregunta21']
    pregunta22 = request.form['pregunta22']
    pregunta23 = request.form['pregunta23']
    pregunta24 = request.form['pregunta24']
    pregunta25 = request.form['pregunta25']
    if (pregunta1 == "si" and pregunta4 == "si") or (pregunta1 == "si" and pregunta18 == "si") or (pregunta4 == "si" and pregunta18 == "si"):
        carrera='Comunicacion y disenio'
        carreras.append(carrera)
    if (pregunta2 == "si" and pregunta5 == "si") or (pregunta2 == "si" and pregunta14 == "si") or (pregunta5 == "si" and pregunta14 == "si"):
        carrera = 'Ciencias Administrativas'
        carreras.append(carrera)
    if (pregunta7 == "si" and pregunta10 == "si") or (pregunta7 == "si" and pregunta15 == "si") or (pregunta10 == "si" and pregunta15 == "si"):
        carrera = 'Ingenieria y sistemas'
        carreras.append(carrera)
    if (pregunta9 == "si" and pregunta11 == "si") or (pregunta9 == "si" and pregunta21 == "si") or (pregunta11 == "si" and pregunta21 == "si"):
        carrera = 'Ciencias de la salud'
        carreras.append(carrera)
    if (pregunta6 == "si" and pregunta12 == "si") or (pregunta6 == "si" and pregunta16 == "si") or (pregunta12 == "si" and pregunta16 == "si"):
        carrera = 'Arquitectura'
        carreras.append(carrera)
    if (pregunta13 == "si" and pregunta17 == "si") or (pregunta13 == "si" and pregunta20 == "si") or (pregunta17 == "si" and pregunta20 == "si"):
        carrera = 'Derecho y ciencias politicas'
        carreras.append(carrera)
    if (pregunta3 == "si" and pregunta8 == "si") or (pregunta3 == "si" and pregunta19 == "si") or (pregunta3 == "si" and pregunta22 == "si") or (pregunta8 == "si" and pregunta19 == "si") or (pregunta8== "si" and pregunta22 == "si") or (pregunta19 == "si" and pregunta22 == "si"):
        carrera = 'Hotelería, Gastronomía y Turismo'
        carreras.append(carrera)
    if (pregunta23 == "si" and pregunta24 == "si") or (pregunta23 == "si" and pregunta25 == "si") or (pregunta24 == "si" and pregunta24 == "si"):
        carrera = 'Logistica Maritma y portuaria'
        carreras.append(carrera)
    respuesta = make_response(render_template('pag2.html', c=carreras))
    return respuesta

@app.route('/SeleccionarFacultad', methods=['POST'])
def test2():
   facultad_final=request.form['pregunta']
   if facultad_final == 'Comunicacion y disenio':
       respuesta=make_response(render_template('comunicacion.html',facul=facultad_final))
       return respuesta
   elif facultad_final == 'Ciencias Administrativas':
       respuesta = make_response(render_template('Ciencias Administrativas.html', facul=facultad_final))
       return respuesta
   elif facultad_final == 'Ingenieria y sistemas':
       respuesta = make_response(render_template('Sistemas.html', facul=facultad_final))
       return respuesta
   elif facultad_final == 'Ciencias de la salud':
       respuesta = make_response(render_template('comunicacion.html', facul=facultad_final))
       return respuesta
   elif facultad_final == 'Arquitectura':
       respuesta = make_response(render_template('Arquitectura.html', facul=facultad_final))
       return respuesta
   elif facultad_final == 'Derecho y ciencias politicas':
       respuesta = make_response(render_template('Derechos y ciencias politicas.html', facul=facultad_final))
       return respuesta
   elif facultad_final == 'Hotelería, Gastronomía y Turismo':
       respuesta = make_response(render_template('HGT.html', facul=facultad_final))
       return respuesta
   elif facultad_final == 'Logistica Maritma y portuaria':
       respuesta = make_response(render_template('Logística, Marítima y Portuaria.html', facul=facultad_final))
       return respuesta

@app.route('/Comunicacion', methods=['POST'])
def Comunicacion():
    pregunta1 = request.form['pregunta1']
    pregunta2 = request.form['pregunta2']
    pregunta3 = request.form['pregunta3']
    pregunta4 = request.form['pregunta4']
    carreras=[]
    if pregunta1 == "si":
        carrera='Lic. en Diseño Gráfico '
        carreras.append(carrera)
    if pregunta2 == "si":
        carrera = 'Lic. en Diseño Gráfico con énfasis en Publicidad y Mercadeo'
        carreras.append(carrera)
    if pregunta3 == "si":
        carrera = 'Lic. en Com. Audiovisual con énfasis en Producción de Radio y TV'
        carreras.append(carrera)
    if pregunta4 == "si":
        carrera = 'Lic. en Publicidad y Mercadeo con énfasis en Imagen Corporativa '
        carreras.append(carrera)
    respuesta = make_response(render_template('Carrera Final.html', c=carreras))
    return respuesta

@app.route('/Arquitectura', methods=['POST'])
def Arquitectura():
    pregunta1 = request.form['pregunta1']
    pregunta2 = request.form['pregunta2']
    pregunta3 = request.form['pregunta3']
    pregunta4 = request.form['pregunta4']
    carreras=[]
    if pregunta1 == "si" and pregunta3 == "si":
        carrera='Licenciatura en Arquitectura'
        carreras.append(carrera)
    if pregunta2 == "si" and pregunta4 == "si":
        carrera = 'Licenciatura en Diseño de Interiores'
        carreras.append(carrera)
    respuesta = make_response(render_template('Carrera Final.html', c=carreras))
    return respuesta

@app.route('/Hotelería,GastronomíayTurismo', methods=['POST'])
def HoteleríaGastronomíayTurismo():
    pregunta1 = request.form['pregunta1']
    pregunta2 = request.form['pregunta2']
    pregunta3 = request.form['pregunta3']
    carreras=[]
    if pregunta1 == "si":
        carrera='Lic. Internacional en Administración de Empresas Hoteleras'
        carreras.append(carrera)
    if pregunta2 == "si":
        carrera = 'Lic. Internacional en Administración de Empresas Turísticas'
        carreras.append(carrera)
    if pregunta3 == "si":
        carrera = 'Lic. Internacional en Artes Culinarias '
        carreras.append(carrera)
    respuesta = make_response(render_template('Carrera Final.html', c=carreras))
    return respuesta

@app.route('/Derechosycienciaspoliticas', methods=['POST'])
def Derechosycienciaspoliticas():
    pregunta1 = request.form['pregunta1']
    pregunta2 = request.form['pregunta2']
    carreras=[]
    if pregunta1 == "si":
        carrera='Lic. en Derecho y Ciencias Políticas '
        carreras.append(carrera)
    if pregunta2 == "si":
        carrera = 'Lic. en Criminología'
        carreras.append(carrera)
    respuesta = make_response(render_template('Carrera Final.html', c=carreras))
    return respuesta

@app.route('/CienciasAdministraciones', methods=['POST'])
def CienciasAdministraciones():
    carreras=[]
    pregunta1 = request.form['pregunta1']
    pregunta2 = request.form['pregunta2']
    pregunta3 = request.form['pregunta3']
    pregunta4 = request.form['pregunta4']
    pregunta5 = request.form['pregunta5']
    pregunta6 = request.form['pregunta6']
    pregunta7 = request.form['pregunta7']
    pregunta8 = request.form['pregunta8']
    pregunta9 = request.form['pregunta9']
    pregunta10 = request.form['pregunta10']
    pregunta11 = request.form['pregunta11']
    if pregunta1 == "si":
        carrera='Lic. en Administración de Negocios'
        carreras.append(carrera)
    if pregunta2 == "si":
        carrera= 'Lic. en Contabilidad '
        carreras.append(carrera)
    if pregunta3 == "si":
        carrera='Lic. en Administración de Recursos Humanos '
        carreras.append(carrera)
    if pregunta4 == "si":
        carrera ='Lic. en Banca y Finanzas '
        carreras.append(carrera)
    if pregunta5 == "si":
        carrera='Lic. en Comercio Internacional '
        carreras.append(carrera)
    if pregunta6 == "si":
        carrera = 'Lic. en Negocios Internacionales '
        carreras.append(carrera)
    if pregunta7 == "si":
        carrera='Lic. en Ingeniería Comercial Lic. en Comportamiento Organizacional y Desarrollo Humano '
        carreras.append(carrera)
    if pregunta8 == "si":
        carrera = 'Lic. en Global Business '
        carreras.append(carrera)
    if pregunta9 == "si":
        carrera='Lic. en Administración de Empresas Turísticas'
        carreras.append(carrera)
    if pregunta10 == "si":
        carrera = 'Lic. en Mercadeo y Publicidad'
        carreras.append(carrera)
    if pregunta11 == "si":
        carrera='Lic. en Mercadeo y Ventas'
        carreras.append(carrera)
    respuesta = make_response(render_template('Carrera Final.html', c=carreras))
    return respuesta

# @app.route('/LMP', methods=['POST'])
# def LMP():
#     pregunta1 = request.form['pregunta1']
#     pregunta2 = request.form['pregunta2']
#     pregunta3 = request.form['pregunta3']
#     pregunta4 = request.form['pregunta4']
#     carreras=[]
#     if pregunta1 == "si":
#         carrera='1.	Lic. en Administración Marítima y Portuaria '
#         carreras.append(carrera)
#     if pregunta2 == "si":
#         carrera= '2. Lic. en Contabilidad '
#         carreras.append(carrera)
#     if pregunta3 == "si":
#         carrera='3.	Lic. en Administración de Recursos Humanos '
#         carreras.append(carrera)
#     if pregunta4 == "si":
#         carrera ='4. Lic. en Banca y Finanzas '
#         carreras.append(carrera)

@app.route('/Ingenieria', methods=['POST'])
def ingenieria():
    carreras = []
    pregunta1 = request.form['pregunta1']
    pregunta2 = request.form['pregunta2']
    pregunta3 = request.form['pregunta3']
    pregunta4 = request.form['pregunta4']
    pregunta5 = request.form['pregunta5']
    pregunta6 = request.form['pregunta6']
    pregunta7 = request.form['pregunta7']
    if pregunta1 == "si":
        carrera = 'Lic. en Ing. de Redes y Datos con énfasis en Sistemas Inalámbricos '
        carreras.append(carrera)
    if pregunta2 == "si":
        carrera = 'Lic. en Ingeniería en Sistemas Computacionales '
        carreras.append(carrera)
    if pregunta3 == "si":
        carrera = 'Lic. en Ingeniería en Electrónica y Comunicaciones '
        carreras.append(carrera)
    if pregunta4 == "si":
        carrera = 'Lic. en Ingeniería en Industrial con énfasis en Gestión de Calidad'
        carreras.append(carrera)
    if pregunta5 == "si":
        carrera = 'Lic. en Ingeniería en Industrial con énfasis en Gestión de Operaciones '
        carreras.append(carrera)
    if pregunta6 == "si":
        carrera = 'Lic. en Ingeniería Industrial y de Sistemas '
        carreras.append(carrera)
    if pregunta7 == "si":
        carrera = 'Lic. en Sistemas Comp. con énfasis en Desarrollo de Sistemas Avanzados de Redes y Software '
        carreras.append(carrera)
    respuesta = make_response(render_template('Carrera Final.html', c=carreras))
    return respuesta


if __name__ == "__main__":
    app.run(debug=True)
