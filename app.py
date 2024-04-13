from flask import Flask, redirect, render_template, request, session
from flask_session import Session
import requests

app = Flask(__name__)
app.secret_key = 'hello'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

API_URL = "https://api.jikan.moe/v4/"

def MANGA_BY_NAME(user_name):
    name = user_name.replace(' ', '+')
    URL = API_URL  + "manga?q=" + name + "&type=manga"
    data = requests.get(URL)
    manga_data = data.json()
    return manga_data

def MANGA_BY_ID(id):
    URL = API_URL  + "manga/" + id
    data = requests.get(URL)
    manga_data = data.json()
    return manga_data

def MANGA_REC():
    URL = API_URL  + "top" + "/manga"
    data = requests.get(URL)
    manga_data = data.json()
    return manga_data

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        if "list" not in session:
            session["list"] = []
        id = request.form.get("manga_id")
        id_to_remove = request.form.get("manga_id_remove")
        if id and id not in session['list']:
            session["list"].append(id)
            session.modified = True
        if id_to_remove:
            session['list'].remove(id_to_remove)
            session.modified = True
        return redirect("/")

    if request.method == "GET":
        mangas = []
        if "list" in session:
            manga_list = session["list"]
            for manga in manga_list:
                information = MANGA_BY_ID(manga)
                mangas.append(information)
        else:
            mangas = []
    return render_template("index.html", mangas = mangas)

@app.route("/genre", methods=["GET", "POST"])
def genre():
    if request.method == "GET":
        return render_template("top.html")
    elif request.method == "POST":
        info = MANGA_REC()
        if not info:
            return render_template("apology.html")
        return render_template("info.html", info=info)


@app.route("/title", methods=["GET", "POST"])
def title():
    if request.method == "GET":
        return render_template("title.html")
    elif request.method == "POST":
        title = request.form.get("title")
        if not title:
            return render_template("apology.html")
        info = MANGA_BY_NAME(title)
        if not info:
            return render_template("apology.html")
        return render_template("info.html", info=info)








