# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

n = int(input("Введите трехзначное число: "))
print(n // 100 + n // 10 % 10 + n % 10)

# решение №2

num = int(input("Введите 3-х значное число: "))
res = 0
if len(num) == 3:
    for i in num:
        res += int(i)
    print(res)
else:
    print('Вы ввели не 3-х значное число')

    # Решение задачи самопроверки

n = 100

# Введите ваше решение ниже

n1 = n // 100 
n2 = (n % 100) // 10 
n3 = n % 10 
res = n1 + n2 + n3

# Решение автотеста

n1 = n // 100 # Нахождение первой цифры числа
n2 = (n % 100) // 10 # Нахождение второй цифры числа
n3 = n % 10 # Нахождение третьей цифры числа
res = n1 + n2 + n3