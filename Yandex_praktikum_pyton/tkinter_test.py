from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo

from prettytable import PrettyTable
import sqlite3

my_table = PrettyTable()
my_table.field_names = ["No.", "ФИО", "Birthday", "Salary"]
cmb_employees_value = []

'''
# Печать списка сотрудников в окне (на удаление)
def print_employee_list():
    my_table.clear_rows()

    # Устанавливаем соединение с базой данных
    connection = sqlite3.connect('employees_database.db')
    cursor = connection.cursor()

    # Выбираем и сортируем пользователей по возрасту по убыванию
    cursor.execute('SELECT * FROM employees')
    results = cursor.fetchall()

    if len(results) > 0:
        for i in range(len(results)):
            my_table.add_row([i + 1, results[i][1], results[i][2], results[i][3]])

    else:
        print(f'Список сотрудников пуст!')
    # Сохраняем изменения и закрываем соединение
    connection.close()
    print('\n')
    return results
'''


# Открываем окно сотрудников и выводим их список
def open_employee_list_window():
    window_employee_list = Tk()
    window_employee_list.title("Список сотрудников")
    window_employee_list.geometry("700x600")

    my_table.clear_rows()

    # Устанавливаем соединение с базой данных
    connection = sqlite3.connect('employees_database.db')
    cursor = connection.cursor()

    # Выбираем и сортируем пользователей по возрасту по убыванию
    cursor.execute('SELECT * FROM employees')
    results = cursor.fetchall()

    if len(results) > 0:
        for i in range(len(results)):
            my_table.add_row([i + 1, results[i][1], results[i][2], results[i][3]])
    else:
        print(f'Список сотрудников пуст!')
    # Сохраняем изменения и закрываем соединение
    connection.close()
    print('\n')

    lbl_window_employee_list = ttk.Label(window_employee_list, text=my_table, justify=LEFT)  # создаем текстовую метку
    lbl_window_employee_list.pack(anchor=CENTER, expand=1)


# Открываем окно добавления сотрудников, вводим данные и добавляем
def open_employee_insert_window():
    # Функция обработки добавления сотрудников в БД
    def employee_insert():
        employee_fio = (ent_fio.get())
        employee_birthday = (ent_birthday.get())
        employee_salary = (ent_salary.get())
        # Устанавливаем соединение с базой данных
        connection = sqlite3.connect('employees_database.db')
        cursor = connection.cursor()

        # Добавляем нового пользователя
        cursor.execute('INSERT INTO employees (employee_FIO, employee_birthday, employee_salary) VALUES (?, ?, ?)',
                       (employee_fio, employee_birthday, employee_salary))

        # Сохраняем изменения и закрываем соединение
        connection.commit()
        connection.close()
        n = '\n'
        showinfo(title="Сотрудник добавлен",
                 message=f'Сотрудник{n}ФИО: "{employee_fio}"{n}День Рожднения: {employee_birthday}{n} ЗП: "{employee_salary}"{n}Успешно добавлен!')
        ent_fio.delete(0, END)
        ent_birthday.delete(0, END)
        ent_salary.delete(0, END)

    window_employee_insert = Tk()
    window_employee_insert.title("Добавление сотрудников")
    window_employee_insert.geometry("700x600")
    lbl_fio = Label(window_employee_insert, text="Введите фамилию нового сотрудника")
    lbl_fio.pack()
    ent_fio = Entry(window_employee_insert, width=50)
    ent_fio.pack()
    lbl_birthday = Label(window_employee_insert, text="Введите дату рождения нового сотрудника")
    lbl_birthday.pack()
    ent_birthday = Entry(window_employee_insert, width=50)
    ent_birthday.pack()
    lbl_salary = Label(window_employee_insert, text="Введите ЗП нового сотрудника")
    lbl_salary.pack()
    ent_salary = Entry(window_employee_insert, width=50)
    ent_salary.pack()
    btn_employees_insert_action = Button(window_employee_insert, text="Добавить сотрудника", command=employee_insert)
    btn_employees_insert_action.pack()


