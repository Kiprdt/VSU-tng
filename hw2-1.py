s = [ ]
st = input("Ввод:")
s.append(st)
while st != "":
    st = input("Ввод:")
    s.append(st)
else:
    list.pop([s])
if "" in s:
    s.remove("")
print(s)