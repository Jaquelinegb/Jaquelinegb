import shutil
import os

arquivos = os.listdir()

for arquivo in arquivos:
    if ".xls" in arquivo:
        shutil.move(arquivo, f"./planilhas/{arquivo}")
    elif ".doc" in arquivo:
        shutil.move(arquivo, f"./documetos/{arquivo}")

