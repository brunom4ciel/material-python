import pytest
from src import Singleton
from src import Produto

def testa_classe_singleton_se_duas_instancias_sao_iguais_com_sucesso():
	singleton = Singleton()
	assert id(singleton) == id(Singleton())
	# id() Retorna a identidade de um objeto.
	# Isso é garantido como único entre objetos existentes simultaneamente.
	# (CPython usa o endereço de memória do objeto.)

@pytest.mark.parametrize(('produto', 'nome', 'codigo', 'preco', 'quantidade', 
						  'produto2', 'nome2', 'codigo2', 'preco2', 'quantidade2'), 
						  [(Produto, 'Arroz', 1, 1, 1, Produto, 'Feijao', 1, 1, 1), 
		 				   (Produto, 'Feijao', 1, 1, 1, Produto, 'Arroz', 1, 1, 1,)])
def testa_classe_singleton_se_duas_instancias_de_produto_sao_iguais_com_sucesso(
	produto, nome, codigo, preco, quantidade, produto2, nome2, codigo2, preco2, quantidade2):
	produto_inst = Singleton(produto, nome, codigo, preco, quantidade)
	produto_inst2 = Singleton(produto2, nome2, codigo2, preco2, quantidade2)
	assert produto_inst.obtem_nome() == produto_inst2.obtem_nome() \
		and produto_inst.obtem_nome() == 'Arroz' and produto_inst2.obtem_nome() == 'Arroz'

@pytest.mark.parametrize(('produto', 'nome', 'codigo', 'preco', 'quantidade', 
						  'produto2', 'nome2', 'codigo2', 'preco2', 'quantidade2'), 
						  [(Produto, 'Arroz', 1, 1, 1, Produto, 'Feijao', 1, 1, 1), 
		 				   (Produto, 'Feijao', 1, 1, 1, Produto, 'Arroz', 1, 1, 1,)])
def testa_classe_singleton_atualizando_dados_na_instancia_com_sucesso(
	produto, nome, codigo, preco, quantidade, produto2, nome2, codigo2, preco2, quantidade2):
	produto_inst = Singleton(produto, nome, codigo, preco, quantidade)
	produto_inst2 = Singleton(produto2, nome2, codigo2, preco2, quantidade2)
	produto_inst.update_instance(produto=produto2, nome=nome2, codigo=codigo2, 
							  preco=preco2, quantidade=quantidade2)
	assert produto_inst.obtem_nome() == nome2 and produto_inst2.obtem_nome() == nome2
