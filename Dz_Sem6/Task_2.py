"""Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
 второй и предпоследний и т.д. Пример:[2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]"""

# def mult(my_lst):
#     return [my_lst[i]*my_lst[-i-1] for i in range(len(my_lst)//2+len(my_lst)%2)]

l = lambda my_lst: [my_lst[i]*my_lst[-i-1] for i in range(len(my_lst)//2+len(my_lst) % 2)]
my_lst = [2, 3, 5, 6]

print(l(my_lst))