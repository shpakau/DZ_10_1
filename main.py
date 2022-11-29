# # Задача 1.----------------------------------------------------------------------------
# # Реализуйте классы MinStat, MaxStat, AverageStat, которые будут находить минимум, максимум и среднее
# # арифметическое последовательности целых чисел.
# # Экземпляры классов инициализируются без аргументов. Метод add_number должен добавлять в статистику число,
# # которое будет учтено при вычислении финального результата методом result. Для экземпляров MinStat и
# # MaxStat result должен возвращать целое число, для AverageStat — число типа float (это число будет
# # сравниваться с правильным ответом до седьмой значащей цифры).
# # Если в последовательности отсутствуют числа и статистические величины вычислить невозможно,
# # метод result должен возвращать None.
# # --- Формат ввода
# # Каждый тест представляет собой код, в котором будут использоваться ваши классы. Файл c решением
# # необязательно называть solution.py, он будет переименован автоматически. Тест запускается с
# # вашими классами, а его вывод сравнивается с правильным решением.
print('Задача №1')

class MinStat:
    def __init__(self):
        self.v = []
    def add_number(self, n):
        self.v.append(n)
    def result(self):
        if self.v == []:
            return None
        else:
            return min(self.v)

class MaxStat:
    def __init__(self):
        self.v = []
    def add_number(self, n):
        self.v.append(n)
    def result(self):
        if self.v == []:
            return None
        else:
            return max(self.v)

class AverageStat:
    def __init__(self):
        self.v = []
    def add_number(self, n):
        self.v.append(n)
    def result(self):
        if self.v == []:
            return None
        else:
            n = len(self.v)
            s = sum(self.v)
            return s / n


print(' Пример №1')
values = [1, 2, 4, 5]

mins = MinStat()
maxs = MaxStat()
average = AverageStat()
for v in values:
    mins.add_number(v)
    maxs.add_number(v)
    average.add_number(v)

print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))

print('Пример №2')
mins = MinStat()
maxs = MaxStat()
average = AverageStat()

print(mins.result(), maxs.result(), average.result())

print('Пример №3')
values = [1, 0, 0]

mins = MinStat()
maxs = MaxStat()
average = AverageStat()
for v in values:
    mins.add_number(v)
    maxs.add_number(v)
    average.add_number(v)

print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))