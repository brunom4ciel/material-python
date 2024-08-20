from src import SingletonLazy

def testa_classe_singleton_lazy_se_duas_instancias_sao_iguais_com_sucesso():
	singleton = SingletonLazy().get_instance()
	assert id(singleton) == id(SingletonLazy().get_instance())
	# id() Retorna a identidade de um objeto.
	# Isso é garantido como único entre objetos existentes simultaneamente.
	# (CPython usa o endereço de memória do objeto.)
