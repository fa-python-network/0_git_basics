import socket, threading


class ClientThread(threading.Thread):
    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print('Новое подключение:', clientAddress)

    def run(self):
        print('Подключен:', clientAddress)
        self.csocket.send(bytes('привет. это сервер.', 'utf-8'))
        msg = ''
        while True:
            data = self.csocket.recv(2048)
            msg = data.decode()
            print('пользователь:', msg)
            if msg == 'выход':
                break

            self.csocket.send(bytes(msg,'UTF-8'))

        print('Пользователь с адресом', clientAddress, 'отключился.')

LOCALHOST = "127.0.0.1"
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))

print('сервер запущен')
print('Ожидается ввод пользователя.')

while True:
    server.listen(1)
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()
