import json
import os

ARQUIVO = 'data.json'

def carregar_dados():
    # Verifica se o arquivo existe para não dar erro na primeira vez que rodar
    if not os.path.exists(ARQUIVO):
        return []
    
    with open(ARQUIVO, 'r', encoding='utf-8') as f:
        return json.load(f)

def salvar_dados(dados):
    # Salva os dados de forma legível (indent=4)
    with open(ARQUIVO, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)