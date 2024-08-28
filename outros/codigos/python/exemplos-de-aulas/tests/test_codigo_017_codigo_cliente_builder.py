import pytest
from unittest.mock import patch
from src.padroesdeprojetos.criacao import codigo_cliente_builder

@pytest.mark.parametrize("valor_esperado", [("Partes do produto: Parte c", "Partes do produto: Parte a, Parte b, Parte c")])
def teste_codigo_cliente_builder_com_sucesso(valor_esperado):
	with patch('builtins.print') as mock_print:
		codigo_cliente_builder()
		mock_print.assert_any_call(valor_esperado[0])
		mock_print.assert_any_call(valor_esperado[1])
		assert mock_print.call_count == len(valor_esperado)
