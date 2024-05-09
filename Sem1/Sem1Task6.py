# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались 
# за проезд и получали билет с номером. Счастливым билетом называют такой билет 
# с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

# Решение задачи самопроверки

billet = input('Введите номер билета: ')

left = int(billet[0]) + int(billet[1]) + int(billet[2])
right = int(billet[3]) + int(billet[4]) + int(billet[5])
if left == right:
    print('Yes')
else:
    print('NO')

# Решение №2

billet = input('Введите 6-значный номер билета: ')
if len(billet) != 6:
    print(f'Число {billet} не 6-ти значное')
else:
    res1 = 0
    res2 = 0
    for i in range(len(billet)//2):
        res1 += int(billet[i])
        res2 += int(billet[len(billet)//2 + i])
    if res1 == res2:
        print(f'{billet} счастливый номер')
    else:
        print(f'{billet} не счастливый номер')

# Решение автотеста

n1 = n // 100000
n2 = (n % 100000) // 10000
n3 = (n % 10000) // 1000
n4 = (n % 1000) // 100
n5 = (n % 100) // 10
n6 = n % 10
if n1 + n2 + n3 == n4 + n5 + n6:
    print('yes')
else:
    print('no')