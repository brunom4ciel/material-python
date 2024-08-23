from src import SofaAbstrato

class SofaClassicoConcreta(SofaAbstrato):
    def sentar_em(self):
        return "Sentado em um sofa classico"