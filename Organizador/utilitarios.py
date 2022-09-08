import os
import shutil

def cria_dir(nome: str):
    if os.path.exists(nome) == False:
        os.mkdir(nome)

        
def mov_arquivos(arquivos: list):
    for arquivo in arquivos:
        if ".xls" in arquivo:
            shutil.move(arquivo, f"./planilhas/{arquivo}")
        elif ".doc" in arquivo:
            shutil.move(arquivo, f"./documentos/{arquivo}")

