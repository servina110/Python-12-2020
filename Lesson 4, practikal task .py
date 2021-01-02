"""1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами."""
print("Task № 1")


def sal():
    try:
        time = float(input('Выработка в часах >>> '))
        salary = int(input('Ставка в час руб. >>> '))
        bonus = int(input('Премия в руб. >>> '))
        res = time * salary + bonus
        print(f'Заработная плата сотрудника:  {res} руб.')
    except ValueError:
        return print('Ошибка, введите число.')


sal()

"""2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123]."""
print("Task № 2")
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
my_new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num] and num > 0]
print(f'Исходный список: {my_list}')
print(f'Результат: {my_new_list}')

"""3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор."""
print("Task № 3")
print(f'Числа от 20 до 240 кратные 20 или 21 - {[el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]}')

"""4. Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел, соответствующих требованию. Элементы вывести в порядке их следования в исходном списке. Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]"""
print("Task № 4")
my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
my_new_list = [el for el in my_list if my_list.count(el) < 2]
print(my_new_list)

"""5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные числа от 100 до 1000 (включая границы). 
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce()."""
print("Task № 5")
from functools import reduce


def my_func(el_p, el):
    return el_p * el


print(f'Список четных чисел от 100 до 1000 : {[el for el in range(99, 1001) if el % 2 == 0]}')
print(
    f'Результат вычисления произведения всех элементов списка: {reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0])}')

"""6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен быть бесконечным. 
Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. 
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено."""
print("Task № 6")
print("а) Итератор, генерирующий целые числа, начиная с указанного")
from itertools import count

for el in count(int(input('Введите стартовое число >>> '))):
    if el > 10:
        break
    else:
        print(el)
print("б) Итератор, повторяющий элементы некоторого списка, определенного заранее :")
from itertools import cycle

count = 0
my_list = ['С', 'Новым', 'Годом', '2021']
for el_2 in cycle(my_list):
    if count > 20:
        break
    print(el_2)  # внимание - беконечный цикл!
    count += 1

"""7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. 
При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n). 
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24."""
print("Task № 7")
from itertools import count
from math import factorial


def fibo_gen():
    for el in count(1):
        yield factorial(el)


gen = fibo_gen()
x = 0
for i in gen:
    if x < 15:
        print(i)
        x += 1
    else:
        break
