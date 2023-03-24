from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = "llave super secreta" #Establecemos una clave secreta para dar más seguridad a lo que guardamos en sesión

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/proceso', methods=['POST'])
def proceso():
    
    #Guardamos en sesión
    session['user_name'] = request.form['nombre']
    session['tipo_usuario'] = request.form['tipo_usuario']

    #Cuando nosotros obtenemos una solicitud POST REDIRIGIMOS
    return redirect('/exito')

@app.route('/exito')
def exito():
    return render_template('exito.html')
    

if __name__ == "__main__":
    app.run(debug=True)