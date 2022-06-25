from flask import Flask, render_template, request
import os


app = Flask(__name__)

@app.route("/registro", methods = ["GET"])
def paginaLogin():
    return render_template("index.html")

@app.route("/registrado", methods = ["POST"])
def registro():
    login = request.form["login"]
    senha = request.form["senha"]
    email = request.form["email"]
    if not login or not senha or not email or os.path.exists(f"{login} {senha}.txt") == True or os.path.exists(f"{email}.txt") == True:
        return render_template("erro.html")
    arquivo = open(f"{login} {senha}.txt", "a+")
    arquivo2 = open(f"{email}.txt", "a+")
    arquivo.write("{}\n".format(login))
    arquivo.write("{}\n".format(senha))
    arquivo2.write("{}\n".format(email))
    arquivo.close()
    arquivo2.close()
    return render_template("registrado.html", login = login)
@app.route("/login", methods = ["GET"])
def login():
    return render_template("login.html")

@app.route("/logado", methods = ["POST"])
def logado():
    login = request.form["login"]
    senha = request.form["senha"]
    if os.path.exists(f"{login} {senha}.txt") == False:
        return render_template("erro.html")
    return render_template("home.html", login = login)

@app.route("/excluir", methods = ["GET"])
def excluir():
    return render_template("excluir.html")

@app.route("/excluido", methods = ["POST"])
def excluido():
    login = request.form["login"]
    senha = request.form["senha"]
    email = request.form["email"]
    if os.path.exists(f"{login} {senha}.txt") == False or os.path.exists(f"{email}.txt") == False:
        return "Erro!, usuario ou senha ou email não existentes! Tente novamente!"

    os.remove(f"{login} {senha}.txt")
    os.remove(f"{email}.txt")

    return "Removido!"

@app.route("/trocarsenha", methods = ["GET"])
def trocarsenha():
    return render_template("trocarsenha.html")

@app.route("/trocado", methods = ["POST"])
def trocado():
    login = request.form["login"]
    senha = request.form["senha"]
    novasenha = request.form["novasenha"]
    confirmarsenha = request.form["confirmarsenha"]

    if os.path.exists(f"{login} {senha}.txt") == False or novasenha != confirmarsenha:
        return "Erro! usuario ou senha ou nova senha invalidos! Tente novamente!"

    os.remove(f"{login} {senha}.txt")
    open(f"{login} {confirmarsenha}.txt", "a+")
    return "Trocado!"

app.run()
