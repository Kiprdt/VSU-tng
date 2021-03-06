from app.matrix import Matrix
import pytest


@pytest.mark.parametrize(('f1', 'f2'), [
    ([[1, 2], [3, 4]], [[1, 2], [3, 4]]),
    ([[10, 25], [0, 4]], [[10, 25], [0, 4]]),
    ([[0, 0], [0, 0]], [[0, 0], [0, 0]])
])
def test_eq(f1, f2):
    a = Matrix(f1)
    b = Matrix(f2)
    assert a == b


@pytest.mark.parametrize(('f1', 'f2', 'f3'), [
    ([[1, 2], [3, 4]], [[1, 2], [3, 4]], [[2, 4], [6, 8]]),
    ([[10, 25], [3, 4]], [[10, 25], [0, 4]], [[20, 50], [3, 8]]),
    ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
])
def test_add(f1, f2, f3):
    a = Matrix(f1)
    b = Matrix(f2)
    assert a + b == Matrix(f3)


@pytest.mark.parametrize(('f1', 'f2', 'f3'), [
    ([[1, 2], [3, 4]], [[1, 2], [3, 4]], [[0, 0], [0, 0]]),
    ([[10, 25], [3, 4]], [[10, 25], [0, 4]], [[0, 0], [3, 0]]),
    ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[1, 0, 0], [0, 1, 0], [0, 0, 1]]),
    ([[-4, -8], [-9, -16]], [[5, -8], [-13, 4]], [[-9, 0], [4, -20]])
])
def test_sub(f1, f2, f3):
    a = Matrix(f1)
    b = Matrix(f2)
    assert a - b == Matrix(f3)


@pytest.mark.parametrize(('f1', 'f2', 'f3'), [
    ([[1, 2], [3, 4]], [[1, 2], [3, 4]], [[7, 10], [15, 22]]),
    ([[10, 25], [3, 4]], [[10, 25], [0, 4]], [[100, 350], [30, 91]]),
    ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]),
    ([[-4, -8], [-9, -16]], [[5, -8], [-11, 4]], [[68, 0], [131, 8]]),
    ([[-4, -8, -1], [-9, -16, 0]], [[5, -8], [-13, 4], [0, 4]], [[84, -4], [163, 8]])

])
def test_mul(f1, f2, f3):
    a = Matrix(f1)
    b = Matrix(f2)
    assert a * b == Matrix(f3)


@pytest.mark.parametrize(('f1', 'f2', 'f3'), [
    ([[0, 10], [-3, 1]], 4, [[0, 40], [-12, 4]]),
    ([[1, 2], [3, 4]], 4, [[4, 8], [12, 16]]),
    ([[1, 2], [3, 4]], 0, [[0, 0], [0, 0]])
])
def test_rmul(f1, f2, f3):
    a = Matrix(f1)
    b = f2
    print(b * a)
    assert a * b == Matrix(f3)
    assert b * a == Matrix(f3)
    
    
 @pytest.mark.parametrize(('f1', 'f2', 'f3'), [
    ([[0, 10], [-3, 1]], 4, [[0, 2.5], [-0.75, 0.25]]),
    ([[1, 2], [3, 4]], 5, [[0.2, 0.4], [0.6, 0.8]]),
    ([[1, 2], [3, 4]], 1, [[1, 2], [3, 4]])

])
def test_truediv(f1, f2, f3):
    a = Matrix(f1)
    b = f2
    print(b * a)
    assert a / b == Matrix(f3)




