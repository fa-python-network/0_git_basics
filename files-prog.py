import os

working_directory = "./"


def create_folder(folder_name):
    folder_path = os.path.join(working_directory, folder_name)
    if not os.path.exists(folder_name):
        os.mkdir(folder_path)
    print(f"Папка '{folder_name}' создана")


def delete_folder(folder_name):
    folder_path = os.path.join(working_directory, folder_name)
    if os.path.exists(folder_name):
        os.rmdir(folder_path)
    print(f"Папка '{folder_name}' удалена")


def move_to_folder(folder_name):
    global working_directory
    new_path = os.path.join(working_directory, folder_name)
    if os.path.exists(new_path) and os.path.isdir(new_path):
        working_directory = new_path
        print(f"Перешли в папку '{folder_name}'")
    else:
        print("Папка не существует")


def create_file(file_name):
    file_path = os.path.join(working_directory, file_name)
    if not os.path.exists(file_name):
        with open(file_path, 'w') as file:
            pass
    print(f"Файл '{file_name}' создан")


def write_to_file(file_name, text):
    file_path = os.path.join(working_directory, file_name)
    with open(file_path, 'w') as file:
        file.write(text)
    print(f"Текст записан в файл '{file_name}'")


def view_file(file_name):
    file_path = os.path.join(working_directory, file_name)
    with open(file_path, 'r') as file:
        content = file.read()
        print(f"Содержимое файла '{file_name}':\n{content}")


def delete_file(file_name):
    file_path = os.path.join(working_directory, file_name)
    os.remove(file_path)
    print(f"Файл '{file_name}' удален")


def copy_file(source_file, destination_folder):
    source_path = os.path.join(working_directory, source_file)
    destination_path = os.path.join(
        working_directory, destination_folder, source_file)
    if os.path.exists(source_path) and os.path.isfile(source_path):
        os.system(f'copy "{source_path}" "{destination_path}"')
        print(f"Файл '{source_file}' скопирован в папку '{destination_folder}'")
    else:
        print("Файл не существует")


def move_file(source_file, destination_folder):
    source_path = os.path.join(working_directory, source_file)
    destination_path = os.path.join(
        working_directory, destination_folder, source_file)
    if os.path.exists(source_path) and os.path.isfile(source_path):
        os.rename(source_path, destination_path)
        print(f"Файл '{source_file}' перемещен в папку '{destination_folder}'")
    else:
        print("Файл не существует")


def rename_file(old_name, new_name):
    old_path = os.path.join(working_directory, old_name)
    new_path = os.path.join(working_directory, new_name)
    if os.path.exists(old_path) and os.path.isfile(old_path):
        os.rename(old_path, new_path)
        print(f"Файл '{old_name}' переименован в '{new_name}'")
    else:
        print("Файл не существует")


# Examples
create_folder("Folder1")
create_file("file1.txt")
write_to_file("file1.txt", "Hello World!")
view_file("file1.txt")
copy_file("file1.txt", "Folder1")
move_to_folder("Folder1")
delete_file("file1.txt")
delete_folder("Folder1")
