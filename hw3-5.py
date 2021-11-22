from hw31 import func_add

def middle_func(n):
    n = [float(i) for i in n]
    middle = sum(n) / len(n)
    print(middle)


x = func_add()
middle_func(x)
