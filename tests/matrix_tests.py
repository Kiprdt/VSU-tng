from app.matrix_deter import Matrix3x3
import pytest


def test_determinant():
    m = Matrix3x3([[1, 9, -8], [21, 0 , 0], [0, 4, 8]])
    f = m.determinant()
    assert f == -2184


def test_determinant2():
    m = Matrix3x3([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    f = m.determinant()
    assert f == 0


def test_input(mocker):
    mocker.patch("builtins.input", side_effect=['3', '3'])
    f = Matrix3x3()
    f.input()
    assert f == Matrix3x3([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
