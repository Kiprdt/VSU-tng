def factorial(n):
    k = 1
    if n == 0:
        return 1
    else:
        for i in range(2, n + 1):
            k = k * i
        return k


def factorial_tests():
    assert factorial(5) == 120
    assert factorial(3) == 6
    assert factorial(0) == 1


n = int(input("Введите число."))
print(factorial(n))
factorial_tests()
