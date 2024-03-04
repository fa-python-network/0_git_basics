# file_manager.py

import os
import shutil
import sys

def set_working_directory():
    with open("config.txt", "r", encoding='utf-8') as config_file:  # Открываем файл конфигурации для чтения
        script_directory = config_file.read().strip()  # Читаем рабочую директорию и удаляем пробелы
    working_directory = os.path.abspath(script_directory)
    os.chdir(working_directory)  # Смена рабочей директории на указанную в конфигурации
    return working_directory  # Возвращаем рабочую директорию

# def set_working_directory():
#     script_directory = os.path.dirname(os.path.realpath(__file__))
#     os.chdir(script_directory)
#     return script_directory


def create_folder(name):
    os.mkdir(name)  # Создание папки с указанным именем

def delete_folder(name):
    os.rmdir(name)  # Удаление папки с указанным именем

def move_into_folder(name):
    os.chdir(name)  # Переход в папку с указанным именем

def move_out_of_folder():
    current_directory = os.getcwd()  # Получаем текущую рабочую директорию
    parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))  # Получаем абсолютный путь родительской директории

    if parent_directory != initial_directory:  # Сравниваем родительскую директорию с рабочей директорией
        os.chdir(parent_directory)  # Если они не равны, переходим в родительскую директорию
    else:
        print("Ошибка: Вы находитесь в корневой рабочей папке, выход за ее пределы запрещен.")  # Если они равны, выводим сообщение об ошибке

def create_file(name):
    open(name, 'a').close()  # Создание пустого файла с указанным именем

def write_to_file(name, text):
    with open(name, "w", encoding='utf-8') as file:  # Открываем файл для записи
        file.write(text)  # Запись текста в файл

def read_file(name):
    with open(name, "r", encoding='utf-8') as file:  # Открываем файл для чтения
        print(file.read())  # Вывод содержимого файла на экран

def delete_file(name):
    os.remove(name)  # Удаление файла с указанным именем

def copy_file(source, destination):
    shutil.copy(source, destination)  # Копирование файла из источника в назначение

def move_file(source, destination):
    shutil.move(source, destination)  # Перемещение файла из источника в назначение

def rename_file(old_name, new_name):
    os.rename(old_name, new_name)  # Переименование файла

def process_input(user_input):
    tokens = user_input.split()  # Разделение ввода пользователя на слова (команда и параметры)
    command = tokens[0]  # Первое слово - команда



    if command == "создать_папку":
        if len(tokens) < 2:
            print("Ошибка: Пожалуйста, укажите имя папки для создания.")
        else:
            create_folder(tokens[1])
    elif command == "удалить_папку":
        if len(tokens) < 2:
            print("Ошибка: Пожалуйста, укажите имя папки для удаления.")
        else:
            delete_folder(tokens[1])
    elif command == "войти_в_папку":
        if len(tokens) < 2:
            print("Ошибка: Пожалуйста, укажите имя папки для входа.")
        else:
            move_into_folder(tokens[1])
    elif command == "выйти_из_папки":
        move_out_of_folder()
    elif command == "создать_файл":
        if len(tokens) < 2:
            print("Ошибка: Пожалуйста, укажите имя файла для создания.")
        else:
            create_file(tokens[1])
    elif command == "записать_в_файл":
        if len(tokens) < 3:
            print("Ошибка: Пожалуйста, укажите имя файла и текст для записи.")
        else:
            write_to_file(tokens[1], " ".join(tokens[2:]))
    elif command == "прочитать_файл":
        if len(tokens) < 2:
            print("Ошибка: Пожалуйста, укажите имя файла для чтения.")
        else:
            read_file(tokens[1])
    elif command == "удалить_файл":
        if len(tokens) < 2:
            print("Ошибка: Пожалуйста, укажите имя файла для удаления.")
        else:
            delete_file(tokens[1])
    elif command == "скопировать_файл":
        if len(tokens) < 3:
            print("Ошибка: Пожалуйста, укажите имя исходного файла и путь назначения.")
        else:
            copy_file(tokens[1], tokens[2])
    elif command == "переместить_файл":
        if len(tokens) < 3:
            print("Ошибка: Пожалуйста, укажите имя исходного файла и путь назначения.")
        else:
            move_file(tokens[1], tokens[2])
    elif command == "переименовать_файл":
        if len(tokens) < 3:
            print("Ошибка: Пожалуйста, укажите текущее имя файла и новое имя.")
        else:
            rename_file(tokens[1], tokens[2])
    elif command == "завершить":
        print("Завершение программы...")
        sys.exit(0)

    else:
        print("Ошибка: Неверная команда. Пожалуйста, используйте одну из следующих команд:")
        print_help()

def print_help():
    commands = {
        "создать_папку": "Создает новую папку с указанным именем.",
        "удалить_папку": "Удаляет папку с указанным именем.",
        "войти_в_папку": "Переходит в папку с указанным именем.",
        "выйти_из_папки": "Выходит из текущей папки в родительскую.",
        "создать_файл": "Создает новый файл с указанным именем.",
        "записать_в_файл": "Записывает текст в файл с указанным именем.",
        "прочитать_файл": "Выводит содержимое файла с указанным именем.",
        "удалить_файл": "Удаляет файл с указанным именем.",
        "скопировать_файл": "Копирует файл из указанного источника в назначение.",
        "переместить_файл": "Перемещает файл из указанного источника в назначение.",
        "переименовать_файл": "Переименовывает файл с указанным именем.",
        "завершить": "Завершение программы."
    }

    print("\nСписок доступных команд:")
    for command, description in commands.items():
        print(f"{command}: {description}")

def main():
    global initial_directory  # Объявляем глобальную переменную initial_directory
    initial_directory = set_working_directory()  # Сохраняем первоначальную директорию
    print_help()

    while True:
        user_input = input("\nВведите команду: ")
        process_input(user_input)

if __name__ == "__main__":
    main()