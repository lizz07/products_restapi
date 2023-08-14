from flask import Flask, request

app=Flask(__name__)
@app.route("/")
def home():
    app.logger.info(f'solicitud en la ruta {request.path}')
    return "<p>Hola mundo bienvenidos a flask</p>"

@app.route("/saludar/<nombre>")
def saludar(nombre):
    app.logger.info(f'solicitud en la ruta {request.path}')
    return f"Hola {nombre}"

@app.route("/edad/<int:edad>")
def edad(edad):
    app.logger.info(f'solicitud en la ruta {request.path}')
    return f"Tu edad es {edad}"

@app.get("/api/user/<user>")
def user(user):
    valores={'user':user}
    return valores