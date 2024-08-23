from src import ProdutoAbstratoExcecao

class ProdutoConcretoExcecao(ProdutoAbstratoExcecao):
    serie: int # público
    __lote: int # privado
    def __init__(self, nome: str, codigo: int, preco: int, quantidade: int):
        self.nome = nome
        self.codigo = codigo
        self.preco = preco
        self.quantidade = quantidade
        self.serie = round(codigo * 1000)
        self.__lote = round(1000)
    def obtem_nome(self)-> str:
        return self.nome    
    def obtem_codigo(self)-> int:
        return self.codigo    
    def obtem_preco(self)-> int:
        return self.preco    
    def obtem_serie(self)-> int:
        return self.serie    
    def obtem_lote(self)-> int:
        return self.__lote    
    def altera_preco(self, novo_preco) -> bool:
        preco_atual = self.preco
        self.preco = novo_preco
        if novo_preco > preco_atual: return True
        return False    
    def altera_quantidade(self, novo_pedido: int) -> bool:
        if novo_pedido > self.quantidade: return False
        self.quantidade -= novo_pedido
        return True    
    def obtem_produto(self) -> str:
        return '{}-{}-{}-{}-{}-{}'.format(self.__lote, self.serie, self.nome, self.codigo, self.preco, self.quantidade)
