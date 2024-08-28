from .codigo_017_builder_abstrato import BuilderAbstrato
from .codigo_017_produto_base import ProdutoBase

class BuilderConcreta(BuilderAbstrato):

    def __init__(self):
        self.limpar()

    def limpar(self) -> None:
        self.__produtoBase = ProdutoBase()

    @property
    def produto(self)-> ProdutoBase:
        produto = self.__produtoBase
        self.limpar()
        return produto

    def construir_parte_a(self) -> None:
        self.__produtoBase.adicionar_parte("Parte a")

    def construir_parte_b(self)-> None:
        self.__produtoBase.adicionar_parte("Parte b")

    def construir_parte_c(self)-> None:
        self.__produtoBase.adicionar_parte("Parte c")
