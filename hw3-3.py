def fibonacci(n1):
    fib1 = 1
    fib2 = 1
    print(fib1, fib2, end=' ')
    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, end=' ')


n = int(input("Введите номер элемента:"))
fibonacci(n)
