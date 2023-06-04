# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import messagebox, filedialog
import os
import shutil
from settings import *

root = Tk()
root.geometry("900x550")
root.title("приложение для управления файлами")
root.config(background="white")

def create_file():
    global name_entry, dir, f
    dir = WORK_FOLDER_PATH
    f = Frame(root, background="white")
    f.place(width=300,height=300,x=350,y=50)
    Label(f, text="Введите имя файла", bg='white', font="bold").grid(row=0, column=0, padx=10, pady=10)
    name_entry = Entry(f, bd=4, width=25, relief=SUNKEN)
    name_entry.grid(row=1, column=0, padx=10, pady=10)
    Button(f, text='создать файл', font="bold", bg='dark green', fg='white', command=makeFile).grid(row=2, column=0,
                                                                                                    padx=10, pady=10)
    Button(f, text='отменить', font="bold", bg='red2', fg='white', command=f.destroy).grid(row=2, column=1)
    f.mainloop()


def makeFile():
    name = name_entry.get() + ".txt"
    os.chdir(dir)
    open(name, 'a').close()
    f.destroy()
    messagebox.showinfo('создать файл', "файл успешно создан")


def writing_text_files():
    global path1, text1, f2
    file = filedialog.askopenfilename(initialdir=WORK_FOLDER_PATH)
    if file:
        if WORK_FOLDER_PATH in file:
            path1 = os.path.abspath(file)
            f2 = Frame(root, background="grey")
            f2.place(width=300,height=300,x=350,y=50)
            Label(f2, text="Введите текст").grid(row=0, column=1, padx=10, pady=10)
            text1 = Entry(f2)
            text1.grid(row=1, column=1, padx=10, pady=10)
            Button(f2, text='сохранить', command=change_text).grid(row=2, column=1, padx=10, pady=10)
            Button(f2, text='Отменить', command=f2.destroy).grid(row=2, column=2)
            f2.mainloop()
        else:
            messagebox.showinfo('Ошибка', "Выход за пределы рабочей папки")


def change_text():
    global path1, text1, f2
    with open(path1, 'w') as f:
        f.write(text1.get())
    messagebox.showinfo('ввод текста', "текст введен")
    f2.destroy()


def open_file():
    file = filedialog.askopenfilename(initialdir=WORK_FOLDER_PATH)
    if file:
        if WORK_FOLDER_PATH in file:
            os.startfile(file)
            messagebox.showinfo('открыть файл', file + " успешно открыт")
        else:
            messagebox.showinfo('Ошибка', "Выход за пределы рабочей папки")


def delete_file():
    file = filedialog.askopenfilename(initialdir=WORK_FOLDER_PATH)
    if file:
        if WORK_FOLDER_PATH in file:
            os.remove(file)
            messagebox.showinfo('удалить файл', file + " удалено успешно")
        else:
            messagebox.showinfo('Ошибка', "Выход за пределы рабочей папки")
    else:
        messagebox.showinfo('Ошибка', "Выход за пределы рабочей папки")


def rename_file():
    global filename, file, f1, path
    file = filedialog.askopenfilename(initialdir=WORK_FOLDER_PATH)
    if file:
        if WORK_FOLDER_PATH in file:
            path = os.path.abspath(file)
            f1 = Frame(root, background="grey")
            f1.place(width=300, height=300, x=300, y=40)
            Label(f1, text="Введите имя файла").grid(row=0, column=0, padx=10, pady=10)
            filename = Entry(f1)
            filename.grid(row=1, column=0, padx=10, pady=10)
            Button(f1, text='Переименовать файл', command=change_name).grid(row=2, column=0, padx=10, pady=10)
            Button(f1, text='Отменить', command=f1.destroy).grid(row=2, column=2, padx=10, pady=10)
            f1.mainloop()
        else:
            messagebox.showinfo('Ошибка', "Выход за пределы рабочей папки")


def change_name():
    newName = filename.get()+'.txt'
    dir = os.path.dirname(path)
    renamed = os.path.join(dir, newName)
    os.rename(path, renamed)
    f1.destroy()
    messagebox.showinfo('переименовать файл', file + " успешно переименован")


