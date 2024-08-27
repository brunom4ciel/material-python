from .codigo_017_builder_abstrato import BuilderAbstrato

class Diretor:
    def __init__(self, builder: BuilderAbstrato):
        self.builder = builder

    def construir(self):
        self.builder.build_parte1()
        self.builder.build_parte2()
        self.builder.build_parte3()
