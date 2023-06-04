import socket
import os


def process(req):
    words = req.split(' ')
    wordsLen = len(words)

    if words[0] == 'создать':
        if wordsLen == 2:
            return create_file(rootDirectory, words[1])
        else:
            return 'некорректное количество аргументов'
    elif words[0] == 'написать':
        if wordsLen > 2:
            return write_file(rootDirectory, words[1], words[2:])
        else:
            return 'некорректное количество аргументов'
    elif words[0] == 'открыть':
        if wordsLen == 2:
            return read_file(rootDirectory, words[1])
        else:
            return 'некорректное количество аргументов'
    elif words[0] == 'удалить':
        if wordsLen == 2:
            return delete_file(rootDirectory, words[1])
        else:
            return 'некорректное количество аргументов'
    elif words[0] == 'выход':
        return 'Завершение работы'

    return 'неизвестная команда'


def create_file(path, name):
    filename = os.path.join(path, name)

    if not os.path.exists(filename):
        open(filename, 'a').close()
        return 'Файл создан'
    else:
        return 'Файл существует'


def write_file(path, name, words):
    filename = os.path.join(path, name)
    file = open(filename, 'a')

    text = ''

    for word in words:
        text += str(word) + ' '

    file.write(text)
    file.close()

    return 'Текст добавлен'


def read_file(path, name):
    filename = os.path.join(path, name)

    if os.path.exists(filename):
        file = open(filename, 'r')
        text = file.read()

        file.close()

        return text
    else:
        return 'Файл не существует'


def delete_file(path, name):
    filename = os.path.join(path, name)

    if os.path.exists(filename):
        os.remove(filename)

        return 'Успешно удален'
    else:
        return 'Файл не существует'


rootDirectory = os.path.dirname(os.path.abspath(__file__))
dirName = 'root'
rootDirectory = os.path.join(rootDirectory, dirName)
if not os.path.exists(rootDirectory):
    os.mkdir(rootDirectory)

sock = socket.socket()
sock.bind(('', 6666))
sock.listen(1)

while True:
    conn, addr = sock.accept()
    request = conn.recv(1024).decode()
    print('Пользователь:', request)

    response = process(request)
    conn.send(response.encode())
    if request == 'Выход':
        break

conn.close()
