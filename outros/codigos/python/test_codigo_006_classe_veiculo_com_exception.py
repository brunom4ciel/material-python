from codigo_006_classe_veiculo_com_exception import Veiculo
import pytest

@pytest.mark.parametrize(('chassi', 'motor'), [('KHG969878976G7DF9G7', 'SGD97S9')])
def teste_obtem_chassi_e_motor_com_sucesso(chassi, motor):
	veiculo = Veiculo(chassi, motor)		
	assert 	veiculo.obtem_chassi() == chassi and veiculo.obtem_motor() == motor

@pytest.mark.parametrize(('chassi', 'motor', 'novo_chassi'), [('KHG969878976G7DF9G7', 'SGD97S9', 'KHG969878976G7DF9G7')])
def teste_alterar_chassis_iguais(chassi, motor, novo_chassi):
	veiculo = Veiculo(chassi, motor)
	with pytest.raises(ValueError) as excinfo:  
		veiculo.altera_chassi(novo_chassi) 
	assert str(excinfo.value) == "Chassi igual ao atual" and excinfo.type is ValueError

@pytest.mark.parametrize(('chassi', 'motor', 'novo_chassi'), [('KHG969878976G7DF9G7', 'SGD97S9', 'KHG969878976G7DF9G6')])
def teste_alterar_chassis_diferentes(chassi, motor, novo_chassi):
	veiculo = Veiculo(chassi, motor)
	assert veiculo.altera_chassi(novo_chassi) == True
