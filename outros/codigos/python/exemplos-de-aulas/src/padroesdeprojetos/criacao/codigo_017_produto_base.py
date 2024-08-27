class ProdutoBase():
    def __init__(self):
        self.parte1 = None
        self.parte2 = None
        self.parte3 = None

    def __str__(self):
        return f"Produto: Parte1={self.parte1}, Parte2={self.parte2}, Parte3={self.parte3}"