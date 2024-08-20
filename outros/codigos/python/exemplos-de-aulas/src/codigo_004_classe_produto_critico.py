from src.codigo_003_classe_produto import Produto

class ProdutoCritico(Produto):
    def __init__(self, nome: str, codigo: int, preco: int, quantidade: int, estoque_min: int):
        super().__init__(nome, codigo, preco, quantidade)
        self.estoque_min = estoque_min
    
    def obtem_serie(self)-> int:
        return self.serie
    
    def altera_quantidade(self, novo_pedido: int) -> bool:
        if novo_pedido + self.estoque_min > self.quantidade:
            return False
        return super().altera_quantidade(novo_pedido)

    def altera_preco(self, novo_preco: int) -> bool:
        preco_atual = self.preco
        if novo_preco > 1.1 * preco_atual or novo_preco < 0.9 * preco_atual:
            return False
        super().altera_preco(novo_preco)
        return True
    
    def obtem_produto(self) -> str:
        return '{}-{}-{}-{}-{}'.format(self.nome, self.codigo, self.preco, self.quantidade, self.estoque_min)
