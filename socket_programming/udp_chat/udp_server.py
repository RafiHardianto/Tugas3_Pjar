import socket
import threading
from datetime import datetime

HOST = '0.0.0.0'
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

clients = set()

print(f"[UDP SERVER RUNNING] {HOST}:{PORT}")

def save_log(message):
    with open("udp_log.txt", "a") as file:
        file.write(message + "\n")

while True:
    data, addr = server.recvfrom(1024)

    if addr not in clients:
        clients.add(addr)

    message = data.decode()

    timestamp = datetime.now().strftime("%H:%M:%S")
    full_message = f"[{timestamp}] {message}"

    print(full_message)
    save_log(full_message)

    for client in clients:
        if client != addr:
            server.sendto(full_message.encode(), client)
