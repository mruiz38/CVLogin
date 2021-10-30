from flask import Flask, render_template, request
app= Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    user_name = request.form.get("user_name")
    #if user_name =  "Juan":
    return "exitos" + user_name

