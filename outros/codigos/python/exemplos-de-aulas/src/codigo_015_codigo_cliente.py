from src import MoveisFactoryAbstrato

# Cliente usando a Abstract Factory
def codigo_cliente(factory: MoveisFactoryAbstrato):
    chair = factory.criar_cadeira()
    sofa = factory.criar_sofa()

    print(chair.sentar_em())
    print(sofa.sentar_em())