# Открытие окна редактирования сотрудников
def open_employee_edit_window():
    def employee_combobox_request():

        cmb_employees_value.clear()
        # Устанавливаем соединение с базой данных
        connection = sqlite3.connect('employees_database.db')
        cursor = connection.cursor()

        # Выбираем и сортируем пользователей по возрасту по убыванию
        cursor.execute('SELECT employee_id, employee_FIO FROM employees')
        results = cursor.fetchall()
        if len(results) > 0:
            for i in range(len(results)):
                cmb_employees_value.append(results[i][1])

        else:
            cmb_employees_value.append = "список сотрудников пуст!"
        return results, cmb_employees_value

    def employee_edit_confrim():
        employee_fio = cmb_employees.get()
        employee_type = cmb_edit_type.get()
        employee_data = ent_edit_data.get()
        if employee_type == "ФИО":
            # Устанавливаем соединение с базой данных
            connection = sqlite3.connect('employees_database.db')
            cursor = connection.cursor()

            # Добавляем нового пользователя
            cursor.execute('UPDATE Employees SET employee_FIO = ? WHERE employee_FIO = ?',
                           (employee_data, employee_fio))

            # Сохраняем изменения и закрываем соединение
            connection.commit()
            connection.close()
            showinfo(title="ФИО сотрудника изменено!",
                     message=f'ФИО сотрудника "{employee_fio}" изменена на "{employee_data}"')
        elif employee_type == "День Рождения":
            # Устанавливаем соединение с базой данных
            connection = sqlite3.connect('employees_database.db')
            cursor = connection.cursor()

            # Добавляем нового пользователя
            cursor.execute('UPDATE Employees SET employee_birthday = ? WHERE employee_FIO = ?',
                           (employee_data, employee_fio))

            # Сохраняем изменения и закрываем соединение
            connection.commit()
            connection.close()
            showinfo(title="День рождения сотрудника изменен!",
                     message=f'День Рождения сотрудника "{employee_fio}" изменен на "{employee_data}"')
        elif employee_type == "ЗП":
            # Устанавливаем соединение с базой данных
            connection = sqlite3.connect('employees_database.db')
            cursor = connection.cursor()

            # Добавляем нового пользователя
            cursor.execute('UPDATE Employees SET employee_salary = ? WHERE employee_FIO = ?',
                           (employee_data, employee_fio))

            # Сохраняем изменения и закрываем соединение
            connection.commit()
            connection.close()
            showinfo(title="ЗП сотрудника изменена!",
                     message=f'ЗП сотрудника "{employee_fio}" изменена на "{employee_data}"')
        window_employee_edit.destroy()

    window_employee_edit = Tk()
    window_employee_edit.title("Редактирование сотрудников")
    window_employee_edit.geometry("700x600")
    # Выбор сотрудника для редактирования
    lbl_window_employee_edit = ttk.Label(window_employee_edit, text="Выберете ФИО сотрудника из списка",
                                         justify=LEFT)  # создаем текстовую метку
    lbl_window_employee_edit.pack()
    employee_combobox_request()
    cmb_employees = ttk.Combobox(window_employee_edit, values=cmb_employees_value, width=50)
    cmb_employees.pack()
    # Подпись и выбор редактируемого поля
    lbl_edit_type = ttk.Label(window_employee_edit, text="Выберете параметр для редактирования")
    lbl_edit_type.pack()
    cmb_edit_type = ttk.Combobox(window_employee_edit, values=["ФИО", "День Рождения", "ЗП"], width=50)
    cmb_edit_type.pack()
    # Подпись и ввод редактируемого поля
    lbl_edit_data = ttk.Label(window_employee_edit, text="Введите новое значние для выбранного паарметра")
    lbl_edit_data.pack()
    ent_edit_data = ttk.Entry(window_employee_edit, width=53)
    ent_edit_data.pack()
    # Кнопка подтверждения редактирования
    btn_employee_edit = ttk.Button(window_employee_edit, text="Подтвердить", command=employee_edit_confrim)
    btn_employee_edit.pack()


def open_employee_delete_window():
    def employee_combobox_request():

        cmb_employees_value.clear()
        # Устанавливаем соединение с базой данных
        connection = sqlite3.connect('employees_database.db')
        cursor = connection.cursor()

        # Выбираем и сортируем пользователей по возрасту по убыванию
        cursor.execute('SELECT employee_id, employee_FIO FROM employees')
        results = cursor.fetchall()
        if len(results) > 0:
            for i in range(len(results)):
                cmb_employees_value.append(results[i][1])

        else:
            cmb_employees_value.append = "список сотрудников пуст!"
        return results, cmb_employees_value

    def employee_delete_confrim():
        employee_fio = cmb_employees.get()
        # Устанавливаем соединение с базой данных
        connection = sqlite3.connect('employees_database.db')
        cursor = connection.cursor()

        # Добавляем нового пользователя
        cursor.execute('DELETE FROM Employees WHERE employee_FIO = ?', (employee_fio,))

        # Сохраняем изменения и закрываем соединение
        connection.commit()
        connection.close()
        showinfo(title="Сотрудник удален!",
                 message=f'Сотрудник "{employee_fio}" удален!')
        window_employee_delete.destroy()

    window_employee_delete = Tk()
    window_employee_delete.title("Удаление сотрудников")
    window_employee_delete.geometry("700x600")
    lbl_window_employee_delete = ttk.Label(window_employee_delete, text="Выберете сотрудника для удаления",
                                           justify=LEFT)  # создаем текстовую метку
    lbl_window_employee_delete.pack()
    # Выбор сотрудника для удаления
    employee_combobox_request()
    cmb_employees = ttk.Combobox(window_employee_delete, values=cmb_employees_value, width=50)
    cmb_employees.pack()
    # Кнопка подтверждения редактирования
    btn_employee_delete = ttk.Button(window_employee_delete, text="Удалить", command=employee_delete_confrim)
    btn_employee_delete.pack()


root = Tk()  # создаем корневой объект - окно
root.title("Система учета сотрудников фирмы")  # устанавливаем заголовок окна
root.geometry("600x500")  # устанавливаем размеры окна

label = Label(text="Выберете пункт меню для взаимодействия с базой данных")  # создаем текстовую метку
label.pack()

# стандартная кнопка
btn_employees_list = ttk.Button(text="Посмотреть список всех сотрудников", command=open_employee_list_window, width=50)
btn_employees_list.pack()
btn_employees_insert = ttk.Button(text="Добавить сотрудника", command=open_employee_insert_window, width=50)
btn_employees_insert.pack()
btn_employees_edit = ttk.Button(text="Отредактировать информацию о сотруднике", command=open_employee_edit_window, width=50)
btn_employees_edit.pack()
btn_employees_delete = ttk.Button(text="Удалить информацию о сотруднике", command=open_employee_delete_window, width=50)
btn_employees_delete.pack()

root.mainloop()

# label.pack()  # размещаем метку в окне

root.mainloop()
