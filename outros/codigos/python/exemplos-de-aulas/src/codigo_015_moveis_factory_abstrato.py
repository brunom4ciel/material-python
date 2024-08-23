import abc
from src import CadeiraAbstrata, SofaAbstrato

class MoveisFactoryAbstrato(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def criar_cadeira(self) -> CadeiraAbstrata:
        pass

    @abc.abstractmethod
    def criar_sofa(self) -> SofaAbstrato:
        pass
