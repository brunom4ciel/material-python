import abc

class BuilderAbstrato(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def build_parte1(self):
        pass

    @abc.abstractmethod
    def build_parte2(self):
        pass

    @abc.abstractmethod
    def build_parte3(self):
        pass