from hw3-1 import func_add


a = func_add()
for x in set(a):    # set() - преобразует в множество, удаляя дубликаты.
    y = a.count(x)
    print("Элемент - ", x, "\t|""\tЧастота - ", y)
