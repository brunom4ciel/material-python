class Veiculo:
    chassi: int # público
    __motor: int # privado
    def __init__(self, chassi: int, motor: int):
        self.chassi = chassi
        self.__motor = motor
    def obtem_chassi(self)-> int:
        return self.chassi    
    def obtem_motor(self)-> int:
        return self.__motor    
    def altera_chassi(self, novo_chassi: int) -> bool:
        try:
            if novo_chassi != self.chassi: 
                self.chassi = novo_chassi
                return True
            else:
                raise ValueError("Chassi igual ao atual")
        except ValueError as error:
            raise ValueError(error)
