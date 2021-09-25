s = [ ]
st = input("Ввод:")
s.append(st)
while st != "":
    st = input("Ввод:")
    s.append(st)
if "" in s:
    s.remove("")
print(s)
