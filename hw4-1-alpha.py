def func_add():
    spisok = []
    spisok = list(map(int, spisok))
    add = input("Введите данные, чтобы закончить просто нажмите 'Enter'. ")
    while add != "":
        spisok.append(add)
        add = input("Введите данные, чтобы закончить просто нажмите 'Enter'. ")
    k = int(input("Введите сдвиг:"))
    spisok = spisok[-k:] + spisok[:-k]
    print(spisok)


func_add()
