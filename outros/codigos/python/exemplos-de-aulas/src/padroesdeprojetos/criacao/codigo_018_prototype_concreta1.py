from .codigo_018_prototype_base import PrototypeBase
import copy

class PrototypeConcreta1(PrototypeBase):
    def __init__(self, value):
        self.value = value

    def clone(self):
        # Usa a função deepcopy para criar uma cópia do objeto
        # Leia mais em https://docs.python.org/pt-br/3/library/copy.html
        return copy.deepcopy(self)

    def __str__(self):
        return f"PrototypeConcreta1 com valor: {self.value}"