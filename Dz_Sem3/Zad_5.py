""""Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Пример:
для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи"""
fibo = [1, 0, 1]
fib1 = 0
fib2 = 1

n = 8                  #'''input("Номер элемента ряда Фибоначчи: ")'''
n = int(n) - 1
new_fib = []
negafib = []
while n > 0:
    fib1, fib2 = fib2, fib1 + fib2
    n -= 1
    new_fib.append(fib2)
    ''' Отношнние к нормальной,положительной последовательности '''
    negafib.append((-1)**(n+1) * fib2)
    # print("Значение этого элемента:", fib2)
    # print(fib2, end=' ')
# print(new_fib)
# print(negafib[::-1])

print(negafib[::-1]+fibo+new_fib)