from prettytable import PrettyTable
import sqlite3

vault_FIO = []
vault_date_birth = []
vault_salary = []
my_table = PrettyTable()
my_table.field_names = ["No.", "ФИО", "Birthday", "Salary"]


def print_employee_list():
    my_table.clear_rows()

    # Устанавливаем соединение с базой данных
    connection = sqlite3.connect('employees_database.db')
    cursor = connection.cursor()

    # Выбираем и сортируем пользователей по возрасту по убыванию
    cursor.execute('SELECT * FROM employees')
    results = cursor.fetchall()

    if len(results) > 0:
        print('Список сотрудников:')
        for i in range(len(results)):
            my_table.add_row([i + 1, results[i][1], results[i][2], results[i][3]])
        print(my_table)
    else:
        print(f'Список сотрудников пуст!')
    # Сохраняем изменения и закрываем соединение
    connection.close()
    print('\n')
    return results


def edit_employee():
    my_table.clear_rows()  # очищаем таблицу перед очередным заполнением

    # Устанавливаем соединение с базой данных
    connection = sqlite3.connect('employees_database.db')
    cursor = connection.cursor()

    # Выбираем и сортируем пользователей по возрасту по убыванию
    cursor.execute('SELECT * FROM employees')
    results = cursor.fetchall()

    if len(results) > 0:
        print('Список сотрудников:')
        for i in range(len(results)):
            my_table.add_row([i + 1, results[i][1], results[i][2], results[i][3]])
        print(my_table)
    else:
        print(f'Список сотрудников пуст!')
    print('\n')

    print('Выберете сотрудника для редактирования, указав его номер в списке')
    choose = input()
    id_employee = results[int(choose) - 1][0]
    connection.close()
    print('Введите номер желаемого параметра для редактирования')
    print('1 - ФИО, 2 - Дата Рождения, 3 - ЗП')
    return id_employee


def edit_employee_FIO(id_employee):
    # Устанавливаем соединение с базой данных
    connection = sqlite3.connect('employees_database.db')
    cursor = connection.cursor()

    # Добавляем нового пользователя
    cursor.execute('UPDATE Employees SET employee_FIO = ? WHERE employee_id = ?', (input(), id_employee))

    # Сохраняем изменения и закрываем соединение
    connection.commit()
    connection.close()


def edit_employee_birthday(id_employee):
    # Устанавливаем соединение с базой данных
    connection = sqlite3.connect('employees_database.db')
    cursor = connection.cursor()

    # Добавляем нового пользователя
    cursor.execute('UPDATE Employees SET employee_birthday = ? WHERE employee_id = ?', (input(), id_employee))

    # Сохраняем изменения и закрываем соединение
    connection.commit()
    connection.close()


def edit_employee_salary(id_employee):
    # Устанавливаем соединение с базой данных
    connection = sqlite3.connect('employees_database.db')
    cursor = connection.cursor()

    # Добавляем нового пользователя
    cursor.execute('UPDATE Employees SET employee_salary = ? WHERE employee_id = ?', (input(), id_employee))

    # Сохраняем изменения и закрываем соединение
    connection.commit()
    connection.close()


def delete_employee(id_employee):
    # Устанавливаем соединение с базой данных
    connection = sqlite3.connect('employees_database.db')
    cursor = connection.cursor()

    # Добавляем нового пользователя
    cursor.execute('DELETE FROM Employees WHERE employee_id = ?', (id_employee,))

    # Сохраняем изменения и закрываем соединение
    connection.commit()
    connection.close()


def print_menu():
    print('Чтобы выбрать пункт меню, введите нужную цифру из списка ниже:')
    print('1) Посмотреть списов всех сотрудников')
    print('2) Добавить информацию о сотруднике')
    print('3) Отредактировать информацию о сотруднике')
    print('4) Удалить информацию о сотруднике')


def add_employee():
    print('Введите ФИО сотрудника')
    employee_FIO = (input())
    print('Введите Дату рождения сотрудника в формате ДД.ММ.ГГГГ')
    employee_birthday = (input())
    print('Введите "ЗП" сотрудника')
    employee_salary = (input())
    print('Сотрудник добавлен!\n')

    # Устанавливаем соединение с базой данных
    connection = sqlite3.connect('employees_database.db')
    cursor = connection.cursor()

    # Добавляем нового пользователя
    cursor.execute('INSERT INTO employees (employee_FIO, employee_birthday, employee_salary) VALUES (?, ?, ?)',
                   (employee_FIO, employee_birthday, employee_salary))

    # Сохраняем изменения и закрываем соединение
    connection.commit()
    connection.close()


def delete_employee_start():
    my_table.clear_rows()  # очищаем таблицу перед очередным заполнением

    # Устанавливаем соединение с базой данных
    connection = sqlite3.connect('employees_database.db')
    cursor = connection.cursor()

    # Выбираем и сортируем пользователей по возрасту по убыванию
    cursor.execute('SELECT * FROM employees')
    results = cursor.fetchall()

    if len(results) > 0:
        print('Список сотрудников:')
        for i in range(len(results)):
            my_table.add_row([i + 1, results[i][1], results[i][2], results[i][3]])
        print(my_table)
    else:
        print(f'Список сотрудников пуст!')
    print('\n')

    print('Выберете сотрудника для удаления, указав его номер')
    choose = input()
    id_employee = results[int(choose) - 1][0]
    deleted_user = results[int(choose) - 1][1]
    connection.close()
    return id_employee, deleted_user


while True:
    print_menu()
    code = input()
    if code == '1':
        print_employee_list()
    elif code == '2':  # Добавление сотрудника
        add_employee()

    elif code == '3':  # Редактирование сотрудника
        id_employee = edit_employee()
        input_data = input()
        if input_data == '1':
            print('Введите новое ФИО сотрудника')
            edit_employee_FIO(id_employee)
            print('ФИО сотрудника обновлена!\n')
        elif input_data == '2':
            print('Введите новую дату рождения сотрудника')
            edit_employee_birthday(id_employee)
            print('Дата рождения сотрудника обновлена!\n')
        elif input_data == '3':
            print('Введите новую "ЗП" сотрудника')
            edit_employee_salary(id_employee)
            print('ЗП сотрудника обновлена!\n')
        else:
            print('Вы ввели неправильное значение!')
            print('Обновление данных прервано!\n')
    elif code == '4':
        id_employee, deleted_user = delete_employee_start()
        delete_employee(id_employee)
        print(f'Сотрудник "{deleted_user}" удалён из списка\n')
    else:
        print('Вы ввели неправильное значение!\n')
