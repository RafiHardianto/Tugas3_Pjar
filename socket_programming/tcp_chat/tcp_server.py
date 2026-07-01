import socket
import threading
import json
import os

HOST = '0.0.0.0'
PORT = 6000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
usernames = []

if not os.path.exists("uploads"):
    os.mkdir("uploads")

with open("users.json", "r") as file:
    USERS = json.load(file)

print("[TCP SERVER RUNNING]")

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)

            if message.startswith(b"/sendfile"):
                filename = message.decode().split(" ")[1]

                with open(f"uploads/{filename}", "wb") as file:
                    data = client.recv(4096)
                    file.write(data)

                client.send(f"File {filename} diterima server".encode())

            else:
                broadcast(message)

        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()

            username = usernames[index]
            usernames.remove(username)

            broadcast(f"{username} keluar chat".encode())
            break

def receive():
    while True:
        client, address = server.accept()

        client.send("USERNAME".encode())
        username = client.recv(1024).decode()

        client.send("PASSWORD".encode())
        password = client.recv(1024).decode()

        if username in USERS and USERS[username] == password:

            client.send("LOGIN_SUCCESS".encode())

            usernames.append(username)
            clients.append(client)

            print(f"{username} connected")

            broadcast(f"{username} joined chat!".encode())

            thread = threading.Thread(target=handle, args=(client,))
            thread.start()

        else:
            client.send("LOGIN_FAILED".encode())
            client.close()

receive()