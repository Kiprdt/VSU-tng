from app.matrix import Matrix
import pytest


def test_init():
    a = Matrix([[2, 1, 8], [3, 4, 6]])
    assert a.column == 3
    assert a.line == 2
    assert a.spisok == [
        [2, 1, 8],
        [3, 4, 6]
    ]


def test_input(mocker):
    mocker.patch('builtins.input', side_effect=['3', '3', '1', '1', '1', '1', '2', '3', '4', '5', '6'])
    f = Matrix()
    f.input()
    assert f.spisok == [[1, 1, 1], [1, 2, 3], [4, 5, 6]]


def test_str():
    z = Matrix([[2, 1, 8], [3, 4, 6]])
    q = str(z)
    assert q == '2\t1\t8\n3\t4\t6'
