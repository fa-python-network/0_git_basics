import socket
import pickle
import cryptocode


HOST = '127.0.0.1'
PORT = 5555

sock = socket.socket()
sock.connect((HOST, PORT))

p, g, a = 7, 5, 3
A = g ** a % p
sock.send(pickle.dumps((p, g, A)))

B = pickle.loads(sock.recv(1024))
K = B ** a % p
key = str(K)

msgEn = pickle.loads(sock.recv(1024))
print('Зашифованное сообщение:', msgEn)

msg = cryptocode.decrypt(msgEn, key)
print('расшифрованное сообщение:', msg)

sock.close()