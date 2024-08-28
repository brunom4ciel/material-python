import abc
from .codigo_017_produto_base import ProdutoBase

class BuilderAbstrato(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def limpar(self) -> None:
        pass

    @abc.abstractmethod
    def produto(self)-> ProdutoBase:
        pass

    @abc.abstractmethod
    def construir_parte_a(self)-> None:
        pass

    @abc.abstractmethod
    def construir_parte_b(self)-> None:
        pass

    @abc.abstractmethod
    def construir_parte_c(self)-> None:
        pass
