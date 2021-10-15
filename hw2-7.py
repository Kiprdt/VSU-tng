from random import randint
s = randint(0, 100)
k = int()
while k != s:
    k = int(input())
    if k > s:
        print("Загаданное число меньше")
    elif k < s:
        print("Загаданное число больше")
    else:
        print("Угадал!")