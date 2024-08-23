from src import SofaAbstrato

class SofaModernoConcreta(SofaAbstrato):
    def sentar_em(self):
        return "Sentado em um sofa moderno"