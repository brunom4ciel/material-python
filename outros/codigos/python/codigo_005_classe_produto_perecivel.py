from codigo_003_classe_produto import Produto

class ProdutoPerecivel(Produto):
    def __init__(self, nome: str, codigo: int, preco: int, quantidade: int, validade: int):
        super().__init__(nome, codigo, preco, quantidade)
        self.validade = validade
        
    def obtem_produto(self) -> str:
        return '{}-{}-{}-{}-{}'.format(self.nome, self.codigo, self.preco, self.quantidade, self.validade)

