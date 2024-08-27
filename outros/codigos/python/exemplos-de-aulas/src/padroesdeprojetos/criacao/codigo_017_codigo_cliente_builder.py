if __name__ == "__main__":
    import sys
    import os
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    from padroesdeprojetos.criacao.codigo_017_builder_concreta import BuilderConcreta
    from padroesdeprojetos.criacao.codigo_017_diretor_base import Diretor
else:
    from .codigo_017_builder_concreta import BuilderConcreta
    from .codigo_017_diretor_base import Diretor

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

if __name__ == "__main__":
    codigo_cliente_builder()