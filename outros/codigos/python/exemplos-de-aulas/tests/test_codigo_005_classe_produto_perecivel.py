from src import ProdutoPerecivel
import pytest

@pytest.mark.parametrize(('nome', 'codigo', 'preco', 'quantidade', 'validade'), [('Arroz', 1, 10, 100, 20)])
def teste_obtem_produto_com_sucesso(nome, codigo, preco, quantidade, validade):
	produto_perecivel = ProdutoPerecivel(nome, codigo, preco, quantidade, validade)		
	assert 	produto_perecivel.obtem_produto() == '{}-{}-{}-{}-{}'.format(nome, codigo, preco, quantidade, validade)
