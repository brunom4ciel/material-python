import pytest
from unittest.mock import patch
from src.codigo_020_classe_estoque_e_estoque_critico import codigo_cliente_estoque_e_estoque_critico

@pytest.mark.parametrize("valor_esperado", [(["quantidade média do estoque: 225.00", "quantidade média do estoque crítico: 175.00", "situação do estoque: Efetuar compra", "situação do estoque crítico: Não efetuar compra"])])
def teste_codigo_cliente_estoque_e_estoque_critico_com_sucesso(valor_esperado):
	with patch('builtins.print') as mock_print:
		codigo_cliente_estoque_e_estoque_critico(220, 400, 50)
		mock_print.assert_any_call(valor_esperado[0])
		mock_print.assert_any_call(valor_esperado[1])
		mock_print.assert_any_call(valor_esperado[2])
		mock_print.assert_any_call(valor_esperado[3])
