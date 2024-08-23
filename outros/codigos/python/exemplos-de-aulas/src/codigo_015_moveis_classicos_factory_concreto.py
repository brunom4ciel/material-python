from src import CadeiraAbstrata, SofaAbstrato, MoveisFactoryAbstrato, SofaClassicoConcreta, CadeiraClassicaConcreta

class MoveisClassicosFactoryConcreto(MoveisFactoryAbstrato):
    def criar_cadeira(self) -> CadeiraAbstrata:
        return CadeiraClassicaConcreta()

    def criar_sofa(self) -> SofaAbstrato:
        return SofaClassicoConcreta()