def deletefolder():
    delFolder = filedialog.askdirectory(initialdir=WORK_FOLDER_PATH)
    if delFolder != WORK_FOLDER_PATH:
        if WORK_FOLDER_PATH in delFolder:
            os.rmdir(delFolder)
            messagebox.showinfo('подтверждение', "Папка удалена !")
        else:
            messagebox.showinfo('Ошибка', "Выход за пределы рабочей папки")
    else:
        messagebox.showinfo('Ошибка', "Выход за пределы рабочей папки")


def create_folder():
    global name_entry, dir, f
    dir = WORK_FOLDER_PATH
    f = Frame(root, background="white")
    f.place(width=300,height=300,x=350,y=50)
    Label(f, text="Введите имя папки", bg='white', font="bold").grid(row=0, column=0, padx=10, pady=10)
    name_entry = Entry(f, bd=4, width=25, relief=SUNKEN)
    name_entry.grid(row=1, column=0, padx=10, pady=10)
    Button(f, text='создать папку', font="bold", bg='dark green', fg='white', command=makeFolder).grid(row=2, column=0,
                                                                                                       padx=10, pady=10)
    Button(f, text='отменить', font="bold", bg='red2', fg='white', command=f.destroy).grid(row=2, column=1)
    f.mainloop()


def makeFolder():
    name = name_entry.get()
    os.chdir(dir)
    os.makedirs(name)
    f.destroy()
    messagebox.showinfo('создать папку', " папка успешна сосзданна")


def rename_folder():
    global dir, folder_name, f1, path
    folder_name = filedialog.askdirectory(initialdir=WORK_FOLDER_PATH)
    if folder_name != WORK_FOLDER_PATH:
        path = os.path.abspath(folder_name)
        f1 = Frame(root, background="grey")
        f1.place(width=300,height=150,x=350,y=50)
        Label(f1, text="Введите имя папки").grid(row=0, column=1, padx=10, pady=10)
        folder_name = Entry(f1)
        folder_name.grid(row=1, column=1, padx=10, pady=10)
        Button(f1, text='Переименовать папку', command=change_folder).grid(row=2, column=1, padx=10, pady=10)
        Button(f1, text='отменить', command=f1.destroy).grid(row=2, column=2)
        f1.mainloop()
    else:
        messagebox.showinfo('Ошибка', "Выход за пределы рабочей папки")



def change_folder():
    newName = folder_name.get()
    dir = os.path.dirname(path)
    renamed = os.path.join(dir, newName)
    os.rename(path, renamed)
    f1.destroy()
    messagebox.showinfo('переименовать папку', path + " успешно переименован")


def view_folder():
    view_folder = filedialog.askdirectory(initialdir=WORK_FOLDER_PATH)
    f1 = Frame(root)
    f1.place(width=200,height=200,x=350,y=50)
    listbox = Listbox(f1, width=30)
    listbox.grid(row=0, column=0)
    view_folder = os.listdir(view_folder)
    for name in view_folder:
        listbox.insert('end', name)
    exit_button = Button(f1, text='Ok', bg='dark green', fg='white', font="bold", command=f1.destroy)
    exit_button.grid(row=1, column=0)


