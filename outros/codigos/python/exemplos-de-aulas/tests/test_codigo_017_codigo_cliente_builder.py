import pytest
from unittest.mock import patch
from src.padroesdeprojetos.criacao import codigo_cliente_builder

@pytest.mark.parametrize("valor_esperado", [("Produto: Parte1=Parte 1, Parte2=Parte 2, Parte3=Parte 3")])
def teste_codigo_cliente_builder_com_sucesso(valor_esperado):
	with patch('builtins.print') as mock_print:
		codigo_cliente_builder()
		mock_print.assert_any_call(valor_esperado)
		assert mock_print.call_count == 1

