

"""Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
[2, 3, 4, 5, 6] => [12, 15, 16];
[2, 3, 5, 6] => [12, 15]"""

a = [2, -3, 4, 5, 6]
le = len(a)
mult = 0
le2 = le % 2
if le2 != 0:
    new_lst = [a[i] * a[le - 1 - i] for i in range(le // 2+1)]

    print(new_lst)
    print(le2)

else:
    new_lst = [a[i] * a[le - 1 - i] for i in range(le // 2)]
    print(new_lst)

# for i in range(le//2):
    # print(i)
    # print(le-1 - i)
