import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    
    while True:
        msg = input("Komenda: ")
        if msg == "poddaj rozgrywkę":
            client.send(msg.encode("utf-8"))
            break
        elif msg:
            client.send(msg.encode("utf-8"))
            server_msg = client.recv(1024).decode("utf-8")
            print(f"[SERVER] {server_msg}")
    
    client.close()

SERVER = "127.0.0.1"  # Adres IP serwera
PORT = 5050
ADDR = (SERVER, PORT)

main()

