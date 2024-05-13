# Задача 22
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются 
# в обоих наборах. Пользователь вводит 2 числа. n - кол-во элементов первого 
# множества. m - кол-во элементов второго множества. Затем пользователь вводит 
# сами элементы множеств.
# Пример:
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

var1 = '5 4' 
var2 = '1 3 5 7 9' 
var3 = '2 3 4 5' 

# Введите ваше решение ниже

setVar1 = set()
setVar2 = set()
for i in var2.split():
    setVar1.add(i)
for i in var3.split():
    setVar2.add(i)
list = list(setVar1.intersection(setVar2))
list.sort()
print(*list)

# Решение автотеста

mol = [int(x) for x in var1.split()]
n = mol[0]
m = mol[1]
set_1 = set()
set_2 = set()
list_1 = list()
a = [int(x) for x in var2.split()]
k = set(a)
for i in k:
   set_1.add(i)
b = [int(x) for x in var3.split()]
k1 = set(b)
for i in k1:
   set_2.add(i)
lok = set_1 & set_2
kool = list(lok)
kool.sort()
for i in kool:
   print(i, end=' ')