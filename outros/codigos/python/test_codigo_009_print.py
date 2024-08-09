from codigo_009_print import print_obtem_numero, print_obter_tres_numeros_simples, print_obter_trinta_numeros, print_obter_n_numeros
import pytest
from unittest.mock import patch

@pytest.mark.parametrize("valor_esperado", [(10), (9)])
def teste_print_obtem_numero_com_sucesso(valor_esperado):
	with patch('builtins.input', return_value=valor_esperado), patch('builtins.print') as mock_print:
		print_obtem_numero()
		mock_print.assert_called_once_with(valor_esperado)
		assert mock_print.call_count == 1

@pytest.mark.parametrize("valor_esperado", [([10,10,10]), ([9,9,9])])
def teste_print_obtem_tres_numeros_com_sucesso(valor_esperado):
	with patch('builtins.input', side_effect=valor_esperado), patch('builtins.print') as mock_print:
		print_obter_tres_numeros_simples()
		mock_print.assert_called_once_with(valor_esperado)
		assert mock_print.call_count == 1

@pytest.mark.parametrize("valor_esperado", [([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]), (list(range(0, 30)))])
def teste_print_obtem_trinta_numeros_com_sucesso(valor_esperado):
	with patch('builtins.input', side_effect=valor_esperado), patch('builtins.print') as mock_print:
		print_obter_trinta_numeros()
		mock_print.assert_called_once_with(valor_esperado)
		assert mock_print.call_count == 1

@pytest.mark.parametrize("valor_esperado", [(list(range(0, 90)))])
def teste_print_obtem_n_numeros_com_sucesso(valor_esperado):
	with patch('builtins.input', side_effect=valor_esperado), patch('builtins.print') as mock_print:
		print_obter_n_numeros(len(valor_esperado))
		mock_print.assert_called_once_with(valor_esperado)
		assert mock_print.call_count == 1




