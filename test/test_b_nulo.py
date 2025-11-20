from src.raiz_ecuacion_segundo_grado import raiz_ecuacion_segundo_grado
import pytest

@pytest.mark.b_nulo
def test_b_nulo():
    assert raiz_ecuacion_segundo_grado(1, 0, -1) == (1, -1)
    assert raiz_ecuacion_segundo_grado(-1, 0, 1) == (1, -1)

@pytest.mark.b_nulo
def test_b_nulo_solucion_imagiaria():
    assert raiz_ecuacion_segundo_grado(1, 0, 1) is None
    assert raiz_ecuacion_segundo_grado(-1, 0, -1) is None