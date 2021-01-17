"""Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
«день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число,
месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных. """
print("Task № 1 ")


class Data:
    def __init__(self, day_month_year):

        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != "-": my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2021 >= year >= 0:
                    return f'Дата указана верно.'
                else:
                    return f'Не верный год.'
            else:
                return f'Не верный месяц.'
        else:
            return f'Не верный день.'

    def __str__(self):
        return f'Текущая дата: {Data.extract(self.day_month_year)}'


today = Data("16 - 01 - 2021")
print(today)
print(Data.extract("01 - 01 - 1934"))
print(today.extract("15 - 12 - 2077"))
print(Data.valid(45, 3, 2077))
print(today.valid(26, 12, 99999))
print(Data.valid(16, 1, 2021))

"""Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, 
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту 
ситуацию и не завершиться с ошибкой. """
print("Task № 2 ")
class ZeroError(Exception):
    def __init__(self, program):
        self.program = program


def division():
    try:
        number1 = int(input('Введите первое число >>> '))
        number2 = int(input('Введите второе число >>> '))
        if number2 == 0:
            raise ZeroError("Делить на ноль запрещено!")
        else:
            res = number1 / number2
            return res
    except ValueError:
        return "Нужно вводить число !"
    except ZeroError as err:
        return err


print(f'Результат: {division()}')


"""Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. 
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список. 
Класс-исключение должен контролировать типы данных элементов списка. """
print("Task № 3 ")
class NumbersError(Exception):
    def __init__(self):
        pass


class TypeCheck:
    def __init__(self):
        self.my_list = []

    def check_value(self):
        global user_val
        while True:
            try:
                try:
                    user_val = int(input('Введите данные >>> '))
                    ex = input(f'Данные добавлены "{user_val}" в список. \nПродолжить "Enter", вывести список "q": ').lower()
                    self.my_list.append(user_val)
                    if ex == 'q':
                        print(self.my_list)
                        break
                except ValueError:
                    raise NumbersError
            except NumbersError:
                ex = input(f'Нужно вводить числа !!!, \nПродолжить "Enter", вывести список "q": ').lower()
                if ex == 'q':
                    print(self.my_list)
                    break
                else:
                    self.check_value()


a = TypeCheck()
a.check_value()


"""Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», 
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В 
базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, 
уникальные для каждого типа оргтехники. """

"""Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в 
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, 
а также других данных, можно использовать любую подходящую структуру, например словарь. """

"""Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, 
для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных. """
print("Task № 4-6 ")
from typing import Any


class StoreMashines:
    my_unit: Any

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    def reception(self):
        try:
            unit = input(f'Введите наименование >>>')
            unit_p = int(input(f'Введите цену за ед >>>'))
            unit_q = int(input(f'Введите количество >>>'))
            unique = {'Модель устройства': unit, 'Цена за ед': unit_p, 'Количество': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Текущий список:\n {self.my_store}')
        except:
            return f'Ошибка ввода данных !!!'

        print(f'Для продолжения "Enter", для выхода "Q"')
        q = input(f'Ваше решение >>> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад:\n {self.my_store_full}')
            return f'Выход'
        else:
            return StoreMashines.reception(self)


class Printer(StoreMashines):
    def to_print(self):
        return f'Количества принтеров, отправленных на склад: {self.numb} '


class Scanner(StoreMashines):
    def to_scan(self):
        return f'Количества сканеров, отправленных на склад: {self.numb} '


class Copier(StoreMashines):
    def to_copier(self):
        return f'Количества копиров, отправленных на склад: {self.numb} '


unit_1 = Printer('hp', 4557, 8, 45)
unit_2 = Scanner('Canon', 3560, 6, 35)
unit_3 = Copier('Xerox', 1245, 12, 52)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_2.to_scan())
print(unit_3.to_copier())


"""Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку 
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные 
числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата. """
print("Task № 7 ")

class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'Сложение кмплексных чисел: {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        return f'Умножение комплексных чисел: {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'


c_1 = ComplexNumber(55, 99)
c_2 = ComplexNumber(36, 78)
print(c_1 + c_2)
print(c_1 * c_2)