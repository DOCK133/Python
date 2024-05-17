# Функция filter
# Функция filter() применяет указанную функцию к каждому элементу итерируемого 
# объекта и возвращает итератор с теми объектами, для которых функция 
# вернула True.

data = [15, 65, 9, 36, 175]
res = list(filter(lambda x: x % 10 == 5, data))
print(res)