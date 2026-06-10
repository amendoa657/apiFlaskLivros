import json
import os

PASTA = "arquivos"
CAMINHO_ARQUIVO = os.path.join(PASTA, "biblioteca.json")


def inicializar_diretorio():
    if not os.path.exists(PASTA):
        os.makedirs(PASTA)


def salvar_no_arquivo(lista_dados):
    inicializar_diretorio()
    with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(lista_dados, f, ensure_ascii=False, indent=4)


def carregar_do_arquivo():
    if os.path.exists(CAMINHO_ARQUIVO):
        try:
            with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as f:
                print(type(f))
                return json.load(f)

        except (json.JSONDecodeError, FileNotFoundError):
            return []
    return []