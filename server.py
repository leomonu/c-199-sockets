from email import message
import socket
from threading import Thread

# socket types TCP(tries to resend the packet that are lostHTTP<HHTTPS,SMTP,FTP)
# ,UDP(does not send lost packet,DNS,DHCP,Faster one)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


ip_address = '127.0.0.1'

port = 8000

# available port  = 65000 1024 not available
# socket  = ip + port

server.bind((ip_address, port))
server.listen()
# multiple clients can send multiple request to server
# clients = []
print("Server is running .... ")
list_of_clients = []


def clientThread(conn, addr):
    conn.send("Welcome to this chat room").encode("utf-8")

    while True:
        try:
            message-conn.recv(2048).decode("utf-8")
            if message:
                print("<"+addr[0]+">"+message)
                message_to_send = "<"+addr[0]+">"+message
                broadcast(message_to_send, conn)

            else:
                remove(conn)

        except:
            continue


def broadcast(message, connection):
    for clients in list_of_clients:
        if clients != connection:
            try:
                clients.send(message.encode("utf-8"))
            except:
                remove(connection)


def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)


 
while True:

        conn, addr = server.accept()

        list_of_clients.append(conn)

        print(addr[0]+"connected")

        new_thread = Thread(target=clientThread, args=(conn, addr))
        new_thread