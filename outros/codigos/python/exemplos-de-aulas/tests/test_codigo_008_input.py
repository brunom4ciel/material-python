from src import obtem_numero, obter_tres_numeros_simples, obter_trinta_numeros, obter_n_numeros
import pytest
from unittest.mock import patch

@pytest.mark.parametrize("valor_esperado", [(10), (9)])
def teste_obter_numero_com_sucesso(valor_esperado):
	with patch('builtins.input', return_value=valor_esperado):
		resultado = obtem_numero()
		assert resultado == valor_esperado

@pytest.mark.parametrize("valor_esperado", [([10,10,10]), ([9,9,9])])
def teste_obter_tres_numeros_simples_com_sucesso(valor_esperado):
	with patch('builtins.input', side_effect=valor_esperado):
		resultado = obter_tres_numeros_simples()
		assert resultado == valor_esperado

@pytest.mark.parametrize("valor_esperado", [([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]), (list(range(0, 30)))])
def teste_obter_trinta_numeros_com_sucesso(valor_esperado):
	with patch('builtins.input', side_effect=valor_esperado):
		resultado = obter_trinta_numeros()
		assert resultado == valor_esperado

@pytest.mark.parametrize("valor_esperado", [(list(range(0, 90)))])
def teste_obter_n_numeros_com_sucesso(valor_esperado):
	with patch('builtins.input', side_effect=valor_esperado):
		resultado = obter_n_numeros(len(valor_esperado))
		assert resultado == valor_esperado