from codigo_003_classe_produto import Produto
import pytest

@pytest.mark.parametrize(('nome', 'codigo', 'preco', 'quantidade'), [('Arroz', 1, 1, 1), ('Feijao', 1, 1, 1)])
def testa_criacao_de_produtos_com_sucesso(nome, codigo, preco, quantidade):
	produto = Produto(nome, codigo, preco, quantidade)
	assert produto.obtem_nome() == nome and produto.obtem_codigo() == codigo and produto.obtem_preco() == preco and produto.obtem_lote() != 0 and produto.obtem_serie() != 0

@pytest.mark.parametrize(('nome', 'codigo', 'preco', 'quantidade'), [('Arroz', 1, 1, 1), ('Feijao', 1, 1, 1)])
def teste_alteracao_preco_de_produtos_com_sucesso(nome, codigo, preco, quantidade):
	produto = Produto(nome, codigo, preco, quantidade)	
	assert produto.altera_preco(2) == True

@pytest.mark.parametrize(('nome', 'codigo', 'preco', 'quantidade'), [('Arroz', 1, 1, 1), ('Feijao', 1, 1, 1)])
def teste_alteracao_preco_de_produtos_com_falha(nome, codigo, preco, quantidade):
	produto = Produto(nome, codigo, preco, quantidade)	
	assert produto.altera_preco(1) == False

@pytest.mark.parametrize(('nome', 'codigo', 'preco', 'quantidade'), [('Arroz', 1, 1, 1), ('Feijao', 1, 1, 1)])
def teste_alteracao_quantidade_de_produtos_com_sucesso(nome, codigo, preco, quantidade):
	produto = Produto(nome, codigo, preco, quantidade)	
	assert produto.altera_quantidade(2) == False

@pytest.mark.parametrize(('nome', 'codigo', 'preco', 'quantidade'), [('Arroz', 1, 1, 1), ('Feijao', 1, 1, 1)])
def teste_alteracao_quantidade_de_produtos_com_falha(nome, codigo, preco, quantidade):
	produto = Produto(nome, codigo, preco, quantidade)	
	assert produto.altera_quantidade(1) == True

@pytest.mark.parametrize(('nome', 'codigo', 'preco', 'quantidade'), [('Arroz', 1, 1, 1), ('Feijao', 1, 1, 1)])
def teste_obtem_produto_com_sucesso(nome, codigo, preco, quantidade):
	produto = Produto(nome, codigo, preco, quantidade)	
	assert produto.obtem_produto() == '{}-{}-{}-{}-{}-{}'.format(produto.obtem_lote(), produto.obtem_serie(), nome, codigo, preco, quantidade)