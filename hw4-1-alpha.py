def func_add():
    s = []
    n = input("Введите данные, чтобы закончить просто нажмите 'Enter'. ")
    while n != "":
        s.append(n)
        n = input("Введите данные, чтобы закончить просто нажмите 'Enter'. ")
    return s


def moving(s, z):
    s = s[-z:] + s[:-z]
    return s


def moving_tests():
    assert moving([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
    assert moving([7, 12, 14, 8, 1, 5], 3) == [8, 1, 5, 7, 12, 14]
    assert moving([7, 6, 5, 4, 3, 2, 1], 4) == [4, 3, 2, 1, 7, 6, 5]


a = func_add()
k = int(input("Введите значение для сдвига:"))
print(moving(a, k))
moving_tests()
