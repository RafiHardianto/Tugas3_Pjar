import socket
import threading
import tkinter as tk
from tkinter import simpledialog, messagebox
from datetime import datetime

SERVER_IP = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# ================= WINDOW =================
window = tk.Tk()
window.title("UDP Chat App")
window.geometry("600x700")
window.configure(bg="#1e1e1e")

# ================= USERNAME =================
username = simpledialog.askstring("Username", "Masukkan Username:")

# ================= HEADER =================
header = tk.Frame(window, bg="#292929", height=70)
header.pack(fill=tk.X)

title = tk.Label(
    header,
    text="UDP CHAT ROOM",
    bg="#292929",
    fg="white",
    font=("Segoe UI", 18, "bold")
)
title.pack(pady=20)

# ================= CHAT AREA =================
chat_frame = tk.Frame(window, bg="#1e1e1e")
chat_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

chat_box = tk.Text(
    chat_frame,
    bg="#252526",
    fg="white",
    font=("Consolas", 11),
    relief=tk.FLAT,
    state='disabled',
    wrap=tk.WORD
)

chat_box.pack(fill=tk.BOTH, expand=True)

# ================= INPUT AREA =================
bottom_frame = tk.Frame(window, bg="#1e1e1e")
bottom_frame.pack(fill=tk.X, padx=10, pady=10)

message_entry = tk.Entry(
    bottom_frame,
    bg="#2d2d30",
    fg="white",
    insertbackground="white",
    font=("Segoe UI", 12),
    relief=tk.FLAT
)

message_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=10)

# ================= RECEIVE =================
def receive_messages():
    while True:
        try:
            message, _ = client.recvfrom(1024)

            chat_box.config(state='normal')

            timestamp = datetime.now().strftime("%H:%M")

            chat_box.insert(
                tk.END,
                f"[{timestamp}] {message.decode()}\n\n"
            )

            chat_box.config(state='disabled')
            chat_box.see(tk.END)

        except:
            break

# ================= SEND =================
def send_message():
    message = message_entry.get()

    if message.strip() == "":
        messagebox.showwarning(
            "Warning",
            "Pesan tidak boleh kosong!"
        )
        return

    full_message = f"{username}: {message}"

    client.sendto(full_message.encode(), (SERVER_IP, PORT))

    message_entry.delete(0, tk.END)

# ================= BUTTON =================
send_button = tk.Button(
    bottom_frame,
    text="SEND",
    bg="#0e639c",
    fg="white",
    font=("Segoe UI", 11, "bold"),
    relief=tk.FLAT,
    padx=20,
    command=send_message,
    cursor="hand2"
)

send_button.pack(side=tk.LEFT, padx=10)

# ================= THREAD =================
thread = threading.Thread(target=receive_messages)
thread.daemon = True
thread.start()

window.mainloop()