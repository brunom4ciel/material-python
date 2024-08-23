import abc

class CadeiraAbstrata(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def sentar_em(self):
        pass