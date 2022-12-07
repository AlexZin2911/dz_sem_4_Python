# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.(Вывод тех элементов, которые были без повторов)
# Ввод: 1 2 3 2 4 4
# Вывод: 1 3

import numpy as np
lst = np.random.randint(-10, 10, 20)
print(lst)
# num = []
# print(random(num))
list = []
num_unik = set(lst)
for i in num_unik:
    list.append(i)
print(list)