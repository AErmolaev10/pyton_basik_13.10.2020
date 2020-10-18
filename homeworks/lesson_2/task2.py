"""
Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы
с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

my_list = []
new_el = 0

while new_el != 'q':
    new_el = input('Введите элемент списка, для выхода введите "q"')
    if new_el != 'q':
        my_list.append(new_el)
    else:
        break

n = 0
for i in range(int(len(my_list))):
    if n + 2 <= len(my_list):
        my_list[n], my_list[n + 1] = my_list[n + 1], my_list[n]
        n += 2
    else:
        break

print(my_list)
