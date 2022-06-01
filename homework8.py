'''1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый,
с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
(например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.'''

class Data:
  def __init__ (self, data):
    self.data = data

  @classmethod
  def from_string(cls, string_date):
    day, month, year = map(int, string_date.split('-'))
    data_list = cls(day, month, year) 
    return f'день{data_list[0]}, месяц{data_list[1]}, год {data_list[2]}'

  @staticmethod
  def valid (day, month, year):
    if year >= 2022:
      if 1 <= month <= 12:
        if (month in ['1', '3', '5', '7', '8', '10', '12'] and day <= 31) or (month in ['4', '6', '9', '11'] and day <= 30) or (month == 2 and day <=29):
          return f'Дата верная'
        else:
          return f'неправильный день'
      else:
        return f'не верный месяц'
    else:
      return f'этот год еще не наступил'

  def __str__(self):
    return f'Текущая дата {Data.from_string(self.data)}'


today = Data('30-05-2022')
print(today)
print(Data.valid(30, 5, 2022))
print(Data.valid(30, 5, 2023))
print(Data.valid(30, 15, 2022))
print(Data.valid(31, 2, 2022))
print(Data.from_string('30-05-2022'))


'''2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. 
Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве делителя программа должна 
корректно обработать эту ситуацию и не завершиться с ошибкой.'''


class Devision(Exception):
    def __init__(self, txt):
        self.txt = txt

    def div():
        try:
            divisible = float(input("Введите делимое - "))
            divisor = float(input("Введите делитель - "))
            if divisor == 0:
                raise Devision("на ноль делить нельзя")
            else:
                quotient = divisible / divisor
                return f'частное = {divisible / divisor}'

        except ValueError:
            return "Вы ввели не число"
        except Devision as err:
            return err


print(div())


'''Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список 
необходимо только числами. Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, 
пока пользователь сам не остановит работу скрипта, введя, например, команду «stop». 
При этом скрипт завершается, сформированный список с числами выводится на экран.
Подсказка: для этого задания примем, что пользователь может вводить только числа и строки. 
Во время ввода пользователем очередного элемента необходимо реализовать проверку типа элемента. 
Вносить его в список, только если введено число. Класс-исключение должен не позволить пользователю 
ввести текст (не число) и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.'''


class MyError(Exception):
    my_list = []

    def __init__(self, *args):
        self.args = args

    def detali(self):
        while True:
            try:
                numer = float(input('Введите число: '))
                self.my_list.append(numer)
                print(f'сохраненый список - {self.my_list}')
            except:
                print(f'это не число')
                choice = input(f'продолжить формирование списка? выберете: "ДА - Y" или "НЕТ - N"')
                if choice == 'N' or choice == 'n':
                    print(f'текущий список {self.my_list}')
                    break
                else:
                    self.detali()

a = MyError()
a.detali()

'''4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. 
А также класс «Оргтехника», который будет базовым для классов-наследников. 
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). 
В базовом классе определите параметры, общие для приведённых типов. 
В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.'''

class Warehouse:
  def __init__(self, product, price, quantity, units):
    self.product = product
    self.prise = price
    self.quantity = quantity
    self.units = units

class OfficeEquipment:
  def __init__(self, product, price, quantity, units, lists):
    self.product = product
    self.price = price
    self.quantity = quantity
    self.units = units
    self.lists = lists

class Printer(OfficeEquipment):
    def printing(self):
        return f'печать{self.lists}'

class Scanner(OfficeEquipment):
    def scaning(self):
        return f'сканирование{self.lists}'

class Copier(OfficeEquipment):
    def coping(self):
        return f'копирование{self.lists}'

printer = Printer('Hp', 7000, 3, 'шт', '15')
scaner = Scanner('Canon', 5400, 10, 'шт', '10')
copir = Copier('Xerox', 3000, 15, 'шт', '20')
printer.printing()
scaner.scaning()
copir.coping()

'''Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад 
и передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц 
оргтехники, а также других данных, можно использовать любую подходящую структуру (например, словарь).'''

class Warehouse:
  def __init__(self, product, price, quantity, units):
    self.product = product
    self.prise = price
    self.quantity = quantity
    self.units = units

class OfficeEquipment:
  def __init__(self, product, price, quantity, units, lists):
    self.product = product
    self.price = price
    self.quantity = quantity
    self.units = units
    self.lists = lists

  def income(self):
    try:
      product = input(f'введите название оборудования: ')
      price = input(f'Цена за товар: ')
      quantity = input(f'Введите колличество товара: ')
      units = input(f'ВВедите единицы измерения')
    except:
      return f'Ошибка ввода данных'


class Printer(OfficeEquipment):
  def printing(self):
    return f'печать{self.lists}'

class Scanner(OfficeEquipment):
    def caning(self):
        return f'сканирование{self.lists}'

class Copier(OfficeEquipment):
    def coping(self):
        return f'копирование{self.lists}'

printer = Printer('Hp', 7000, 3, 'шт', '15')
scaner = Scanner('Canon', 5400, 10, 'шт', '10')
copir = Copier('Xerox', 3000, 15, 'шт', '20')
print(printer.printing())
print(scaner.scaning())
print(copir.coping())

'''6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. 
Например, для указания количества принтеров, отправленных на склад, 
нельзя использовать строковый тип данных.'''

class Warehouse:
  def __init__(self, product, price, quantity, units):
    self.product = product
    self.prise = price
    self.quantity = quantity
    self.units = units
    self.spicok = {'продукт': self.product,
                   'цена':self.prise,
                   'колиичество':self.quantity,
                   'единицы измеренния': self.units }

class OfficeEquipment:
  my_lists = []
  def __init__(self, product, price, quantity, units, lists):
    self.product = product
    self.price = price
    self.quantity = quantity
    self.units = units
    self.lists = lists

  def __str__(self):
      return f' {self.product} - цена {self.prise} - количество на складе {self.quantity} {self.units}'

  def income(self):
    try:
      product = input(f'введите название оборудования: ')
      price = input(f'Цена за товар: ')
      quantity = input(f'Введите колличество товара: ')
      units = input(f'ВВедите единицы измерения')
      itog = {'продукт': product,
              'цена':price,
              'колиичество':quantity,
              'единицы измеренния': units }
      #self.spicok(itog)
      A = self.my_lists.append(self.spicok(itog))
    except:
      return f'Ошибка ввода данных'
      choice = input(f'продолжить формирование списка? выберете: "ДА - Y" или "НЕТ - N"')
      if choice == 'N' or choice == 'n':
        print(f'текущий список {A}')
        break
      else:
        return OfficeEquipment.income()

class Printer(OfficeEquipment):
  def printing(self):
    return f'печать{self.lists}'

class Scanner(OfficeEquipment):
    def caning(self):
        return f'сканирование{self.lists}'

class Copier(OfficeEquipment):
    def coping(self):
        return f'копирование{self.lists}'

printer = Printer('Hp', 7000, 3, 'шт', '15')
scaner = Scanner('Canon', 5400, 10, 'шт', '10')
copir = Copier('Xerox', 3000, 15, 'шт', '20')
print(printer.printing())
print(scaner.scaning())
print(copir.coping())

'''7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». 
Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта. 
Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных 
экземпляров. Проверьте корректность полученного результата.'''

class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'Сумма равна: {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        return f'Произведение равно: {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'


c_1 = ComplexNumber(5, -3)
c_2 = ComplexNumber(4, 7)
print(c_1 )
print(c_2)
print(c_1 + c_2)
print(c_1 * c_2)