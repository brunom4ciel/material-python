from typing import Any

class ProdutoBase():
    def __init__(self)-> None:
        self._partes = []

    def adicionar_parte(self, parte: Any) -> None:
        self._partes.append(parte)

    def __str__(self):
        return f"Partes do produto: {', '.join(self._partes)}"