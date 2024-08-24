from src import MoveisFactoryAbstrato

# Cliente usando a Abstract Factory
def codigo_cliente(factory: MoveisFactoryAbstrato):
    cadeira = factory.criar_cadeira()
    sofa = factory.criar_sofa()

    print(cadeira.sentar_em())
    print(sofa.sentar_em())
