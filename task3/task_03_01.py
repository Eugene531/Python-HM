# Глобальная область видимости
phone_book = {}


# Функция добавления в телефонную книгу
def add_number():
    name = input()
    number = input()
    phone_book[name] = phone_book.get(name, []) + [number]


# Функция получения данных из телефонной книги
def get_number():
    name = input()
    print('имя'.ljust(12), 'номер')
    for number in phone_book.get(name, []):
        print(name.ljust(12), number)


# Функия удаления записей из телефонной книги
def remove_number():
    name = input()
    if name in phone_book:
        phone_book.pop(name)
    else:
        print('Человека нет в справочнике')


if __name__ == '__main__':
    # Функции
    funs = {
            '1': add_number,
            '2': get_number,
            '3': remove_number
        }
    
    # Вызов функции в зависимости от выбора пользователя
    while True:
        action = input(
            '1. Добавить номер и имя человека\n'
            '2. Вывести номера человека по имени\n'
            '3. Удалить номера по имени.\n'
            )
        
        funs[action]()
        

