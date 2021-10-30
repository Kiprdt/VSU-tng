def fibonacci(n1):
    if n1 in (1, 2):
        return 1
    return fibonacci(n1 - 1) + fibonacci(n1 - 2)


n = int(input("Введите номер элемента:"))
print(fibonacci(n))
