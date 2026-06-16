from flask import Flask,request,render_template,redirect
import dados
from operacoes import criarLivro,alterarLivro

biblioteca = dados.carregar_do_arquivo()

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
def updateBiblioteca():
    global biblioteca
    biblioteca = dados.carregar_do_arquivo()


@app.route('/')
def home():
    return redirect('/biblioteca')

@app.route('/biblioteca/', methods=['GET'])
def listarLivros():
    return render_template("biblioteca.html", livros=biblioteca)

@app.route("/biblioteca/registro")
def formularioRegistrarLivro():
    return render_template("registarLivro.html")
@app.route("/biblioteca/registro/executar", methods=["POST"])
def executarRegistroLivro():
    criarLivro(request.form)
    return redirect("/biblioteca")


@app.route("/biblioteca/alterar")
def formularioAlterarLivro():
    return render_template("alterarLivro.html")

@app.route("/biblioteca/alterar/executar", methods=["POST"])
def executarAlteracaoLivro():
    alterarLivro(request.form)
    return redirect("/biblioteca")






if __name__ == '__main__':
    app.run(debug=True, port=5000)
