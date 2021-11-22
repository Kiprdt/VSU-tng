def func(z):
    g = 0
    for i in range(2, z // 2 + 1):
        if z % i == 0:
            g = g + 1
    if g == 0:
        return True
    return False


z = int(input("Введите число:"))
print(func(z))
