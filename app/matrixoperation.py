class Matrix:
    def __init__(self, spisok=None):
        if spisok is None:
            spisok = [[0]]
        self.line = len(spisok)
        self.column = len(spisok[0])
        self.spisok = spisok

    @classmethod
    def from_list(cls, spisok):
        return cls(spisok)

    def input(self):
        self.spisok = []
        self.line = int(input("Введите количество строк - "))
        self.column = int(input("Введите количество столбцов - "))
        for _ in range(self.line):
            self.spisok.append([])
            for _ in range(self.column):
                x = int(input("Ввод - "))
                self.spisok[-1].append(x)

    def __eq__(self, other):
        if self.line == len(other.spisok):
            count = 0
            for i in range(self.line):
                for k in range(self.column):
                    if self.spisok[i][k] == other.spisok[i][k]:
                        continue
                    else:
                        count += 1
                if count == 0:
                    return self.spisok == other.spisok
                else:
                    return False
        else:
            return False

    def __add__(self, other):
        newspisok = []
        for i in range(self.line):
            newspisok.append([])
            for j in range(self.column):
                x = self.spisok[i][j] + other.spisok[i][j]
                newspisok[-1].append(x)
        return Matrix.from_list(newspisok)

    def __sub__(self, other):
        newspisok = []
        for i in range(self.line):
            newspisok.append([])
            for j in range(self.column):
                x = self.spisok[i][j] - other.spisok[i][j]
                newspisok[-1].append(x)
        return Matrix.from_list(newspisok)

    def __rmul__(self, other):
        newspisok = []
        for i in range(self.line):
            newspisok.append([])
            for j in range(self.column):
                x = self.spisok[i][j] * other
                newspisok[-1].append(x)
        return Matrix.from_list(newspisok)
    
    def mul_tion(self, other):
        if self.column == other.line:
            tempmatrix = []
            newmatrix = []
            x = 0
            for i in range(self.line):
                for j in range(other.column):
                    for k in range(other.line):
                        x += self.spisok[i][k] * other.spisok[k][j]
                    tempmatrix.append(x)
                    x = 0
                newmatrix.append(tempmatrix)
                tempmatrix = []
            return Matrix.from_list(newmatrix)
        raise ValueError("Перемножать можно только согласованные матрицы")

    def __mul__(self, other):
        if isinstance(self, Matrix) and isinstance(other, Matrix):
            return self.mul_tion(other)
        elif isinstance(self, Matrix) and isinstance(other, int):
            return self.__rmul__(other)
        elif isinstance(self, int) and isinstance(other, Matrix):
            return other.__rmul__(self)
        return False

    def __truediv__(self, other):
        if other != 0:
            newspisok = []
            for i in range(self.line):
                newspisok.append([])
                for j in range(self.column):
                    x = self.spisok[i][j] / other
                    newspisok[-1].append(x)
            return Matrix.from_list(newspisok)
        else:
            raise ValueError('На ноль делить нельзя!')

    def __str__(self):
        return "\n".join(["\t".join(map(str, i)) for i in self.spisok])

    def __repr__(self):
        return str(self)
