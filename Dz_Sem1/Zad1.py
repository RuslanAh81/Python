# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#
# Пример:
#
# - 6 -> да
# - 7 -> да
# - 1 -> нет

a, b = 6, 7
"""a, b - типа выходные"""
day = int(input("Введите день недели : "))

if day < 1 or day > 7:
    print("число вне диапозона дня недели ")
else:

    if day == a or day == b:
        print('Выходной')

    else:
        print('Рабочий')

