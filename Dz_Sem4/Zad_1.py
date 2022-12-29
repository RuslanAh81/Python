# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random
import random


def write_file(new_equation):
    with open('file1.txt', 'w') as data:
        data.write(new_equation)


def rnd():
    return random.randint(-100, 100)


def create_mn(k):
    lst = [rnd() for i in range(k+1)]
    return lst


def create_str(sp):
    lst = sp[::-1]
    eq = ''
    if len(lst) < 1:
        eq = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                eq += f'{lst[i]}*x^{len(lst)-i-1}'
                if lst[i+1] != 0:
                    eq += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                eq += f'{lst[i]}*x'
                if lst[i+1] != 0:
                    eq += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                eq += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                eq += ' = 0'
    return eq



k = int(input("Введите натуральную степень k = "))
koef = create_mn(k)

new_equation = create_str(koef)
new_equation = new_equation.replace('+ -', '- ').replace('1*x', 'x')


print(koef)
print(new_equation)
write_file(new_equation)