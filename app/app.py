from flask import Flask, render_template, request, redirect, url_for, Blueprint
from flask_bootstrap import Bootstrap


import os

UPLOAD_FOLDER = os.path.abspath("../uploads_files")
# Asegúrate de que la carpeta 'uploads' exista o créala si no existe
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app = Flask(__name__)

Bootstrap(app)

ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png"}

blueprint_uploads = Blueprint(
    "uploads",
    __name__,
    static_folder=UPLOAD_FOLDER,
    static_url_path="/uploads_files",
)


app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.before_request
def before_request():
    # print("Antes de la petición")
    return


@app.after_request
def after_request(response):
    # print("Después de la petición")
    return response


@app.route("/")
def index():
    colores = ["rojo", "verde", "azul", "amarillo"]
    data = {
        "title": "Home",
        "bienvenida": "Bienvenido a mi sitio web",
        "colores": colores,
        "numero_colores": len(colores),
    }
    return render_template("index.html", data=data, files=UPLOAD_FOLDER)


@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return redirect(request.url)

    files = request.files.getlist("file")
    uploaded_files = []

    for file in files:
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            uploaded_files.append(app.config["UPLOAD_FOLDER"] + filename)
    print(uploaded_files)
    return render_template("index.html", uploaded_files=uploaded_files)


@app.route("/gallery")
def gallery():
    # requested_path = request.args.get("path")
    uploaded_files = os.listdir(app.config["UPLOAD_FOLDER"])
    print("archivos dento", uploaded_files)
    uploaded_paths = [
        os.path.join("../../../uploads_files", filename) for filename in uploaded_files
    ]
    print("paths", uploaded_paths)
    return render_template("gallery.html", uploaded_files=uploaded_paths)


@app.route("/traducir/<palabra>")
def traducir(palabra):
    traducciones = {
        "rojo": "red",
        "verde": "green",
        "azul": "blue",
        "amarillo": "yellow",
    }
    return render_template("traducir.html", palabra=palabra, data=traducciones[palabra])


def query_string():
    print(request)
    print(request.args)
    print(request.args.get("param1"))
    print(request.args.get("param2"))
    return "Ok"


def not_found(error):
    return render_template("404.html"), 404


# return redirect(url_for("index"))


if __name__ == "__main__":
    # app.add_url_rule("/gallery", view_func=gallery)
    app.register_error_handler(404, not_found)
    app.register_blueprint(blueprint_uploads)
    app.run(debug=True, port=5000)
