
'''Сформировать список из  N членов последовательности.
Для N = 5: 1, -3, 9, -27, 81 и т.д.'''

num = int(input ('ведите число:'))

m_lst = [(-3)**i for i in range(num)]

print(f'Итоговая последовательность: {m_lst}')