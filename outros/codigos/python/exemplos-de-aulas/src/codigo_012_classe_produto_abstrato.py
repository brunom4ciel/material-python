import abc
class ProdutoAbstrato(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self, nome: str, codigo: int, preco: int, quantidade: int) -> None:
        pass
    @abc.abstractmethod
    def obtem_nome(self)-> str:
        pass
    @abc.abstractmethod
    def obtem_codigo(self)-> int:
        pass
    @abc.abstractmethod 
    def obtem_preco(self)-> int:
        pass
    @abc.abstractmethod
    def obtem_serie(self)-> int:
        pass 
    @abc.abstractmethod
    def obtem_lote(self)-> int:
        pass
    @abc.abstractmethod
    def altera_preco(self, novo_preco) -> bool:
        pass  
    @abc.abstractmethod
    def altera_quantidade(self, novo_pedido: int) -> bool:
        pass
    @abc.abstractmethod
    def obtem_produto(self) -> str:
        pass
