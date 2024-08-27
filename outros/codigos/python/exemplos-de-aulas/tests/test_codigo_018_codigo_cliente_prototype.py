import pytest
from unittest.mock import patch
from src.padroesdeprojetos.criacao import codigo_cliente_prototype

@pytest.mark.parametrize("valor_esperado", [(["PrototypeConcreta1 com valor: Valor 1", "PrototypeConcreta2 com valor: Valor 2"])])
def teste_codigo_cliente_prototype_com_sucesso(valor_esperado):
	with patch('builtins.print') as mock_print:
		codigo_cliente_prototype()
		mock_print.assert_any_call(valor_esperado[0])
		mock_print.assert_any_call(valor_esperado[1])
		assert mock_print.call_count == len(valor_esperado)
