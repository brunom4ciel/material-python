class ProdutoAbstratoExcecao:

    def __init__(self, nome: str, codigo: int, preco: int, quantidade: int) -> None:
        raise NotImplementedError()
    def obtem_nome(self)-> str:
        raise NotImplementedError()
    def obtem_codigo(self)-> int:
        raise NotImplementedError()
    def obtem_preco(self)-> int:
        raise NotImplementedError()    
    def obtem_serie(self)-> int:
        raise NotImplementedError()     
    def obtem_lote(self)-> int:
        raise NotImplementedError()    
    def altera_preco(self, novo_preco) -> bool:
        raise NotImplementedError() 
    def altera_quantidade(self, novo_pedido: int) -> bool:
        raise NotImplementedError()
    def obtem_produto(self) -> str:
        raise NotImplementedError()
