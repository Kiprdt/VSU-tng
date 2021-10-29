def factorial():
    n = int(input("Введите число."))
    k = 1
    if n == 0:
        return 1
    else:
        for i in range(2, n + 1):
            k = k * i
        print(k)


factorial()
      
