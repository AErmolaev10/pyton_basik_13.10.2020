"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна
подсчитывать сумму чисел в файле и выводить ее на экран.
"""

with open('numb.txt', 'w', encoding='UTF-8') as num:
    numbers = input('Enter a set of numbers separated by a space')
    num.writelines(numbers)
    num_list = numbers.split()
    s = 0
    for i in num_list:
        s += int(i)
    print(s)
