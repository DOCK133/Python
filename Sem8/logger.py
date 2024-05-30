from data_create import input_user_data

def input_data():
    name, surname, phone, adress = input_user_data()
    var = int(input(f'\nВ каком формате записать данные?\n'
                    f'1 Вариант‚:\n'
                    f'{name}\n'
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{adress}\n\n'
                    f'2 Вариант:\n'
                    f'{name};{surname};{phone};{adress}\n\n'
                    f'\nВаш выбор: '
                    ))
    if var == 1:
        with open("data_first_variant.csv", "a", encoding="utf-8") as file:
            file.write( f'{name}\n'
                        f'{surname}\n'
                        f'{phone}\n'
                        f'{adress}\n\n')
    else:
        with open("data_second_variant.csv", "a", encoding="utf-8") as file:
            file.write(f'{name};{surname};{phone};{adress}\n\n')



def print_data():
    print("1 файл: ")
    with open("data_first_variant.csv", "r", encoding="utf-8") as file:
        data = file.readlines()
        for i in data:
            print(i, end="")

    print("2 файл: ")
    with open("data_second_variant.csv", "r", encoding="utf-8") as file:
        data = file.readlines()
        for i in data:
            if i != '\n':
                print(i, end="")

def modify_data():
    name = input("Введите имя или фамилию, данные которого нужно изменить: ")
    data = [{"имя": "Иван", "фамилия": "Иванов", "возраст": 25}]
    for record in data:
        if record["имя"] == name or record["фамилия"] == name:
            new_name = input("Введите новое имя: ")
            new_surname = input("Введите новую фамилию: ")
            # Найдена соответствующая запись
            # Запросить новые данные
            record["имя"] = new_name
            record["фамилия"] = new_surname
            print("Данные изменены успешно.")
        else:
            print("Запись с указанным именем или фамилией не найдена.")


def delete_data():
    name = input("Введите имя или фамилию, данные которого нужно удалить: ")
      
    with open('data_first_variant.csv', 'w', encoding="utf-8") as file:
        reader = file.readlines()
        data = list(reader)
    
    deleted_count = 0
    
    with open('data_first_variant.csv', 'w', newline='') as file:
        writer = delete_data(file)
        for row in data:
            if name.lower() not in [cell.lower() for cell in row]:
                writer.writerow(row)
            else:
                deleted_count += 1
    
    if deleted_count > 0:
        print("Данные удалены успешно.")
    else:
        print("Нет данных для удаления по указанному имени или фамилии.")
    print("Данные удалены успешно.")