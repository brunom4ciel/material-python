import pytest
from unittest.mock import patch
from src import MoveisModernosFactoryConcreto, MoveisClassicosFactoryConcreto, codigo_cliente

@pytest.mark.parametrize("valor_esperado", [(['Sentado em uma cadeira moderna', 'Sentado em um sofa moderno'])])
def teste_codigo_cliente_para_usar_moveis_modernos_com_sucesso(valor_esperado):
	with patch('builtins.print') as mock_print:
		moderna_factory = MoveisModernosFactoryConcreto()
		codigo_cliente(moderna_factory)
		mock_print.assert_any_call(valor_esperado[0])
		mock_print.assert_any_call(valor_esperado[1])
		assert mock_print.call_count == len(valor_esperado)

@pytest.mark.parametrize("valor_esperado", [(['Sentado em uma cadeira classica', 'Sentado em um sofa classico'])])
def teste_codigo_cliente_para_usar_moveis_classicos_com_sucesso(valor_esperado):
	with patch('builtins.print') as mock_print:
		moderna_factory = MoveisClassicosFactoryConcreto()
		codigo_cliente(moderna_factory)
		mock_print.assert_any_call(valor_esperado[0])
		mock_print.assert_any_call(valor_esperado[1])
		assert mock_print.call_count == len(valor_esperado)
