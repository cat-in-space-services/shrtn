from flask import Flask, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv
from os import getenv, path
from random import choices
from string import ascii_lowercase

app = Flask(__name__)
load_dotenv()
#secret key for flash messages
app.secret_key  = getenv("SECRET_KEY")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/new", methods=["POST"])
def new():
    url = request.form["url"]
    slug = request.form["slug"]
    if path.exists("links.txt") != True:
        open("links.txt", "w")
    if slug == "":
        slug = ''.join(choices(ascii_lowercase, k=5))
    else:
        if slug.isalnum() != True:
            flash("Slug must be composed only of letters and numbers", "danger")
            return redirect(url_for("index"))
        with open("links.txt", "r") as f:
            for line in f:
                if line.split("+")[0] == slug:
                    flash("Slug already in use", "danger")
                    return redirect(url_for("index"))

    
    with open("links.txt", "a") as f:
        f.write(f"{slug}+{url}\n")
    flash(f"<strong>Your link has been shortened!<strong> <code>{ getenv('BASE_URL') }/s/{ slug }</code>", "success")
    return redirect(url_for("index"))

@app.route("/s/<slugReq>")
def s(slugReq):
    with open("links.txt", "r") as f:
        for line in f:
            crtslug = line.split("+")[0].replace("\n", "")
            print(crtslug + " " + slugReq)
            if crtslug == slugReq:
                return redirect(line.split("+")[1].replace("\n", ""))
    flash("Slug not found", "danger")
    return redirect(url_for("index"))

        

if __name__ == "__main__":
    app.run()
