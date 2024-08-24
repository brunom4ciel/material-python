import sys
import os
# Adiciona o caminho do diretório `atual` ao sys.path. 
# Isso resolver problemas com imports de módulos que estão no mesmo diretório.
sys.path.append(os.path.join(os.path.dirname(__file__), '..', ''))
from src import DocumentoPdfConcreta
from src import DocumentoMsWordConcreta

# Cliente usando a Factory Method
def codigo_cliente_factory_method(tipo_documento: str):

    if(tipo_documento == "word" or tipo_documento == "pdf"):

        if tipo_documento == "word":
            documento = DocumentoMsWordConcreta()

        elif tipo_documento == "pdf":
            documento = DocumentoPdfConcreta()

        print(documento.abrir())
    else:

        print("Tipo de documento desconhecido")
