def func():
    n = int(input())
    g = 0
    for i in range(2, n // 2 + 1):    
        if n % i == 0:
            g = g + 1
    if g == 0:
        return True
    else:
        return False
