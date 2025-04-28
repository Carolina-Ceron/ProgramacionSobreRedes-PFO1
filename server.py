import socket
import datetime
import db_controller

# Configuración del socket TCP/IP

#Inicializar el socket
port = 5000

def initializeSocket():
    try:
        mySocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        mySocket.bind(("localhost",port))
        mySocket.listen(1)
        print("The socket has been initialized")
        return mySocket
    except:
        print("Error initializing socket")

def messageReceiver(mySocket:socket.socket):
    while True:
        connection, ip = mySocket.accept()
        ip = f"{ip[0]}:{ip[1]}"
        while True:
            message = connection.recv(1024).decode()
            if message == "éxito":
                break
            messageDate = datetime.datetime.today()
            print("new message received from", ip, "at", messageDate)
            db_controller.saveMessage(message,messageDate,ip)
            connection.send(f"Mensaje recibido: {messageDate} ".encode())
        break

messageReceiver(initializeSocket())
