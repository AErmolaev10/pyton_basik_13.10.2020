"""
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества
слов в каждой строке.
"""

my_file = open('viki.txt', 'r')

content = my_file.readlines()
print(f'Number of lines in the file - {len(content)}')

my_file = open('viki.txt', 'r')
content = my_file.read().split()
print(f'Total number of words - {len(content)}')

my_file.close()
