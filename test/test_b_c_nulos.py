from src.raiz_ecuacion_segundo_grado import raiz_ecuacion_segundo_grado
import pytest


@pytest.mark.b_c_nulos
def test_raiz_nula_unica():
    assert raiz_ecuacion_segundo_grado(1, 0, 0) == 0

@pytest.mark.a_nulo
def test_raiz_nula_coeficiente_nulo():
    assert raiz_ecuacion_segundo_grado(0, 0, 0) == None