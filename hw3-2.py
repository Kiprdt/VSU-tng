def seasons(n):
    months = {"Зима": (1, 2, 12),
              "Весна": (3, 4, 5),
              "Лето": (6, 7, 8),
              "Осень": (9, 10, 11)}
    for key in months:    # Перебор ключей в словаре.
        if n in months[key]:    # Соответствие между введённым "n" и ключами.
            return print(key)


n = int(input("Введите номер месяца:"))
seasons(n)
