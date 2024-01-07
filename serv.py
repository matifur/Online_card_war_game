import socket
import threading
import random

# Definicja kart
values = list(range(2, 11)) + ['J', 'Q', 'K', 'A']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

# Funkcja do porównywania wartości kart
def card_value(card):
    if card[0] in ['J', 'Q', 'K', 'A']:
        return 11 + ['J', 'Q', 'K', 'A'].index(card[0])
    return card[0]

# Logika gry
def play_game(conn1, conn2):
    deck = [(value, suit) for value in values for suit in suits]
    random.shuffle(deck)
    player1_hand, player2_hand = deck[:26], deck[26:]
    player1_score, player2_score = 0, 0
    rounds_played = 0

    while rounds_played < 31 and player1_hand and player2_hand:
        for conn, hand in [(conn1, player1_hand), (conn2, player2_hand)]:
            conn.sendall("server>> Twoja tura, rzuc karte (r) lub poddaj się (p): ".encode())
            decision = conn.recv(1024).decode().strip().lower()

            if decision == 'p':
                conn.sendall("server>> Poddajesz się. Przegrałeś!\n".encode())
                (conn2 if conn == conn1 else conn1).sendall("Przeciwnik się poddał. Wygrałeś!\n".encode())
                return

            if decision == 'r':
                card = hand.pop(0)
                conn.sendall(f"server>> Rzucasz kartę: {card}\n".encode())
                (conn2 if conn == conn1 else conn1).sendall(f"Przeciwnik rzucił kartę: {card}\n".encode())

            rounds_played += 0.5  # Każdy gracz rzucający kartę to pół rundy

            if rounds_played >= 31:
                break

        if rounds_played >= 31:
            break

        # Podsumowanie rundy
        summary = f"\nserver>> Runda {int(rounds_played)}: {'gracz 1' if decision == 'r' else 'gracz 2'} wygrywa.\n"
        conn1.sendall(summary.encode())
        conn2.sendall(summary.encode())

    # Podsumowanie wyników
    result = f"\nserver>> Koniec gry. Twój wynik: {player1_score}, wynik przeciwnika: {player2_score}\n"
    conn1.sendall(result.encode())
    conn2.sendall(result.encode())
    conn1.close()
    conn2.close()

# Funkcja obsługująca klienta
def handle_client(conn, addr, clients):
    clients.append(conn)
    if len(clients) == 2:
        play_game(clients[0], clients[1])
        clients.clear()

# Start serwera
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")

    clients = []

    while True:
        conn, addr = server.accept()
        print(f"[NEW CONNECTION] {addr} connected.")
        threading.Thread(target=handle_client, args=(conn, addr, clients)).start()

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (SERVER, PORT)

start_server()

