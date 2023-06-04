import socket

sock = socket.socket()

ch = int(input("Выберите файл:\n1. 1.html\n2. 2.html\n3. index.html\n>>> "))

if ch == 1:
    filename = "1.html"
elif ch == 2:
    filename = "2.html"
else:
    filename = "index.html"

try:
    sock.bind(('', 80))
    print("Используется порт 80")
except OSError:
    sock.bind(('', 8080))
    print("Используется порт 8080")

sock.listen(5)

conn, addr = sock.accept()
print("Подключение", addr)

data = conn.recv(8192)
msg = data.decode()

print(msg)

with open(filename, 'r') as f:
    resp = f.read()

resp = """HTTP/1.1 200 OK
Server: SelfMadeServer v0.0.1
Content-type: text/html
Connection: close

Hello, webworld!""" + resp

conn.send(resp.encode())

conn.close()