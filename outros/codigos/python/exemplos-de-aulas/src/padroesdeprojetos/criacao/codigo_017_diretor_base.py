from .codigo_017_builder_abstrato import BuilderAbstrato

class Diretor:
    def __init__(self)-> None:
        self.__construir = None

    @property
    def construir(self) -> BuilderAbstrato:
        return self.__construir
    
    @construir.setter
    def construir(self, construir: BuilderAbstrato) -> None:
        self.__construir = construir

    def construir_produto_simples(self) -> None:
        self.__construir.construir_parte_c()

    def construir_produto_sofisticado(self) -> None:
        self.__construir.construir_parte_a()
        self.__construir.construir_parte_b()
        self.__construir.construir_parte_c()
