from codigo_004_classe_produto_critico import ProdutoCritico
import pytest

@pytest.mark.parametrize(('nome', 'codigo', 'preco', 'quantidade', 'estoque_min'), [('Arroz', 1, 10, 10, 20)])
def teste_alteracao_preco_de_produtos_com_sucesso(nome, codigo, preco, quantidade, estoque_min):
	produto_critico = ProdutoCritico(nome, codigo, preco, quantidade, estoque_min)	
	assert produto_critico.altera_preco(11) == True

@pytest.mark.parametrize(('nome', 'codigo', 'preco', 'quantidade', 'estoque_min'), [('Arroz', 1, 10, 10, 20)])
def teste_alteracao_preco_de_produtos_com_falha(nome, codigo, preco, quantidade, estoque_min):
	produto_critico = ProdutoCritico(nome, codigo, preco, quantidade, estoque_min)	
	assert produto_critico.altera_preco(12) == False

@pytest.mark.parametrize(('nome', 'codigo', 'preco', 'quantidade', 'estoque_min'), [('Arroz', 1, 10, 10, 20)])
def teste_alteracao_quantidade_de_produtos_com_sucesso(nome, codigo, preco, quantidade, estoque_min):
	produto_critico = ProdutoCritico(nome, codigo, preco, quantidade, estoque_min)	
	assert produto_critico.altera_quantidade(2) == False

@pytest.mark.parametrize(('nome', 'codigo', 'preco', 'quantidade', 'estoque_min'), [('Arroz', 1, 10, 100, 20)])
def teste_alteracao_quantidade_de_produtos_com_falha(nome, codigo, preco, quantidade, estoque_min):
	produto_critico = ProdutoCritico(nome, codigo, preco, quantidade, estoque_min)	
	assert produto_critico.altera_quantidade(1) == True

@pytest.mark.parametrize(('nome', 'codigo', 'preco', 'quantidade', 'estoque_min'), [('Arroz', 1, 10, 100, 20)])
def teste_obtem_produto_com_sucesso(nome, codigo, preco, quantidade, estoque_min):
	produto_critico = ProdutoCritico(nome, codigo, preco, quantidade, estoque_min)		
	assert 	produto_critico.obtem_produto() == '{}-{}-{}-{}-{}'.format(nome, codigo, preco, quantidade, estoque_min)

@pytest.mark.parametrize(('nome', 'codigo', 'preco', 'quantidade', 'estoque_min'), [('Arroz', 1, 10, 100, 20)])
def teste_obtem_serie_com_sucesso(nome, codigo, preco, quantidade, estoque_min):
	produto_critico = ProdutoCritico(nome, codigo, preco, quantidade, estoque_min)		
	assert 	produto_critico.obtem_serie() == produto_critico.serie