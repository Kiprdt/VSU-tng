from hw3-1 import func_add


x = func_add()
x = [float(i) for i in x]    # Преобразуем все элементы списка во float.
middle = sum(x) / len(x)
print(middle)
