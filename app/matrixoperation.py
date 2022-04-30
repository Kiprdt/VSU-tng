class Matrix:
    def __init__(self, spisok=None):
        if spisok is None:
            spisok = [[0]]
        self.line = len(spisok)
        self.column = len(spisok[0])
        self.spisok = spisok

    def input(self):
        self.spisok = []
        self.line = int(input("Введите количество строк - "))
        self.column = int(input("Введите количество столбцов - "))
        for _ in range(self.line):
            self.spisok.append([])
            for _ in range(self.column):
                x = int(input("Ввод - "))
                self.spisok[-1].append(x)

    def __add__(self, other):
        newmatrix = Matrix()
        newmatrix.spisok = []
        for i in range(self.line):
            newmatrix.spisok.append([])
            for j in range(self.column):
                x = self.spisok[i][j] + other.spisok[i][j]
                newmatrix.spisok[-1].append(x)
        return newmatrix

    def __mul__(self, other):
        if self.column == other.line:
            newmatrix = Matrix()
            tempmatrix = []
            newmatrix.spisok = []
            x = 0
            for i in range(self.line):
                for j in range(other.column):
                    for k in range(other.line):
                        x += self.spisok[i][k] * other.spisok[k][j]
                    tempmatrix.append(x)
                    x = 0
                newmatrix.spisok.append(tempmatrix)
                tempmatrix = []
            return newmatrix
        raise ValueError("Перемножать можно только согласованные матрицы")


    def __str__(self):
        return "\n".join(["\t".join(map(str, i)) for i in self.spisok])


# b = Matrix3x3()
# b.input()
# print(b)
# print(b.determinant())

a = Matrix([[1, 2], [3, 4]])
b = Matrix([[5, 6], [7, 8]])
c = a + b
print(c)
d = a * b
print(d)



