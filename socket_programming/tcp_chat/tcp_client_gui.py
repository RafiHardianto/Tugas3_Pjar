import socket
import threading
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from datetime import datetime

HOST = '127.0.0.1'
PORT = 6000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# ================= WINDOW =================
window = tk.Tk()
window.title("TCP Chat Application")
window.geometry("650x750")
window.configure(bg="#1e1e1e")

# ================= HEADER =================
header = tk.Frame(window, bg="#292929", height=70)
header.pack(fill=tk.X)

title = tk.Label(
    header,
    text="TCP REALTIME CHAT",
    bg="#292929",
    fg="white",
    font=("Segoe UI", 18, "bold")
)

title.pack(pady=20)

# ================= CHAT AREA =================
chat_frame = tk.Frame(window, bg="#1e1e1e")
chat_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

chat_box = tk.Text(
    chat_frame,
    bg="#252526",
    fg="white",
    font=("Consolas", 11),
    relief=tk.FLAT,
    wrap=tk.WORD,
    state='disabled'
)

chat_box.pack(fill=tk.BOTH, expand=True)

# ================= INPUT =================
bottom_frame = tk.Frame(window, bg="#1e1e1e")
bottom_frame.pack(fill=tk.X, padx=10, pady=10)

entry = tk.Entry(
    bottom_frame,
    bg="#2d2d30",
    fg="white",
    insertbackground="white",
    font=("Segoe UI", 12),
    relief=tk.FLAT
)

entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=10)

# ================= LOGIN =================
def login():
    username = simpledialog.askstring(
        "Login",
        "Username:"
    )

    password = simpledialog.askstring(
        "Login",
        "Password:"
    )

    if client.recv(1024).decode() == "USERNAME":
        client.send(username.encode())

    if client.recv(1024).decode() == "PASSWORD":
        client.send(password.encode())

    result = client.recv(1024).decode()

    if result == "LOGIN_SUCCESS":
        messagebox.showinfo("Success", "Login berhasil")

    else:
        messagebox.showerror("Error", "Login gagal")
        window.destroy()

# ================= RECEIVE =================
def receive():
    while True:
        try:
            message = client.recv(1024).decode()

            timestamp = datetime.now().strftime("%H:%M")

            chat_box.config(state='normal')

            chat_box.insert(
                tk.END,
                f"[{timestamp}] {message}\n\n"
            )

            chat_box.config(state='disabled')
            chat_box.see(tk.END)

        except:
            break

# ================= SEND MESSAGE =================
def send_message():
    message = entry.get()

    if message.strip() == "":
        messagebox.showwarning(
            "Warning",
            "Pesan kosong!"
        )
        return

    client.send(message.encode())

    entry.delete(0, tk.END)

# ================= SEND FILE =================
def send_file():
    filepath = filedialog.askopenfilename()

    if filepath:
        filename = filepath.split("/")[-1]

        client.send(f"/sendfile {filename}".encode())

        with open(filepath, "rb") as file:
            data = file.read()

        client.send(data)

        messagebox.showinfo(
            "Success",
            f"File {filename} berhasil dikirim"
        )

# ================= BUTTONS =================
button_frame = tk.Frame(window, bg="#1e1e1e")
button_frame.pack(fill=tk.X, padx=10, pady=5)

send_btn = tk.Button(
    button_frame,
    text="SEND",
    bg="#0e639c",
    fg="white",
    font=("Segoe UI", 11, "bold"),
    relief=tk.FLAT,
    padx=20,
    command=send_message,
    cursor="hand2"
)

send_btn.pack(side=tk.LEFT, padx=5)

file_btn = tk.Button(
    button_frame,
    text="SEND FILE",
    bg="#107c10",
    fg="white",
    font=("Segoe UI", 11, "bold"),
    relief=tk.FLAT,
    padx=20,
    command=send_file,
    cursor="hand2"
)

file_btn.pack(side=tk.LEFT)

# ================= START =================
login()

thread = threading.Thread(target=receive)
thread.daemon = True
thread.start()

window.mainloop()