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
    if pregunta1 == "si" and pregunta4 == "si" and pregunta18 == "si":
        carrera='Comunicacion y disenio'
        carreras.append(carrera)
    if pregunta2 == "si" and pregunta5 == "si" and pregunta14 == "si":
        carrera = 'Ciencias Administrativas'
        carreras.append(carrera)
    if pregunta7 == "si" and pregunta10 == "si" and pregunta15 == "si":
        carrera = 'Ingenieria y sistemas'
        carreras.append(carrera)
    if pregunta9 == "si" and pregunta11 == "si" and pregunta21 == "si":
        carrera = 'Ciencias de la salud'
        carreras.append(carrera)
    if pregunta6 == "si" and pregunta12 == "si" and pregunta16 == "si":
        carrera = 'Arquitectura'
        carreras.append(carrera)
    if pregunta13 == "si" and pregunta17 == "si" and pregunta20 == "si":
        carrera = 'Derecho y ciencias politicas'
        carreras.append(carrera)
    if pregunta3 == "si" and pregunta8 == "si" and pregunta19 == "si" and pregunta22 == 'si':
        carrera = 'Hotelería, Gastronomía y Turismo'
        carreras.append(carrera)
    if pregunta23 == "si" and pregunta24 == "si" and pregunta25 == "si":
        carrera = 'Logistica Maritma y portuaria'
        carreras.append(carrera)
    cantidad=len(carreras)

    respuesta = make_response(render_template('pag2.html', c=carreras, t=cantidad))
    return respuesta

@app.route('/SeleccionarFacultad', methods=['POST'])
def test2():
   facultad_final=request.form['pregunta']
   if facultad_final == 'Comunicacion y disenio':
       return render_template('pag3.html',facul=facultad_final)
   elif facultad_final == 'Ciencias Administrativas':
       return render_template()
   elif facultad_final == 'Ingenieria y sistemas':
       return render_template()
   elif facultad_final == 'Ciencias de la salud':
       return render_template()
   elif facultad_final == 'Arquitectura':
       return render_template()
   elif facultad_final == 'Derecho y ciencias politicas':
       return render_template()
   elif facultad_final == 'Hotelería, Gastronomía y Turismo':
       return render_template()
   elif facultad_final == 'Logistica Maritma y portuaria':
       return render_template()



if __name__ == "__main__":
    app.run(debug=True)
