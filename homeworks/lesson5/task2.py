"""
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества
слов в каждой строке.
"""

my_file = open('viki.txt', 'r')

content = my_file.readlines()
print(f'Количество строк в файле - {len(content)}')

my_file = open('viki.txt', 'r')
content = my_file.read().split()
print(f'Общее количество слов - {len(content)}')

my_file.close()
