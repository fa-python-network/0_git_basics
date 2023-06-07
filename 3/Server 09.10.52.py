import socket
import sys
HOST = 'localhost'
PORT = 5555

def handleClient(clientSocket):
    global HOST
    global PORT
    HOST = clientSocket.getsockname()[0]
    PORT = clientSocket.getpeername()[1]

    try:
        while True:
            clientData = clientSocket.recv(1024)
            if not clientData:
                break
            print("Received from {}: {}".format(HOST, clientData.decode('utf-8')))
            clientSocket.send(clientData)
    except:
        clientSocket.close()
        print("Error in handling client")

if __name__ == '__main__':
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind((HOST, PORT))

    print("Server is listening on port {}".format(PORT))
    serverSocket.listen(5)

    while True:
        try:
            connectedClient, clientAddress = serverSocket.accept()
            handleClient(connectedClient)
        except:
            serverSocket.close()
            sys.exit()