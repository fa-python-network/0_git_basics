import socket

HOST = 'localhost'
PORT = 5555

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        message = input('Enter message: ')
        if message == 'exit' or not message:
            break
        s.send(message.encode())
        data = s.recv(1024)
        print(f'Received: {data.decode()}')
