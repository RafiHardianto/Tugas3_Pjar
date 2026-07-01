# UDP CHAT APPLICATION

## Deskripsi

Program ini merupakan aplikasi chat sederhana menggunakan protokol UDP (User Datagram Protocol) dengan konsep client-server.

Program dibuat menggunakan Python dan GUI sederhana menggunakan Tkinter.

---

# Fitur Program

- Multi client chat
- Broadcast message
- Logging pesan ke file
- Validasi input
- GUI sederhana
- Format pesan username: pesan

---

# Struktur Folder

```plaintext
udp_chat/
│
├── udp_server.py
├── udp_client_gui.py
├── udp_log.txt
└── README.md
```

---

# Cara Menjalankan Program

## 1. Jalankan UDP Server

Buka terminal kemudian masuk ke folder:

```bash
cd udp_chat
```

Jalankan server:

```bash
python udp_server.py
```

Jika berhasil:

```bash
[UDP SERVER RUNNING] 0.0.0.0:5000
```

---

## 2. Jalankan UDP Client

Buka terminal baru:

```bash
cd udp_chat
python udp_client_gui.py
```

Masukkan username saat diminta.

Client dapat dijalankan lebih dari satu untuk melakukan chat.

---

# Cara Kerja Program

1. Client mengirim pesan ke server
2. Server menerima pesan
3. Server melakukan broadcast ke seluruh client
4. Pesan disimpan ke file log

---

# Format Pesan

```plaintext
username: pesan
```

Contoh:

```plaintext
rafi: Halo semuanya
```

---

# Logging

Semua pesan akan disimpan pada file:

```plaintext
udp_log.txt
```

Contoh isi log:

```plaintext
[20:30:11] rafi: Halo
[20:30:15] admin: Hai juga
```

---

# Library yang Digunakan

- socket
- threading
- tkinter
- datetime

Semua library merupakan bawaan Python.

---

# Screenshot yang Dilampirkan

Tambahkan screenshot:
- UDP server running
- Chat antar client
- Isi file udp_log.txt

---

# Author

Nama: Muhammad Rafi Hardianto

