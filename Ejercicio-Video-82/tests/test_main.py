import pytest
from main import sumar, is_greater_than, login


def test_sumar():
    assert sumar(2, 5) == 7  # assert comprueba que sea verdadero


def test_is_greater_than():
    assert is_greater_than(23, 2)


@pytest.mark.parametrize(
    "input_x,input_y,expected",
    [(5, 1, 6), (6, sumar(4, 2), 12), (sumar(19, 1), 15, 35), (-7, 10, sumar(-7, 10))],
)
def test_sum_params(input_x, input_y, expected):
    assert sumar(input_x, input_y) == expected


def test_login_pass():
    login_passes = login("Pablosky", "EntuPut4V1d4creriasAlgoF4lz0")
    assert login_passes


def test_login_pass_fail():
    login_passes_fail = login("Pablusky", "EntuPut4V1d4creriasAlgoF4lz0")
    assert (
        not login_passes_fail
    )  # Al estar mal deberia de devolver false, por eso el not
