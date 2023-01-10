# Файл содержит числа и буквы. Каждый записан в отдельной строке.
# Нужно считать содержимое в список так, чтобы сначала шли числа по возрастанию,
# а потом слова по возрастанию их длинны.
f = open('123', 'r')
s = f.readlines()
print(s)
a = []
b = []
for i in s:
    i = i[:-1]
    if i.isalpha():
        b.append(i)
    elif i.isdigit():
        i = int(i)
        a.append(i)
a.sort()
b.sort()
mas = a+b
print(mas)
# f.close()