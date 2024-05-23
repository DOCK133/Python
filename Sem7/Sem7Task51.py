# Задача №51. Решение в группах
# Напишите функцию same_by(characteristic, objects), которая проверяет, 
# все ли объекты имеют одинаковое значение некоторой характеристики, и возвращают 
# True, если это так. Если значение характеристики для разных объектов 
# отличается - то False. Для пустого набора объектов, функция должна возвращать 
# True. Аргумент characteristic - это функция, которая принимает объект и 
# вычисляет его характеристику.
# Ввод:                                       Вывод:
# values = [0, 2, 10, 6]                      same
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)

def same_by(characteristic, objects):   # функция, которая проверяет, все ли объекты имеют одинаковое значение характеристики, и возвращает True, если это так. Если значение характеристики для разных объектов отличается - то False.
        result = True   # переменная, которая будет хранить результат
        list_1 = [characteristic(x) for x in objects]   # список характеристик объектов
        for i in range(len(list_1) - 1):    # перебор списка
                if list_1[i] != list_1[i + 1]:  # проверка на одинаковость
                        result = False
        return result

values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
        print('same')
else:
        print('different')