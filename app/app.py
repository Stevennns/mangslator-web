from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    send_from_directory,
    Blueprint,
)
from flask_bootstrap import Bootstrap
import requests
import shutil

import os

# Especifica la ruta absoluta al directorio 'uploads_files'
UPLOAD_FOLDER = '/home/grupo3/app/uploads_files'
RESULT_FOLDER = '/home/grupo3/app/mangslator-results'
# Crea el directorio si no existe
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

API_URL = "http://gate.dcc.uchile.cl:8633/mangslator-ia/process2"
#API_URL = "http://127.0.0.1:5003/process2"
print(os.path.abspath(UPLOAD_FOLDER))
print(os.path.abspath(RESULT_FOLDER))

app = Flask(__name__)

Bootstrap(app)

ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png"}

blueprint_uploads = Blueprint(
    "uploads",
    __name__,
    static_folder=UPLOAD_FOLDER,
    static_url_path="/uploads_files",
)
blueprint_results = Blueprint(
    "results",
    __name__,
    static_folder=RESULT_FOLDER,
    static_url_path="/mangslator-results",
)


app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/mangslator-results/<filename>")
def serve_image(filename):
    return send_from_directory(RESULT_FOLDER, filename)


@app.route("/uploads_files/<filename>")
def serve_image2(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


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
    print(UPLOAD_FOLDER)
    return render_template("index.html", data=data, files=UPLOAD_FOLDER)


@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return redirect(request.url)

    files = request.files.getlist("file")
    uploaded_files = []
    if os.path.exists(UPLOAD_FOLDER):
        # Si existe, elimina su contenido
        shutil.rmtree(UPLOAD_FOLDER)

    # Crea el directorio
    os.makedirs(UPLOAD_FOLDER)
    for file in files:
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            uploaded_files.append(app.config["UPLOAD_FOLDER"] + filename)

    uploaded_imgs = os.listdir(UPLOAD_FOLDER)
    uploaded_paths = [
        url_for("serve_image2", filename=filename) for filename in uploaded_imgs
    ]
    #print("paths", uploaded_paths)

    return render_template(
        "index.html", uploaded_files=uploaded_files, imagenes=uploaded_paths
    )


@app.route("/gallery")
def gallery():
    # requested_path = request.args.get("path")
    apicall = requests.post(API_URL)

    if apicall.status_code == 200:
        print("API call success")
        uploaded_files = os.listdir(app.config["UPLOAD_FOLDER"])
        print("archivos dento (llamado api)", uploaded_files)
        uploaded_paths = [
            url_for("serve_image", filename=filename) for filename in uploaded_files
        ]
        print("paths de la api", uploaded_paths)
        return render_template("gallery.html", uploaded_files=uploaded_paths)
    else:
        print("API call failed")
        return render_template("index.html")


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

# var = 'D:\Universidad\\2023-2\\Proyecto_de_IA\\mangslator-results\\011.jpg'
if __name__ == "__main__":
    # app.add_url_rule("/gallery", view_func=gallery)
    #app.register_error_handler(404, not_found)
    app.register_blueprint(blueprint_uploads)
    app.register_blueprint(blueprint_results)
    app.run(debug=True, port=5003)
