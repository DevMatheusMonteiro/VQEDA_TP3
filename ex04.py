import os

def listar_diretorios(caminho, nivel=0):
    itens = os.listdir(caminho)
    for item in itens:
        caminho_completo = os.path.join(caminho, item)
        print("-" * nivel + item)
        if os.path.isdir(caminho_completo):
            listar_diretorios(caminho_completo, nivel + 1)

listar_diretorios("C:\\ADS\\Documentos")
