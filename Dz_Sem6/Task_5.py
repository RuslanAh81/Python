
"""Эадайте список из  n чисел последовательности (1+1/n)**n выведите его на экран, а так же сумму его элементов"""

# n = int(input('input num :'))
# m = []
# s = 0
# for i in range(1, n+1):
#     el = round((1+1/int(i))**int(i), 2)
#     m.append(el)
#     s += el
#
# print(m)
# print(s)

n = int(input('ведите число N :'))
my_lst = [(1+1/int(i))**int(i) for i in range(1, n+1)]
''' Не смог вписать округление в выражение выше '''
# print(my_lst)
print(f'сумма последовательности равна : {round(sum(my_lst),2)}')