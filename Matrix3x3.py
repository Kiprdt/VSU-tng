class Matrix:
    def __init__(self, spisok=None):
        if spisok is None:
            spisok = [[0]]
        self.spisok = spisok

    def input(self):
        self.spisok = []
        line = int(input("Введите количество строк - "))
        column = int(input("Введите количество столбцов - "))
        for _ in range(line):
            self.spisok.append([])
            for _ in range(column):
                x = int(input("Ввод - "))
                self.spisok[-1].append(x)

    def __str__(self):
        return "\n".join(["\t".join(map(str, i)) for i in self.spisok])


class Matrix3x3(Matrix):
    def __init__(self, spisok=None):
        if spisok is None:
            spisok = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        super().__init__(spisok)
        if not self._is_valid():
            raise ValueError("Only matrix 3x3")

    def input(self):
        super().input()
        if not self._is_valid():
            raise ValueError("Only matrix 3x3")

    def _is_valid(self) -> bool:
        if len(self.spisok) != 3:
            return False
        elif len(self.spisok[0]) != 3:
            return False
        elif len(self.spisok[1]) != 3:
            return False
        elif len(self.spisok[2]) != 3:
            return False
        return True

    def determinant(self):
        pos_on = self.spisok[0][0] * self.spisok[1][1] * self.spisok[2][2]
        pos_tw = self.spisok[0][1] * self.spisok[1][2] * self.spisok[2][0]
        pos_th = self.spisok[2][1] * self.spisok[1][0] * self.spisok[0][2]
        min_pos_on = self.spisok[0][2] * self.spisok[1][1] * self.spisok[2][0]
        min_pos_tw = self.spisok[0][1] * self.spisok[1][0] * self.spisok[2][2]
        min_pos_th = self.spisok[1][2] * self.spisok[2][1] * self.spisok[0][0]
        return pos_on + pos_tw + pos_th - min_pos_on - min_pos_tw - min_pos_th


b = Matrix3x3()
b.input()
print(b)
print(b.determinant())
