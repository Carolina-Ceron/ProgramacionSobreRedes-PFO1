import socket


message = ""

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("localhost", 5000))

while message != "éxito":
    message = input("Ingrese su mensaje: ")
    client.send(message.encode()) 
    print(client.recv(1024).decode())
client.close()