import socket

sock = socket.socket()

username = input('Введите логин: ')
password = input('Введите пароль: ')

port = input('Введите порт(Enter для значения по умолчанию): ')

if not port:
    port = 9090
else:
    port = int(port)

addr = input('Введите адрес(Enter для значения по умолчанию): ')

if not addr:
    addr = 'localhost'

sock.connect((addr, port))
sock.send((username + '/' + password).encode())

resAutorization = sock.recv(1024).decode()
print(resAutorization, end='')

while True:
    data = input(f'{username} >>> ')
    sock.send(data.encode())

    if data == 'выход':
        break
    elif data == 'ктоя' or data == 'время':
        answer = sock.recv(1024).decode()
        print(f'Server: {answer}')

sock.close()