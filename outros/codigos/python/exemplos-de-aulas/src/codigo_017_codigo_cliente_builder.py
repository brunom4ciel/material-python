import sys
import os
# Adiciona o caminho do diretório `atual` ao sys.path. 
# Isso resolver problemas com imports de módulos que estão no mesmo diretório.
sys.path.append(os.path.join(os.path.dirname(__file__), '..', ''))

from src.codigo_017_builder_concreta import BuilderConcreta
from src.codigo_017_diretor_base import Diretor

def codigo_cliente_builder():
    # Criando um ConcreteBuilder
    builder = BuilderConcreta()

    # Passando o builder para o Director
    diretor = Diretor(builder)

    # O diretor constrói o produto
    diretor.construir()

    # Obtendo o produto final
    produto = builder.obter_resultado()

    print(f"{produto}")

