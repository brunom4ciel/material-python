import abc

class DocumentoAbstrata(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def abrir(self):
        pass