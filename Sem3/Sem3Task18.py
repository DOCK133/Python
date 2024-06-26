# Задача №20
# Требуется найти в массиве list_1 самый близкий по значению элемент 
# к заданному числу k и вывести его.
# Считать, что такой элемент может быть только один. 
# Если значение k совпадает с этим элементом - выведите его.
# Пример:
# list_1 = [1, 2, 3, 4, 5]
# k = 6

list_1 = [1, 2, 3, 4, 5]

k = 6

number = list_1[0]
for i in list_1:
    if abs(k - i) <= abs(k - number):
        number = i
print(number)

# Решение автотеста

m = abs(k - list_1[0])  # модуль числа
number = list_1[0]
for i in range(1, len(list_1)):
    if m > abs(list_1[i] - k):
        m = abs(list_1[i] - k)
        number = list_1[i]
print(number)