import pytest
from math_utils import somar, subtrair, multiplicar, dividir, e_par

def test_soma_positivos():
    assert somar(2, 3) == 5

def test_subtracao_negativa():
    assert subtrair(10, 15) == -5

def test_multiplicacao_por_zero():
    assert multiplicar(5, 0) == 0

def test_divisao_comum():
    assert dividir(10, 2) == 5

def test_verificar_se_e_par():
    assert e_par(4) is True
    assert e_par(7) is False

def test_divisao_por_zero_erro():
    with pytest.raises(ValueError):
        dividir(10, 0)
