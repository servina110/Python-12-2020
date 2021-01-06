"""1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка."""
print("Task № 1 ")
my_f = open('file.txt', 'w', encoding="UTF=8")
line = input('Введите текст >>>\n')
while line:
    my_f.writelines(line)
    line = input('Введите текст >>>\n')
    if not line:
        break

my_f.close()
my_f = open('file.txt', 'r', encoding="UTF=8")
content = my_f.readlines()
print(f'{content}\n')
my_f.close()

"""2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, 
количества слов в каждой строке."""
print("Task № 2 ")
my_file = open('file_2.txt', 'r', encoding="UTF-8")
content = my_file.read()
print(f'Содержимое файла: \n {content} \n')
my_file = open('file_2.txt', 'r', encoding="UTF-8")
content = my_file.readlines()
print(f'Количество строк в файле: {len(content)} шт.\n')
my_file = open('file_2.txt', 'r', encoding="UTF-8")
line = 0
for i in my_file:
    line += 1

    flag = 0
    word = 0
    for j in i:
        if j != ' ' and flag == 0:
            word += 1
            flag = 1
        elif j == ' ':
            flag = 0

    print(i, f' количество слов в строке:  {word} шт.\n')
my_file = open('file_2.txt', 'r', encoding="UTF-8")
content = my_file.read()
content = content.split()
print(f'\n Общее количество слов: - {len(content)} шт.\n')
my_file.close()

"""3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк). 
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. 
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""
print("Task № 3 ")
with open('file_3.txt', 'r', encoding="UTF-8") as my_file:
    sal = []
    poor = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(float(i[1])) < 20000:
            poor.append(i[0])
        sal.append(i[1])
print(
    f'Оклад меньше 20 тыс. руб. у сотрудников: {poor}, средний оклад: {"%.2f" % (sum(map(float, sal)) / len(sal))} руб.\n')

"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. 
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл."""
print("Task № 4 ")
numbers = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('file_4.txt', 'r', encoding="UTF-8") as file_rep:
    for i in file_rep:
        i = i.split(' ', 1)
        new_file.append(numbers[i[0]] + '  ' + i[1])
    print(f'{new_file}\n')

with open('file_4_new.txt', 'w', encoding="UTF-8") as file_rep_2:
    file_rep_2.writelines(new_file)

"""5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. 
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""
print("Task № 5 ")


def summary():
    try:
        with open('file_5.txt', 'w+', encoding="UTF-8") as file_obj:
            line = input('Введите числа через пробел >>>\n')
            file_obj.writelines(line)
            my_numb = line.split()

            print(f'Сумма чисел: {sum(map(int, my_numb))}\n')

    except ValueError:
        print('ОШИБКА !!! Неправильно введены данные, необходимо вводить числа !')


summary()

"""6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и 
наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. 
Важно, чтобы для каждого предмета не обязательно были все типы занятий. 
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. 
Вывести словарь на экран.
Примеры строк файла: 
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}"""
print("Task № 6 ")
subj = {}
with open('file_6.txt', 'r', encoding="UTF-8") as init_f:
    for line in init_f:
        subject, lecture, practice, lab = line.split()
        subj[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Общее количество часов по предметам: \n {subj}\n')

"""7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать 
данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. 
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. 
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджер контекста."""
print("Task № 7 \n")

import json

profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('file_7.txt', 'r', encoding="UTF-8") as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Прибыль средняя: {prof_aver:.2f} руб.')
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
    pr = {'средняя прибыль': round(prof_aver)}
    profit.update(pr)
    print(f'Прибыль каждой компании: {profit} руб.')

with open('file_7.json', 'w', encoding="UTF-8") as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f'Создан файл с расширением json со следующим содержимым: \n 'f' {js_str}')
