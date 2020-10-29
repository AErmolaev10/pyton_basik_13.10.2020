"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""

dic = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
rus_file = []


with open('task4.txt', 'r', encoding='UTF-8') as my_f:
    for i in my_f:
        print(i)
        i = i.split(' ', 1)
        print(i)
        rus_file.append(dic[i[0]] + ' ' + i[1])

print(rus_file)

with open('task4_new.txt', 'w', encoding='UTF-8') as file_obj_2:
    file_obj_2.writelines(rus_file)
