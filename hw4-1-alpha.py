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


a = func_add()
k = int(input("Введите значение для сдвига:"))
print(moving(a, k))
