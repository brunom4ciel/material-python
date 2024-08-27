from .codigo_018_prototype_base import PrototypeBase
from .codigo_018_codigo_cliente_prototype import codigo_cliente_prototype
from .codigo_018_prototype_concreta1 import PrototypeConcreta1
from .codigo_018_prototype_concreta2 import PrototypeConcreta2

from .codigo_017_builder_concreta import BuilderConcreta
from .codigo_017_builder_abstrato import BuilderAbstrato
from .codigo_017_diretor_base import Diretor
from .codigo_017_produto_base import ProdutoBase
from .codigo_017_codigo_cliente_builder import codigo_cliente_builder

__all__ = ['PrototypeBase', 'codigo_cliente_prototype', 'PrototypeConcreta1', 'PrototypeConcreta2',
           'BuilderConcreta', 'BuilderAbstrato', 'Diretor', 'ProdutoBase',
           'codigo_cliente_builder']

# A partir do Python 3.3, o __init__.py se tornou opcional para pacotes. 
# Se um diretório não contém um __init__.py, ele é considerado um pacote namespace. 
# Pacotes namespace permitem dividir um pacote em vários diretórios diferentes, 
# mas geralmente o __init__.py ainda é usado para controlar a 
# inicialização e a organização dos módulos.