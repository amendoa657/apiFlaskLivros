from flask import Flask,request,render_template
import dados

biblioteca = dados.carregar_do_arquivo()

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/', methods=['GET'])
def home():  # put application's code here
    return "hello world"

@app.route('/biblioteca', methods=['GET'])
def listarLivros():
    return render_template("mostrarBiblioteca.html", livros=biblioteca)

@app.route('/biblioteca/<isbn>')
def pesquisar(isbn=None):
    if isbn:
        resultados = [l for l in biblioteca if isbn == l['isbn']]
        if resultados:
            return resultados
        else:
            return "Nenhum livro encontrado"
    else:
        return "Solicitacao Invalida"


@app.route("/biblioteca/create")
def criarLivro():
    #novoLivro = request.get_json()
    #biblioteca.append(novoLivro)
    #dados.salvarNoArquivo(biblioteca)
    return render_template("criarLivro.html")

@app.route("/biblioteca/delete/<isbn>", methods=['DELETE'])
def deleterLivro(isbn=None):
    if isbn:
        for l in biblioteca:
            if isbn==l['isbn']:
                biblioteca.remove(l)
                dados.salvarNoArquivo(biblioteca)
                return "livro apagado"
            else:
                return "nenhum livro encontrado"
    else:
        return "solicitacao invalida"





if __name__ == '__main__':
    app.run(debug=True, port=5000)