def copy_move_file():
    global sourceText, destinationText, destination_location, f1
    f1 = Frame(root, width=350, height=300, background="lavender")
    f1.grid(row=5, column=0, columnspan=4)

    source_location = StringVar()
    destination_location = StringVar()

    link_Label = Label(f1, text="Выберите Файл для Копирования ", font="bold", bg='lavender')
    link_Label.grid(row=0, column=0, pady=5, padx=5)

    sourceText = Entry(f1, width=50, textvariable=source_location, font="12")
    sourceText.grid(row=0, column=1, pady=5, padx=5)
    source_browseButton = Button(f1, text="Просматривать", bg='cyan2', command=source_browse, width=15, font="bold")
    source_browseButton.grid(row=0, column=2, pady=5, padx=5)

    destinationLabel = Label(f1, text="Выберите пункт назначения", bg="lavender", font="bold")
    destinationLabel.grid(row=1, column=0, pady=5, padx=5)

    destinationText = Entry(f1, width=50, textvariable=destination_location, font=12)
    destinationText.grid(row=1, column=1, pady=5, padx=5)
    dest_browseButton = Button(f1, text="Просматривать", bg='cyan2', command=destination_browse, width=15, font="12")
    dest_browseButton.grid(row=1, column=2, pady=5, padx=5)

    copyButton = Button(f1, text="Скопировать файл", bg='dark green', fg='white', command=copy_file, width=15,
                        font=('bold', 12))
    copyButton.grid(row=2, column=0, pady=10, padx=10)

    moveButton = Button(f1, text="Переместить файл", bg='dark green', fg='white', command=move_file, width=15,
                        font=('bold', 12))
    moveButton.grid(row=2, column=1, pady=10, padx=10)

    cancelButton = Button(f1, text="отмена", bg='red2', fg='white', command=f1.destroy, width=15, font=('bold', 12))
    cancelButton.grid(row=2, column=2, pady=10, padx=10)


def source_browse():
    global files_list
    files_list = list(filedialog.askopenfilenames(initialdir=WORK_FOLDER_PATH))
    sourceText.insert('1', files_list)


def destination_browse():
    destinationdirectory = filedialog.askdirectory(initialdir=WORK_FOLDER_PATH)
    destinationText.insert('1', destinationdirectory)


def copy_file():
    dest_location = destination_location.get()
    if WORK_FOLDER_PATH in dest_location:
        for f in files_list:
            if dest_location:
                if WORK_FOLDER_PATH in f :
                    shutil.copy(f, dest_location)
                else:
                    messagebox.showinfo('Ошибка', "Выход за пределы рабочей папки")
        messagebox.showinfo('скопировать файл', "скопировано успешно")
        f1.destroy()
    else:
        messagebox.showinfo('Ошибка', "Выход за пределы рабочей папки")


def move_file():
    dest_location = destination_location.get()
    if WORK_FOLDER_PATH in dest_location:
        for f in files_list:
            if dest_location:
                if WORK_FOLDER_PATH in f:
                    shutil.move(f, dest_location)
                else:
                    messagebox.showinfo('Ошибка', "Выход за пределы рабочей папки")
        messagebox.showinfo('переместить файл', "успешно перемещенный файл")
        f1.destroy()
    else:
        messagebox.showinfo('Ошибка', "Выход за пределы рабочей папки")


open_btn = Button(root, text="Открыть файл", command=open_file, width=25, font=('bold', 14))
open_btn.place(x=20, y=60)

delete_btn = Button(root, text="Удалить файл", command=delete_file, width=25, font=('bold', 14))
delete_btn.place(x=20, y=180)

rename_btn = Button(root, text="Переименовать файл", command=rename_file, width=25, font=('bold', 14))
rename_btn.place(x=20, y=100)

copy_move_btn = Button(root, text="Копир/Перемещение файла", command=copy_move_file, width=25, font=('bold', 14))
copy_move_btn.place(x=20, y=140)

create_folder_btn = Button(root, text="Создать папку", command=create_folder, width=25, font=('bold', 14))
create_folder_btn.place(x=20, y=260)

deletefolder_btn = Button(root, text="Удалить папку", command=deletefolder, width=25, font=('bold', 14))
deletefolder_btn.place(x=20, y=380)

rename_folder_btn = Button(root, text="Переименовать папку", command=rename_folder, width=25, font=('bold', 14))
rename_folder_btn.place(x=20, y=340)

view_btn = Button(root, text="Просмотр содержимого папки", command=view_folder, width=25, font=('bold', 14))
view_btn.place(x=20, y=300)

exit_btn = Button(root, text="Выход", command=root.destroy, width=25, font=('bold', 14))
exit_btn.place(x=20, y=460)

create_file = Button(root, text="Создать файл", command=create_file, width=25, font=('bold', 14))
create_file.place(x=20, y=20)

writing_text_files = Button(root, text="Записать текст в файл", command=writing_text_files, width=25, font=('bold', 14))
writing_text_files.place(x=20, y=220)

root.mainloop()