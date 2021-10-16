a = list(input("Введите строку:"))
k = int(input("Введите номер искомой цифры:"))
new_list = []
for p in a:
    if p.isdigit():
        new_list.append(p)
print(new_list[k-1])
