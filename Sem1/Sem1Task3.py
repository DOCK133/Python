# Задача №3. Решение в группах
# В некоторой школе решили набрать три новых математических
# класса и оборудовать кабинеты для них новыми партами.
# За каждой партой может сидеть два учащихся. Известно
# количество учащихся в каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

# Вариант 1

class_1 = int(input("Введите кол-во учеников 1 класса: "))
class_2 = int(input("Введите кол-во учеников 2 класса: "))
class_3 = int(input("Введите кол-во учеников 3 класса: "))

parts_1 = (class_1 + 1) // 2
parts_2 = (class_2 + 1) // 2
parts_3 = (class_3 + 2 - 1) // 2

parts_all = (parts_1 + parts_2 + parts_3)

print("Кол-во парт:", parts_all)

parts_1 = class_1 // 2 + class_1 % 2

# Вариант 2
a = int(input())
b = int(input())
c = int(input())

s1 = (a + 1)//2
s2 = (b + 1)//2
s3 = (c + 1)//2

print(s1 + s2 + s3)