from flask import Flask, request, redirect, make_response

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
    <h1>Inicio</h1>
    <ul>
        <li><a href="/set_cookie">Crear cookie</a></li>
        <li><a href="/get_cookie">Leer cookie</a></li>
        <li><a href="/del_cookie">Borrar cookie</a></li>
    </ul>
    """

@app.route("/set_cookie")
def set_cookie():
    resp = make_response(redirect("/"))
    resp.set_cookie("cookie_name", "Tenemos una cookie")
    return resp

@app.route("/get_cookie")
def get_cookie():
    dato = request.cookies.get("cookie_name")
    if dato:
        return f"Cookie encontrada: {dato}"
    return "No hay cookie"

@app.route("/del_cookie")
def del_cookie():
    resp = make_response(redirect("/"))
    resp.set_cookie("cookie_name", "", expires=0)
    return resp

if __name__ == "__main__":
    app.run(debug=True)
