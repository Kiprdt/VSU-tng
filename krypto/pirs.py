import random
import datetime


def pirs(message, message1):
    table = list(range(0, 256))
    random.shuffle(table)
    print(table)
    hasher1 = len(message) % 256
    hasher2 = len(message1) % 256
    for i in message:
        hasher1 = table[(hasher1 + ord(i)) % 256]
        hasher2 = table[(hasher2 + ord(i)) % 256]
    if hasher1 == hasher2:
        return True
    return False

----------------------------------------------------------------------


import random

key = 10101
random.seed(key)
table = list(range(0, 255))

random.shuffle(table)


def hasher(message, tabler):
    hasher1 = len(message) % 256
    for i in message:
        hasher1 = tabler[(hasher1 + ord(i)) % 256]
    return hasher1




alp = "ABCDEFG"

gen = ["A", "B", "C", "AA", "BB", "CC", "AB", "BC", "AC", "BC", "BA", "CA", "CB"]

for j in gen:
    print(hasher(j, table))
    #если есть одинаковые то значит есть коллизия
