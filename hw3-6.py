def func(z):
    g = 0
    for i in range(2, z // 2 + 1):
        if z % i == 0:
            g = g + 1
    return g == 0


def func_tests():
    assert func(2) == True
    assert func(8) == False
    assert func(56) == False
    assert func(13) == True

    
z = int(input("Введите число:"))
print(func(z))
func_tests()
