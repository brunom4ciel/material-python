import abc

class SofaAbstrato(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def sentar_em(self):
        pass