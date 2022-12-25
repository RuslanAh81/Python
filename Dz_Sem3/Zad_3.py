"""Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным
значением дробной части элементов, отличной от 0.
Пример:
[1.1, 1.2, 3.1, 5, 10.01] => 0.19"""

lst = [1.1, -1.4, 76, 3.1, 5, 10.01]
my_max = round(lst[0] % 1, 2)
for i in range(len(lst)):
    my_min = round(lst[0] % 1, 2)

    if my_max < round(lst[i] % 1, 2):
        my_max = round((lst[i] % 1), 2)
    if my_min > round(lst[i] % 1, 2):
        # if my_min == 0:
        #     continue
        my_min = round((lst[i] % 1), 2)

print(f'my_max={my_max}')
print(f'my_min={my_min}')
n = my_max - my_min
print(n)