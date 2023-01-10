# Ввести в файл ‘input.txt’ 2 числа в одну строку через пробел.
# Вывести в файл ‘output.txt’ их разность

with open('input.txt', 'w') as f_input, open('output.txt', 'w') as f_output:
   a = int(input('Введите целое число: '))
   b = int(input('Введите целое число: '))
   f_input.write(f'{a} {b}')
   f_output.write(f'{a - b}')
