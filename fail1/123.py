# В текстовом файле посчитать количество строк,
# а также для каждой отдельной строки определить количество в ней символов

f = open('text.txt', 'r')
lines = 0
symbol = 0
for line in f:
    lines += 1
    for i in line:
        if i != ' ' and symbol == 0:
            symbol = 1
        elif i == ' ':
            symbol = 0
    print(line, 'символов:', len(line))
print("строк:", lines)
f.close()

