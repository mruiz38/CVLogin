from flask import Flask, render_template, request
app= Flask(__name__)
#valor_nom="abc"
#varNombres="a"
@app.route("/")
def index():
    valor_nom="ValorPrueba"
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    return render_template("registrarCV2.html")
    #user_name = request.form.get("user_name")
    #if user_name =  "Juan":
    #return "exitos" + user_name

@app.route("/regresando", methods=["POST"])
def regresando():
    varNombres = request.form.get("varNombres")
    varApe1 = request.form.get("varApe1")
    varApe2 = request.form.get("varApe2")
    varFecNac = request.form.get("varFecNac")
    varEmail = request.form.get("varEmail")
    varNumCel= request.form.get("varNumCel")
    varDNI = request.form.get("varDNI")
    varDir = request.form.get("varDir")
    varCiu= request.form.get("varCiu")
    varResumen = request.form.get("varResumen")
    varExperiencia= request.form.get("varExperiencia")
    varEstudios =request.form.get("varEstudios")
    varLogros= request.form.get("varLogros")
    varHabilidades=request.form.get("varHabilidades")
    varintereses=request.form.get("varintereses")
    varreferencias=request.form.get("varreferencias") 
    return render_template("registrarCV2.html", 
    varNombres=varNombres,varApe1=varApe1, 
    varApe2=varApe2, varFecNac=varFecNac, varEmail=varEmail,
    varNumCel=varNumCel, varDNI=varDNI, varDir=varDir,
    varCiu=varCiu, varResumen=varResumen, varExperiencia=varExperiencia,
    varEstudios=varEstudios, varLogros=varLogros, varHabilidades=varHabilidades,
    varintereses=varintereses, varreferencias=varreferencias )
