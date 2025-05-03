import json
import os

def salvar_lista(caminho_arquivo, lista_objetos):
    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        json.dump([obj._asdict() for obj in lista_objetos], f, ensure_ascii=False, indent=4)

def carregar_lista(caminho_arquivo, tipo_namedtuple):
    if os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            dados = json.load(f)
            return [tipo_namedtuple(**item) for item in dados]
    return []