def func_add():
    spisok_smth = []
    add = None
    while add != "":
        spisok_smth.append(add)
        add = input("Введите данные, чтобы закончить просто нажмите 'Enter'. ")
    for x in set(spisok_smth):    # set() - преобразует в множество, удаляя дубликаты.
        y = spisok_smth.count(x)
        print("Элемент - ", x, "\t|""\tЧастота - ", y)


func_add()
