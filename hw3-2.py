def seasons(n):
    months = {"Зима": [1, 2, 12],
              "Весна": [3, 4, 5],
              "Лето": [6, 7, 8],
              "Осень": [9, 10, 11]}
    for key in months:
        if n in months[key]:
            return key


def seasons_tests():
    assert seasons(4) == "Весна"
    assert seasons(11) == "Осень"
    assert seasons(6) == "Лето"
    assert seasons(1) == "Зима"


n = int(input("Введите номер месяца:"))
print(seasons(n))
seasons_tests()
