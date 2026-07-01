# TCP CHAT APPLICATION

## Deskripsi

Program ini merupakan aplikasi chat berbasis TCP (Transmission Control Protocol) menggunakan konsep client-server.

Program dibuat menggunakan Python dan GUI sederhana menggunakan Tkinter.

TCP digunakan karena memiliki koneksi yang lebih stabil dan aman dibanding UDP.

---

# Fitur Program

- Multiple client connection
- Login authentication
- Real-time chat
- File transfer
- GUI sederhana
- Error handling

---

# Struktur Folder

```plaintext
tcp_chat/
│
├── tcp_server.py
├── tcp_client_gui.py
├── users.json
├── uploads/
└── README.md
```

---

# Cara Menjalankan Program

## 1. Jalankan TCP Server

Buka terminal kemudian masuk ke folder:

```bash
cd tcp_chat
```

Jalankan server:

```bash
python tcp_server.py
```

Jika berhasil:

```bash
[TCP SERVER RUNNING]
```

---

## 2. Jalankan TCP Client

Buka terminal baru:

```bash
cd tcp_chat
python tcp_client_gui.py
```

---

# Login

Username dan password tersimpan pada file:

```plaintext
users.json
```

Contoh akun:

```json
{
    "rafi": "123",
    "admin": "admin"
}
```

---

# Cara Kerja Program

1. Client melakukan koneksi ke server
2. Client login menggunakan username dan password
3. Server memvalidasi login
4. Client dapat melakukan chat secara real-time
5. Client dapat mengirim file ke server

---

# Pengiriman File

Client dapat mengirim file menggunakan tombol:

```plaintext
Send File
```

File yang diterima server akan tersimpan pada folder:

```plaintext
uploads/
```

---

# Library yang Digunakan

- socket
- threading
- tkinter
- json
- os

Semua library merupakan bawaan Python.

---

# Error Handling

Program memiliki beberapa penanganan error seperti:

- Validasi login
- Penanganan client disconnect
- Validasi input kosong
- Penanganan error pengiriman file

---

# Screenshot yang Dilampirkan

Tambahkan screenshot:
- TCP server running
- Login berhasil
- Chat antar client
- File transfer berhasil
- Isi folder uploads

---

# Author

Nama: Muhammad Rafi Hardianto

