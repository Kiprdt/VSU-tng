from random import randint
s = randint(0, 100)
k = -1
while k != s:
    k = int(input())
    if k > s:
        print("Загаданное число меньше")
    elif k < s:
        print("Загаданное число больше")
    else:
        print("Угадал!")
