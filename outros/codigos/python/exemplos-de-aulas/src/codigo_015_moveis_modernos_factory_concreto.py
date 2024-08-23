from src import CadeiraAbstrata, SofaAbstrato, MoveisFactoryAbstrato, SofaModernoConcreta, CadeiraModernaConcreta

class MoveisModernosFactoryConcreto(MoveisFactoryAbstrato):
    def criar_cadeira(self) -> CadeiraAbstrata:
        return CadeiraModernaConcreta()

    def criar_sofa(self) -> SofaAbstrato:
        return SofaModernoConcreta()
