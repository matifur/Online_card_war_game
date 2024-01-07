import socket
import os

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)

    while True:
        response = client.recv(1024).decode()

        print(response)
        if "Koniec gry" in response:
            break

        if "Twoja tura, rzuc karte (r) lub poddaj się (p): " in response:
            decision = input("Wybierz akcję: ").strip().lower()
            while decision not in ['r', 'p']:
                print("Niepoprawna komenda. Spróbuj ponownie.")
                decision = input("Wybierz akcję: ").strip().lower()
            client.send(decision.encode())


SERVER = '127.0.1.1'  # Adres IP serwera
PORT = 5050
ADDR = (SERVER, PORT)

main()

