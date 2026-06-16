import dados

def criarLivro(dadosForm):
    biblioteca = dados.carregar_do_arquivo()

    isbn = dadosForm["isbn"]
    titulo = dadosForm["titulo"]
    autor = dadosForm["autor"]
    genero = dadosForm["genero"]
    anoPublicacao = dadosForm["anoPublicacao"]
    editora = dadosForm["editora"]
    paginas = dadosForm["paginas"]
    status = dadosForm["status"]
    localizacao = dadosForm["localizacao"]

    for l in biblioteca:
        if(l["isbn"]==isbn):
            return print("Nao foi possivel cadastrar, o isbn ja existe!")

    livro = {
        "isbn": isbn,
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "ano_publicacao": anoPublicacao,
        "editora": editora,
        "paginas": paginas,
        "status": status,
        "localizacao": localizacao
    }

    biblioteca.append(livro)

    dados.salvar_no_arquivo(biblioteca)

    return print("Livro Registrado com sucesso!")


def alterarLivro(dadosForm):
    biblioteca = dados.carregar_do_arquivo()
    encontrado = False

    isbn = dadosForm["isbn"]
    titulo = dadosForm["titulo"]
    autor = dadosForm["autor"]
    genero = dadosForm["genero"]
    anoPublicacao = dadosForm["anoPublicacao"]
    editora = dadosForm["editora"]
    paginas = dadosForm["paginas"]
    status = dadosForm["status"]
    localizacao = dadosForm["localizacao"]

    for l in biblioteca:
        if(l["isbn"]==isbn):
            l["titulo"] = titulo
            l["autor"] = autor
            l["genero"] = genero
            l["anoPublicacao"] = anoPublicacao
            l["editora"] = editora
            l["paginas"] = paginas
            l["status"] = status
            l["localizacao"] = localizacao
            encontrado = True

    if(not encontrado):
        return print("Nao foi possivel encontrar um livro com esse isbn")

    dados.salvar_no_arquivo(biblioteca)

    return print("Alterado com sucesso!")






