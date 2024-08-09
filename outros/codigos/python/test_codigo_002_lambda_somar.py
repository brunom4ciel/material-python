from codigo_002_lambda_somar import somar

def teste_somar_com_sucesso():
	assert somar(1,2) == 3

def teste_soma_com_erro():
	assert somar(1,2) != 2
