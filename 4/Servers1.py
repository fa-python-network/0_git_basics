from datetime import datetime
import socket

log = open('log.txt', 'a')

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
log.write(f'{datetime.now()} Сервер запущен\n')

while True:
    conn, addr = sock.accept()
    log.write(f'{datetime.now()} Подключение с {addr[0]}\n')

    username, password = (conn.recv(1024).decode()).split('/')
    log.write(f'{datetime.now()} Пользователь \"{username}\" авторизовался\n')

    resAutorization = ''
    isAuth = False
    userFound = False
    with open('users.txt') as users:
        for line in users:
            line = line.strip('\n')
            words = line.split('/')
            if words[0] == username:
                userFound = True
                resAutorization += f'Привет, {username}!\n'
                if words[1] == password:
                    isAuth = True
                    break
                else:
                    resAutorization += 'неверный пароль\n'
                    break

        if not userFound:
            resAutorization += 'Неизвестный пользователь\n'
            log.write(f'{datetime.now()} Неизвестный пользователь\n')

        if isAuth:
            log.write(f'{datetime.now()} Пользователь \"{username}\" успешно вошел\n')
            conn.send(resAutorization.encode())
            log.write(f'{datetime.now()} Сообщение от сервера:\n')
            log.write(resAutorization)
            while True:
                data = conn.recv(1024).decode()
                print(f'{datetime.now()} {username}: {data}')
                log.write(f'{datetime.now()} Пользователь \"{username}\" сообщение:\n')
                log.write(data + '\n')
                if data == 'выход':
                    log.write(f'{datetime.now()} Пользователь \"{username}\" Отключился\n')
                    break
                elif data == 'время':
                    message = str(datetime.now())
                    conn.send(message.encode())
                    log.write(f'{datetime.now()} Server message:\n')
                    log.write(message + '\n')
                elif data == 'ктоя':
                    message = username
                    conn.send(message.encode())
                    log.write(f'{datetime.now()} Сообщение от сервера:\n')
                    log.write(message + '\n')
        else:
            log.write(f'{datetime.now()} попытка аутентификации не удалась\n')
            conn.send(resAutorization.encode())
            log.write(f'{datetime.now()} сообщение от сервера:\n')
            log.write(resAutorization)

log.write(f'{datetime.now()} сервер закрыт\n')
log.close()
conn.close()
