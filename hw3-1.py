def func_add():
    spisok = []
    add = input("Введите данные, чтобы закончить просто нажмите 'Enter'. ")
    while add != "":
        spisok.append(add)
        add = input("Введите данные, чтобы закончить просто нажмите 'Enter'. ")
    print(spisok)
