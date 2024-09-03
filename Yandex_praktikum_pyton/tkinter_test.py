from tkinter import *

root = Tk()  # создаем корневой объект - окно
root.title("Система учета сотрудников фирмы")  # устанавливаем заголовок окна
root.geometry("600x500")  # устанавливаем размеры окна
root.iconbitmap(default="favicon.ico")

label = Label(text="Выберете пункт меню для взаимодействия с базой данных")  # создаем текстовую метку
label.pack()  # размещаем метку в окне

root.mainloop()