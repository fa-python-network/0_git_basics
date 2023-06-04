import socket


currentDirectory = ''
while True:
    request = input(f'{currentDirectory} >>> ')
    sock = socket.socket()
    sock.connect(('localhost', 6666))
    sock.send(request.encode())
    response = sock.recv(1024).decode()
    print(response)
    sock.close()
    if request == 'выход': break
