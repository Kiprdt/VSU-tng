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
