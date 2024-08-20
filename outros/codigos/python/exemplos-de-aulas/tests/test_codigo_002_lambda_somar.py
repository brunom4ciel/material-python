from src import somar as somar_lambda

def teste_somar_com_sucesso():
	assert somar_lambda(1,2) == 3

def teste_soma_com_erro():
	assert somar_lambda(1,2) != 2
