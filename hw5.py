print("Введите значение для 'x' и 'y' ")
x = int(input())
y = int(input())
if x>0 and y>0:
    print("1-я четверть")
elif x>0 and y<0:
    print("4-я четверть")
elif x<0 and y<0:
    print("3-я четверть")
elif x<0 and y>0:
    print("2-я четверть")
elif x==0 and y>0 or x==0 and y<0:
    print("Точка лежит на оси 'Y' ")
elif x>0 and y==0 or x<0 and y==0:
    print("Точка лежит на оси 'X' ")
elif x==0 and y==0:
    print("Точка лежит в начале координат")