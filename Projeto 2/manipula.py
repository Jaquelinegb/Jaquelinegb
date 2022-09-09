# Módulo manipula_xls
# Decrição: Este módulo oferece funções para manipular arquivos
# no formato xls.
# Autora: Jaqueline
# Versão: 0.0.1
# Data: 09/09/2022

# Importação de pacotes
from openpyxl import workbook

def cria_xls() -> workbook:
    """Esta função cria uma pasta de trabalho MS-Excel."""
    pasta = workbook()
    return pasta

def cria_planilha(nome_planilha: str, pasta: workbook) -> None:
        pasta.active
        pasta.create_sheet(nome_planilha)
