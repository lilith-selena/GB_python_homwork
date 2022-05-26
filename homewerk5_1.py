'''1. Создать программный файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая строка.'''
# Версия №1
txt_fail = open("text.txt",'w')
txt_fail.write("Клара у Карлла\nУкрала кораллы,\nа Карлл у Клары\nУкрал кларнет\n")
txt_fail.close()
txt_fail = open("text.txt",'r')
content = txt_fail.readlines()
print(content)
txt_fail.close()

# Версия №2
import os
os.remove("text.txt")

txt_fail = open("text.txt",'w')
while True:
    s = input("ВВедите текст")
    if s == '': break
    txt_fail.write(s+'\n')
txt_fail.close()

txt_fail = open('text.txt', 'r')
content = txt_fail.readlines()
print(content)
txt_fail.close()

"""2. Создать текстовый файл (не программно), 
сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке."""

#открыть существующий фаил
txt_fail = open('text.txt', 'r')
# присвоить переменной данные из файла считывать по строчкам
count=0
for line in txt_fail:
  count+=1
  print(line)
print(count)
#считать элементы в строчках (почему то =0) похоже надо через сплит
content = txt_fail.readline()
c=len(content)
print(c)
txt_fail.close()

"""Создать текстовый файл (не программно). Построчно записать фамилии сотрудников 
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет 
оклад менее 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней 
величины дохода сотрудников.

Пример файла:
Иванов 23543.12
Петров 13749.32"""
salary = open('salary.txt', 'r')
S = (salary.read()).split('\n')
print(S)
surname = []
SUMMA = 0
count = 0
for i in range(len(S)):
  tmp = S[i].split(' ')
  summa = int(tmp[1])
  surname0 = str(tmp[0])
  if summa>=20000:
    SUMMA += summa
    count +=1
    surname.append(surname0)
print(f'Сотрудники с ЗП выше 20т.р. {surname}')
print("Средняяя ЗП у этих сотрдников",SUMMA/count )
salary.close()
# в колабе отлично все идет, а в PC пишет File "\AppData\Local\Programs\Python\Python310\lib\encodings\cp1251.py", line 23, in decode
#     return codecs.charmap_decode(input,self.errors,decoding_table)[0]
# UnicodeDecodeError: 'charmap' codec can't decode byte 0x98 in position 1: character maps to <undefined> - пока не понимю почему
'''4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные. 
При этом английские числительные должны заменяться на русские. Новый блок строк
должен записываться в новый текстовый файл.'''
numera = {'zero':'ноль', 'one':'один', 'two':'два', 'three':'три', 'four':'четыре', 'five':'пять', 'six':'шесть', 'seven':'семь',
            'eight':'восемь', 'nine':'девять', 'ten':'десять'}
'''nuw_numerals = ()'''
'''numeralsX = open('numerals.txt', 'w')
numerals = (numeralsX.read()).split('\n')
print(numerals)
for i in range(len(numerals)):
  tmp = numerals[i].split(' - ')
  symbols = tmp[0]
  for j in range(numera):
    if symbols == numera.keys(j):
       symbols2 = numera.values()
    else:
        break
    stroka = str(symbols2) + str(" - ") + str(tmp[1])
    print(stroka)
su''' # Запуталась надо еще подумать


def translate_list(src_path, dst_path): #Помогли надо разбираться
    decoder = {'Zero': 'ноль', 'One': 'один', 'Two': 'два', 'Three': 'три', 'Four': 'четыре', 'Five': 'пять',
               'Six': 'шесть', 'Seven': 'семь',
               'Eight': 'восемь', 'Nine': 'девять', 'Ten': 'десять'}
    try:
        with open(src_path, 'r') as src_f, open(dst_path, 'w') as dst_f:
            for line in src_f:
                dst_f.write(' '.join(decoder[word] if word in decoder.keys() else word for word in line.split(' ')))
    except Exception as err:
        print(f'Unexpected error: {err}')


def create_src_file(file_path):
    with open(file_path, 'w') as f:
        f.write('One - 1\nTwo - 2\nThree - 3\nFour - 4')


if __name__ == '__main__':
    import os.path

    src_name = 'task4_src.txt'
    dst_name = 'task4_dst.txt'

    if not os.path.exists(src_name):
        create_src_file(src_name)

    translate_list(src_name, dst_name)

my_f = open("task4_dst.txt", "r")
content = my_f.read()
print(content)
my_f.close
 
'''5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
 Программа должна подсчитывать сумму чисел в файле и выводить её на экран.'''
my_f = open('test.txt', 'w')
line = input('Введите набор чисел, разделённых пробелами')
my_f.writelines(line)
my_f.close()

my_f = open('test.txt', 'r')
content = (my_f.read().split(' '))
print(type(content))
print(content)
summ = 0
for i in range(len(content)):
  summ += int(content[i])
print((summ))
my_f.close()

'''6. Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет 
и наличие лекционных, практических и лабораторных занятий по предмету. Сюда должно входить 
и количество занятий. Необязательно, чтобы для каждого предмета были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести его на экран.
Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}'''
def calculate_hours(file_path):

    result = {}
    try:
        with open(file_path, 'r') as f:
            for line in f:
                subject, numbers = line.split(':')
                subject_sum = sum(int(n) for word in numbers.split() for n in word.split('(') if n.isdigit())
                result[subject] = subject_sum
    except Exception as err:
        print('Unexpected error:', err)
    return result


if __name__ == '__main__':
    from pprint import pprint
    res_dict = calculate_hours('task6_test.txt')
    pprint(res_dict, width=1)

def calculate_hours(file_path):
    """
    Calculate total hours by subject
    :param file_path: str
    :return: dict
    """
    result = {}
    try:
        with open(file_path, 'r') as f:
            for line in f:
                subject, numbers = line.split(':')
                subject_sum = sum(int(n) for word in numbers.split() for n in word.split('(') if n.isdigit())
                result[subject] = subject_sum
    except Exception as err:
        print('Unexpected error:', err)
    return result


if __name__ == '__main__':
    from pprint import pprint
    res_dict = calculate_hours('task6_test.txt')
    pprint(res_dict, width=1)


import json

"""
Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна
содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""


def calculate_profit(src_file, dst_file): #помогли.надо разобраться
    res = []
    res_dict = {}
    positive_profit_count = 0
    total_profit = 0

    with open(src_file, 'r') as f:
        for line in f:
            firm, _, rev, exp = line[:-1].split()
            profit = int(rev) - int(exp)
            if profit > 0:
                total_profit += profit
                positive_profit_count += 1
            res_dict[firm] = profit
    avr_profit = total_profit / positive_profit_count if positive_profit_count else 0
    res.append(res_dict)
    res.append({'average_profit': avr_profit})

    with open(dst_file, 'w') as f:
        json.dump(res, f)


def generate_sample_file(file_path, samples):

    with open(file_path, 'w') as f:
        for t in samples:
            f.write(' '.join(map(str, t)))
            f.write('\n')


if __name__ == '__main__':
    import os
    from pprint import pprint

    samples_file = 'task7_samples.txt'
    result_file = 'task7_profit.json'
    if not os.path.exists(samples_file):
        samples_example = [("firm_1", "OOO", 10000, 5000),
                           ("firm_2", "Gmbh", 20000, 7000),
                           ("firm_3", "LLC", 8000, 20000)]
        generate_sample_file(samples_file, samples_example)

    calculate_profit(samples_file, result_file)
    with open(result_file, 'r') as f:
        js = json.load(f)
        pprint(js, width=1)