import socket
import threading
import random

def handle_client(conn, addr, other_conn):
    print(f"[NEW CONNECTION] {addr} connected.")
    
    connected = True
    while connected:
        msg = conn.recv(1024).decode("utf-8")
        if msg == "poddaj rozgrywkę":
            other_conn.sendall("Wygrana".encode("utf-8"))
            break
        elif msg:
            print(f"[{addr}] {msg}")
            other_conn.sendall(msg.encode("utf-8"))
    
    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        if threading.activeCount() - 1 < 2:  # Dopuszczenie tylko dwóch graczy
            other_conn, other_addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr, other_conn))
            thread.start()
            other_thread = threading.Thread(target=handle_client, args=(other_conn, other_addr, conn))
            other_thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

print("[STARTING] server is starting...")
start()
