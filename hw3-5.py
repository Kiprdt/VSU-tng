def sequence():
    x = list()
    n = input()
    while n != "":
        x.append(n)
        n = input()
    else:
        x = [float(i) for i in x]    # Преобразуем все элементы списка во float.
        middle = sum(x) / len(x)
        print(middle)


sequence()
