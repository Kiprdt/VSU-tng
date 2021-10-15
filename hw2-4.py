express = input()
k = express.count("(") - express.count(")")
if k > 0:
    print("Не хватает", k, "закрывающих скобок")
elif k < 0:
    print("Не хватает", -k, "открывающих скобок.")
else:
    print("Верное количество скобок.")