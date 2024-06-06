# Задача 40
# Дан файл california_housing_train.csv. Определить среднюю стоимость дома,
# где количество людей от 0 до 500 (population) и сохранить ее в переменную avg.
# Используйте модуль pandas.

import pandas as pd # Импорт библиотеки pandas

df = pd.read_csv('california_housing_train.csv') # Загрузка файла
avg = df[(df['population'] > 0) & (df['population'] < 500)]['median_house_value'].mean() # Вычисление средней стоимости дома