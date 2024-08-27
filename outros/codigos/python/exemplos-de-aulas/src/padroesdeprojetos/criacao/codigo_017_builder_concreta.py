from .codigo_017_builder_abstrato import BuilderAbstrato
from .codigo_017_produto_base import ProdutoBase

class BuilderConcreta(BuilderAbstrato):

    def __init__(self):
        self.produtoBase = ProdutoBase()

    def build_parte1(self)-> str:
        self.produtoBase.parte1 = "Parte 1"

    def build_parte2(self)-> str:
        self.produtoBase.parte2 = "Parte 2"

    def build_parte3(self)-> str:
        self.produtoBase.parte3 = "Parte 3"

    def obter_resultado(self)-> ProdutoBase:
        return self.produtoBase