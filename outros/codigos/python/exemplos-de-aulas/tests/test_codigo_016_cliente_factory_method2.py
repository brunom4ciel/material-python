import pytest
from unittest.mock import patch
from src import codigo_cliente_factory_method2

@pytest.mark.parametrize("valor_esperado", [(["Abrindo um documento PDF"])])
def teste_codigo_cliente_para_abrir_documento_pdf_com_sucesso(valor_esperado):
	with patch('builtins.print') as mock_print:
		codigo_cliente_factory_method2("pdf")
		mock_print.assert_any_call(valor_esperado[0])
		assert mock_print.call_count == len(valor_esperado)

@pytest.mark.parametrize("valor_esperado", [(["Abrindo um documento Microsoft Word"])])
def teste_codigo_cliente_para_abrir_documento_msword_com_sucesso(valor_esperado):
	with patch('builtins.print') as mock_print:
		codigo_cliente_factory_method2("word")
		mock_print.assert_any_call(valor_esperado[0])
		assert mock_print.call_count == len(valor_esperado)

@pytest.mark.parametrize("valor_esperado", [(["Tipo de documento desconhecido"])])
def teste_codigo_cliente_para_abrir_documento_outro_com_sucesso(valor_esperado):
	with patch('builtins.print') as mock_print:
		codigo_cliente_factory_method2("outro")
		mock_print.assert_any_call(valor_esperado[0])
		assert mock_print.call_count == len(valor_esperado)