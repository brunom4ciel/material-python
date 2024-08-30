import pytest
from unittest.mock import patch
from src.codigo_019_classe_produto_e_produto_critico import codigo_cliente_produto_e_produto_critico

@pytest.mark.parametrize("valor_esperado", [("nomes: Laptop, Cadeira, Mesa\nnome: Sofa")])
def teste_codigo_cliente_produto_e_produto_critico_com_sucesso(valor_esperado):
	with patch('builtins.print') as mock_print:
		codigo_cliente_produto_e_produto_critico()
		mock_print.assert_any_call(valor_esperado)
		assert mock_print.call_count == 1
