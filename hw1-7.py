a = int(input("Введите X:"))
b = int(input("Введите Y:"))
sum = 0
for i in range(a, b + 1):
    if i % 5 == 0:
        sum += i
print(sum)
