class Estoque:
    def __init__(self, qtd_atual: int, qtd_max: int, qtd_min: int) -> None:
        self.qtd_atual = qtd_atual
        self.qtd_max = qtd_max
        self.qtd_min = qtd_min

    def obter_qtd_media(self) -> float:
        return (self.qtd_max + self.qtd_min)/2
    
    def obter_situacao(self, qtd_media: float = None) -> str:
        qtd_media = self.obter_qtd_media() if qtd_media == None else qtd_media
        return 'Não efetuar compra' if self.qtd_atual >= qtd_media else 'Efetuar compra'
    
class EstoqueCritico(Estoque):
    def __init__(self, qtd_atual: int, qtd_max: int, qtd_min: int) -> None:
        super().__init__(qtd_atual, qtd_max, qtd_min)

    def obter_qtd_media_critica(self) -> float:
        return (self.qtd_max - self.qtd_min)/2

def codigo_cliente_estoque_e_estoque_critico(qtd_atual: int, qtd_max: int, qtd_min: int):
    estoque_critico = EstoqueCritico(qtd_atual, qtd_max, qtd_min)
    print('quantidade média do estoque: {0:.2f}'.format(estoque_critico.obter_qtd_media()))
    print('quantidade média do estoque crítico: {0:.2f}'.format(estoque_critico.obter_qtd_media_critica()))
    print('situação do estoque: {}'.format(estoque_critico.obter_situacao()))
    print('situação do estoque crítico: {}'.format(estoque_critico.obter_situacao(estoque_critico.obter_qtd_media_critica())))

if __name__ == "__main__":
    codigo_cliente_estoque_e_estoque_critico(220, 400, 50)