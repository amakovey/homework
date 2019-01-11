__author__ = 'Маковей А.Н.'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.
print ("lesson 1")
x = int(58378)
x1 = str(x)
l=len(x1)
max = x1[0]
for i in range(1,l):
	if x1[i]> max:
		max = x1[i]
print(max)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.
print ('lesson 2')
a = int(input())
b = int(input())
a,b = b,a
print (a,b)


# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4
print ('lesson 3')
import math
print ('Enter a')
a = int (input())
print ('Enter b')
b = int (input())
print ('Enter c')
c = int (input())
d = b*b-4*a*c
if d<0:
	print ('Корни не вещественны')
else:
	x1 = (-1*b+math.sqrt(d))/2*a*c
	x2 = (-1*b-math.sqrt(d))/2*a*c
	print ('Корень х1 =',x1)
	print ('Корень х2 =',x2)
