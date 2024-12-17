from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simulando una base de datos con una lista de estudiantes
estudiantes = []

# Ruta principal (GET) para mostrar la lista de estudiantes
@app.route('/')
def index():
    return render_template('index.html', estudiantes=estudiantes)

# Ruta para registrar nuevos estudiantes (GET y POST)
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        edad = request.form.get('edad')
        email = request.form.get('email')
        estudiantes.append({'nombre': nombre, 'edad': edad, 'email': email})
        return redirect(url_for('index'))
    return render_template('registro.html')

# Ruta para eliminar un estudiante
@app.route('/eliminar/<int:id>')
def eliminar(id):
    if 0 <= id < len(estudiantes):
        estudiantes.pop(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, debug=True)
    3
    # hola
