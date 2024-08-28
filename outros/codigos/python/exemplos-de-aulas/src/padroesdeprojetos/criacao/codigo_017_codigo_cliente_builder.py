# trecho de código para que seja possível você inicializar direto este script
# com base nos pacotes.
# início
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))) # volta 2 pastas
# fim
from padroesdeprojetos.criacao.codigo_017_builder_concreta import BuilderConcreta
from padroesdeprojetos.criacao.codigo_017_diretor_base import Diretor

def codigo_cliente_builder():
    diretor = Diretor()
    diretor.construir = BuilderConcreta()

    diretor.construir_produto_simples()    
    print(f"{diretor.construir.produto}")

    diretor.construir_produto_sofisticado()    
    print(f"{diretor.construir.produto}")

if __name__ == "__main__":
    codigo_cliente_builder()