from src import iniciar_app
import pytest
from unittest.mock import patch
from io import StringIO
import sys

def test_parse_args():
	original_stdout = sys.stdout
	sys.stdout = StringIO()  # Redireciona stdout para capturar a saída
	test_argv = ['arg1', 'arg2', 'arg3'] # Argumentos de teste
	iniciar_app(test_argv)
	output = sys.stdout.getvalue() # Obtém a saída capturada
	sys.stdout = original_stdout  # Restaura o stdout original	
	expected_output = 'arg1\narg2\narg3\n' # Verifica se a saída está correta
	assert output == expected_output

@pytest.mark.parametrize(
    "test_argv, expected_output",
    [(['arg1', 'arg2', 'arg3'], 'arg1\narg2\narg3\n'),(['foo', 'bar'], 'foo\nbar\n')]
)
def test_parse_args_with_patch(test_argv, expected_output):
	with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
		iniciar_app(test_argv) # Chama a função com os argumentos de teste		
		output = mock_stdout.getvalue() # Obtém a saída capturada		
		assert output == expected_output # Verifica se a saída está correta