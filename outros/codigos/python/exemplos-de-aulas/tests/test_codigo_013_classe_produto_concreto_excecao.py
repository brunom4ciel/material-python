from src import ProdutoConcretoExcecao
import pytest

@pytest.mark.parametrize(('nome', 'codigo', 'preco', 'quantidade'), [('Arroz', 1, 1, 1), ('Feijao', 1, 1, 1)])
def testa_classe_produto_concreto_excecao_geral_com_sucesso(nome, codigo, preco, quantidade):
	produto = ProdutoConcretoExcecao(nome, codigo, preco, quantidade)
	assert produto.obtem_nome() == nome and produto.obtem_codigo() == codigo and produto.obtem_preco() == preco and produto.obtem_lote() != 0 and produto.obtem_serie() != 0
	assert produto.obtem_produto() == '{}-{}-{}-{}-{}-{}'.format(produto.obtem_lote(), produto.obtem_serie(), nome, codigo, preco, quantidade)
	assert produto.altera_preco(2) == True
	assert produto.altera_preco(1) == False
	assert produto.altera_quantidade(2) == False
	assert produto.altera_quantidade(1) == True