def func_add():
    spisok = []
    add = None
    while add != "":
        add = input("Введите данные, чтобы закончить просто нажмите 'Enter'. ")
        spisok.append(add)
    if "" in spisok:
        spisok.remove("")
    print(spisok)
