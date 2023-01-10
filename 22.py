# Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно
# как в первом списке, так и во втором.

a = [1, 2, 3]
b = [4, 5, 6, 7, 8, 9]
print('Всех одновременно ', len(a + b))
c = []
print(c.count(a + b))

# или
aa = set(map(int, input('Ввод ').split()))
bb = set(map(int, input('Ввод ').split()))
cc = aa.intersection(bb)
print(len(cc))
