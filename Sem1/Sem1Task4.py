# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они
# сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов, а Катя
# сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 6  -> 1  4  1
# 24 -> 4  16 4
# 60 -> 10 40 10

birds = int(input("Введите кол-во журавликов: "))

x = birds // 6
y = ( x + x ) * 2

print('Петя и Сережа сделали по', x, 'шт')
print('Маша сделала', y, 'шт')

# Решение №2

birds = int(input("Введите кол-во журавликов: "))

p = (birds // 3) // 2
k = (birds // 3) // 2
m = (birds // 3) * 2

print('Петя сделал', p, 'шт')
print('Коля сделал', k, 'шт')
print('Маша сделала', m, 'шт')

# Решение задачи самопроверки

n = 120

# Введите ваше решение ниже

n1 = n // 6
n2 = n // 6
n3 = (n // 6) * 4

print(n1, n3, n2)

# Решение автотеста

n1 = n // 6
n2 = n // 6
n3 = (n // 6) * 4
print(n1, n3, n2)