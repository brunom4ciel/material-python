from codigo_001_somar import somar
import pytest

@pytest.mark.parametrize(('primeiro_numero', 'segundo_numero', 'resultado_esperado'), [(1, 1, 2), (11, 1, 12)])
def teste_somar_com_sucesso(primeiro_numero, segundo_numero, resultado_esperado):
	assert somar(primeiro_numero, segundo_numero) == resultado_esperado

@pytest.mark.parametrize(('primeiro_numero', 'segundo_numero', 'resultado_esperado'), [(1, 1, 3), (11, 1, 11)])
def teste_soma_com_erro(primeiro_numero, segundo_numero, resultado_esperado):
	assert somar(primeiro_numero, segundo_numero) != resultado_esperado
