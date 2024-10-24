from flask import Flask

#Creamos app mediante una instancia
app = Flask(__name__)

#Creamos rutas con sus correspondientes funciones
@app.route('/')
def holamundo():
    return 'Hola Mundo!!!'

#Creamos otra ruta con su correspondiente función
@app.route('/misProyectos')
def mostrarProyectos():
    return 'Aquí aparecen los Proyectos'

#Ejecutamos la app al ejecutar este archivo
if __name__ == '__main__':
    app.run(debug=True)