def func_add():
    spisok = []
    add = 0
    while add != "":
        add = input()
        spisok.append(add)
    if "" in spisok:
        spisok.remove("")
    print(spisok)
