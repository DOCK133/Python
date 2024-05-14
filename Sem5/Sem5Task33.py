# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и хочет заменить все свои 
# минимальные оценки на максимальные. Напишите программу, которая заменяет 
# оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

n = int(input())

list_1 = list()

for i in range(n):
        x = int(input())
        list_1.append(x)

max_n = max(list_1)
min_n = min(list_1)

for i in range(len(list_1)):
        if list_1[i] == max_n:
                list_1[i] = min_n

print(list_1)