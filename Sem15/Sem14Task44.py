# Задание 44
# В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего 
# из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это 
# сделать без get_dummies?
# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI'lst})
# data.head()

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI'lst})
data.head()

# Получение уникальных значений столбца 'whoAmI'
unique_values = data['whoAmI'].unique()

# Создание новых столбцов с преобразованными данными в one-hot формат
for value in unique_values:
    data[value] = (data['whoAmI'] == value).astype(int)

data.head()