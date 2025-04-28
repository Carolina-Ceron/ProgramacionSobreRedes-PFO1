import socket
import datetime
import db_controller

# Configuración del socket TCP/IP

#Inicializar el socket
def initializeSocket():
    try:
        mySocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        mySocket.bind(("localhost",5000))
        mySocket.listen(1)
        print("The socket has been initialized")
    except:
        print("Error initializing socket")

def messageReceiver(mySocket:socket.socket):
    while True:
        connection, ip = mySocket.accept()