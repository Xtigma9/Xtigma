from flask import Flask, render_template

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Definir una ruta para la página principal
@app.route('/')
def home():
    return render_template('index.html')  # Aquí estamos usando un template

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
