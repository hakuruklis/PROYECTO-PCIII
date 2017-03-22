from flask import Flask
from flask import render_template
from flask import request
from flask import make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/iniciar', methods=['POST'])
def iniciar():
    if request.method == 'POST':
        usuario = request.form['nombre']
        respuesta = make_response(render_template('pag1.html', u=usuario))
        return respuesta

if __name__ == "__main__":
    app.run()