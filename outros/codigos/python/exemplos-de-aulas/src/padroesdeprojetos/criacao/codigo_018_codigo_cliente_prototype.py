if __name__ == "__main__":
    import sys
    import os
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))) # volta 2 pastas
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
    print(f"{clone1}")  # PrototypeConcreta1 com Valor: Valor 1
    print(f"{clone2}")  # PrototypeConcreta2 com Valor: Valor 2

if __name__ == "__main__":
    codigo_cliente_prototype()