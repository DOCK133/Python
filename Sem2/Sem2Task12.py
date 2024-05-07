# Задача № 12
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа 
# X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает 
# две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

s = 12
p = 27

for i in range(1,1001):
    for j in range(1,1001):
        if i <= j and i + j == s and i * j == p:
            print(f'{i} {j}')
print('----------')