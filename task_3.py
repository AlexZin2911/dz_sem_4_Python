# Дан список. Выведите те его элементы, которые встречаются в списке только один раз. 
# Элементы нужно выводить в том порядке, в котором они встречаются в списке.
# [1,2,3,4,4,5,5,6] -> [1,2,3,6]

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