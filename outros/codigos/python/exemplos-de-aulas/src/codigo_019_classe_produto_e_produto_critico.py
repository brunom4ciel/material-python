class Produto:
    def obter_nomes(self) -> str:
        return 'Laptop, Cadeira, Mesa'

class ProdutoCritico(Produto):
    def obter_nome(self) -> str:
        return 'Sofa'

def codigo_cliente_produto_e_produto_critico():
    produto_critico = ProdutoCritico()
    nomes = produto_critico.obter_nomes()
    nome = produto_critico.obter_nome()
    print('nomes: {}\nnome: {}'.format(nomes, nome))

codigo_cliente_produto_e_produto_critico()