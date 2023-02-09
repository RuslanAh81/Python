import numpy as np
import matplotlib.pyplot as plt

a,b,c,d, e =-12, -18, 5, 10,-30
limit = 10
step =0.01
line_style = '-'
color='b'
direct_up = True

def switch_line():
    global line_style
    if line_style == '-':
        line_style = '--'
    else:
        line_style = '-'
    return line_style

def switch_color():
    global color
    if color == 'b':
        color = 'r'
    else:
        color = 'b'
    return color

def my_foo(x):
    func = a*x**4 * np.sin(np.cos(x)) + b*x**3 + c*x**2 + d*x + e
    return func

x= np.arange(-limit, limit, step)
x_change = [(-limit, 'limit')]
for i in range(len(x)-1):
    if my_foo(x[i])>0 and my_foo(x[i+1])<0 or my_foo((x[i]))<0 and my_foo(x[i+1])>0:
        x_acr = np.arange(x[i], x[i+1], 0.000001)
        for j in range(len(x_acr)-1):
            if my_foo(x_acr[j])>0 and my_foo(x_acr[j+1])<0 or my_foo(x_acr[j])<0 and my_foo(x_acr[j+1])>0:
                x_change.append((x[i], 'zero'))
    if direct_up:
        if my_foo(x[i]) > my_foo(x[i + 1]):
            direct_up = False
            x_change.append((x[i], 'dir'))
    else:
        if my_foo(x[i])< my_foo(x[i+1]):
            direct_up = True
            x_change.append((x[i], 'dir'))


print(x_change)

x_change.append((limit, 'limit'))
for i in range(len(x_change)-1):
    cur_x = np.arange(x_change[i][0], x_change[i + 1][0], step)
    if x_change[i][1] == 'zero':
        plt.plot(x_change[i][0], my_foo(x_change[i][0]))
        plt.rcParams['lines.linestyle']=switch_line()
        plt.plot(cur_x, my_foo(cur_x), color)
    else:
        plt.plot(cur_x, my_foo(cur_x), switch_color())
plt.plot(-3, my_foo(-3),'yx')


roots = []
for x in x_change:
    if x[1] == 'zero':
        roots.append(str(round(x[0], 2)))
        plt.plot(x[0], my_foo(x[0]), 'go')

plt.rcParams['lines.linestyle'] = '-'
plt.plot(0, 0, 'b', label='Убывание > 0')
plt.plot(0, 0, 'r', label='Возрастание > 0')
plt.rcParams['lines.linestyle'] = '--'
plt.plot(0, 0, 'b', label='Убывание < 0')
plt.plot(0, 0, 'r', label='Возрастание < 0')
plt.title(f'Корни на промежутке [{-limit};{limit}]: {", ".join(roots)}')
plt.legend()
plt.show()