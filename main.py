from pydoc import pager

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Ejercicio 1
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None

    if request.method == 'POST':
        nota1 = int(request.form['nota1'])
        nota2 = int(request.form['nota2'])
        nota3 = int(request.form['nota3'])
        asistencia = int(request.form['asistencia'])

        promedio = round( (nota1 + nota2 + nota3) / 3 )

        if promedio >= 40 and asistencia >= 75:
            estado = 'Aprobado'
        else:
            estado = 'Reprobado'

        resultado = {
            'promedio': promedio,
            'estado': estado
        }

    return render_template('ejercicio1.html', page_class="ejercicio ejercicio-1", resultado=resultado)

# Ejercicio 2
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    resultado = None

    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        nombres = [nombre1, nombre2, nombre3]
        nombre_largo = max(nombres, key=len)

        resultado = {
            'nombre': nombre_largo,
            'cantidad': len(nombre_largo)
        }

    return render_template('ejercicio2.html', page_class="ejercicio ejercicio-2",resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
