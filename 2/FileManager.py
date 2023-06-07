import os
from settings import *


current_dir = WORK_FOLDER_PATH


def list_files():
    files = os.listdir(current_dir)
    print(f'Files in directory: {str(files)}')


def create_folder():
    folder_name = input('Enter folder name: ')

    try:
        os.mkdir(os.path.join(current_dir, folder_name))
        print('Folder created successfully')
    except:
        print('Failed to create folder')


def delete_folder():
    folder_name = input('Enter folder name: ')

    try:
        os.rmdir(os.path.join(current_dir, folder_name))
        print('Folder deleted successfully')
    except:
        print('Failed to delete folder')


def create_file():
    file_name = input('Enter file name: ')

    try:
        with open(os.path.join(current_dir, file_name), 'w'):
            pass
        print('File created successfully')
    except:
        print('Failed to create file')


def delete_file():
    file_name = input('Enter file name: ')

    try:
        os.remove(os.path.join(current_dir, file_name))
        print('File deleted successfully')
    except:
        print('Failed to delete file')


def rename_file():
    old_name = input('Enter old file name: ')
    new_name = input('Enter new file name: ')

    try:
        os.rename(os.path.join(current_dir, old_name), os.path.join(current_dir, new_name))
        print('File renamed successfully')
    except:
        print('Failed to rename file')


def write_to_file():
    file_name = input('Enter file name: ')
    text = input('Enter text: ')

    try:
        with open(os.path.join(current_dir, file_name), 'w') as f:
            f.write(text)
        print('Text written to file successfully')
    except:
        print('Failed to write text to file')


def view_file():
    file_name = input('Enter file name: ')

    try:
        with open(os.path.join(current_dir, file_name), 'r') as f:
            print(f.read())
    except:
        print('Failed to view file')


def copy_file():
    src_file_name = input('Enter source file name: ')
    dst_file_name = input('Enter destination file name: ')

    try:
        with open(os.path.join(current_dir, src_file_name), 'rb') as src_file:
            with open(os.path.join(current_dir, dst_file_name), 'wb') as dst_file:
                dst_file.write(src_file.read())
        print('File copied successfully')
    except:
        print('Failed to copy file')


def move_file():
    src_file_name = input('Enter source file name: ')
    dst_file_name = input('Enter destination file name: ')

    try:
        os.replace(os.path.join(current_dir, src_file_name), os.path.join(current_dir, dst_file_name))
        print('File moved successfully')
    except:
        print('Failed to move file')


def change_directory():
    global current_dir
    dir_name = input('Enter directory name or ".." to go up one level: ')
    if dir_name == '..':
        if current_dir == BASE_DIR:
            print('You are already in the base directory.')
        else:
            current_dir = os.path.dirname(current_dir)
    else:
        new_dir = os.path.join(current_dir, dir_name)
        if os.path.isdir(new_dir):
            current_dir = new_dir
        else:
            print(f'{dir_name} is not a directory in {current_dir}')


def exit_():
    exit(0)


commands = {
    '1': list_files,
    '2': create_folder,
    '3': delete_folder,
    '4': create_file,
    '5': rename_file,
    '6': write_to_file,
    '7': view_file,
    '8': delete_file,
    '9': copy_file,
    '10': move_file,
    '11': change_directory,
    '12': exit_
}

while True:
    command = input('Enter command:\n'
                    '1. List files\n'
                    '2. Create folder\n'
                    '3. Delete folder\n'
                    '4. Create file\n'
                    '5. Rename file\n'
                    '6. Write to file\n'
                    '7. View file\n'
                    '8. Delete file\n'
                    '9. Copy file\n'
                    '10. Move file\n'
                    '11. Change directory\n'
                    '12. Exit\n')
    if command in commands:
        commands[command]()
    else:
        print('Invalid command')
