from .codigo_001_somar import somar
from .codigo_002_lambda_somar import somar as somar_lambda
from .codigo_003_classe_produto import Produto
from .codigo_005_classe_produto_perecivel import ProdutoPerecivel
from .codigo_004_classe_produto_critico import ProdutoCritico
from .codigo_006_classe_veiculo_com_exception import Veiculo
from .codigo_008_input import obtem_numero, obter_tres_numeros_simples, obter_trinta_numeros, obter_n_numeros
from .codigo_009_print import print_obtem_numero, print_obter_tres_numeros_simples, print_obter_trinta_numeros, print_obter_n_numeros
from .codigo_010_classe_singleton import Singleton
from .codigo_011_classe_singleton_lazy import SingletonLazy
from .codigo_012_classe_produto_abstrato import ProdutoAbstrato
from .codigo_012_classe_produto_concreto import ProdutoConcreto
from .codigo_013_classe_produto_abstrato_excecao import ProdutoAbstratoExcecao
from .codigo_013_classe_produto_concreto_excecao import ProdutoConcretoExcecao
from .codigo_014_argv import iniciar_app

__all__ = ['somar', 'somar_lambda', 'Produto', 'ProdutoPerecivel', 
           'ProdutoCritico', 'Veiculo', 'obtem_numero', 
           'obter_tres_numeros_simples', 'obter_trinta_numeros', 
           'obter_n_numeros', 'print_obtem_numero', 
           'print_obter_tres_numeros_simples', 'print_obter_trinta_numeros', 
           'print_obter_n_numeros', 'Singleton', 'SingletonLazy', 
           'ProdutoAbstrato','ProdutoConcreto', 'ProdutoAbstratoExcecao',
           'ProdutoConcretoExcecao', 'iniciar_app']

# A partir do Python 3.3, o __init__.py se tornou opcional para pacotes. 
# Se um diretório não contém um __init__.py, ele é considerado um pacote namespace. 
# Pacotes namespace permitem dividir um pacote em vários diretórios diferentes, 
# mas geralmente o __init__.py ainda é usado para controlar a 
# inicialização e a organização dos módulos.