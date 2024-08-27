if __name__ == "__main__":
    import sys
    import os
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    from padroesdeprojetos.criacao.codigo_018_prototype_concreta1 import PrototypeConcreta1
    from padroesdeprojetos.criacao.codigo_018_prototype_concreta2 import PrototypeConcreta2
else:
    from .codigo_018_prototype_concreta1 import PrototypeConcreta1
    from .codigo_018_prototype_concreta2 import PrototypeConcreta2

def codigo_cliente_prototype():
    # Criando os protótipos
    prototype1 = PrototypeConcreta1("Valor 1")
    prototype2 = PrototypeConcreta2("Valor 2")

    # Clonando os protótipos
    clone1 = prototype1.clone()
    clone2 = prototype2.clone()

    # Exibindo os objetos clonados
    print(f"{clone1}")  # ConcretePrototype1 com Valor: Valor 1
    print(f"{clone2}")  # ConcretePrototype2 com Valor: Valor 2

if __name__ == "__main__":
    codigo_cliente_prototype()