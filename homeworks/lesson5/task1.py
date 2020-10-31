"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании
ввода данных свидетельствует пустая строка.
"""

file = open('task1.txt', 'w')

while True:
    line = input('write new line')
    if not line:
        break
    file.writelines(line + '\n')

file.close()

file = open('task1.txt', 'r')
for line in file:
    print(line)

file.close()


