import random

# Definicja kart
values = list(range(2, 11)) + ['J', 'Q', 'K', 'A']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
deck = [(value, suit) for value in values for suit in suits]

# Mieszanie i rozdzielanie kart
random.shuffle(deck)
player1_hand, player2_hand = deck[:26], deck[26:]

# Funkcja do porównywania wartości kart
def card_value(card):
    if card[0] in ['J', 'Q', 'K', 'A']:
        return 11 + ['J', 'Q', 'K', 'A'].index(card[0])
    return card[0]

# Funkcja do decyzji gracza
def player_decision(player_number):
    while True:
        decision = input(f"Gracz {player_number}, rzucasz kartę (r) czy poddajesz się (p)? ")
        if decision.strip().lower() in ['r', 'p']:
            return decision.strip().lower()
        else:
            print("Niepoprawna komenda. Proszę wybrać 'r' aby rzucić kartę lub 'p' aby się poddać.")

# Funkcja do rozstrzygania wojny
def resolve_war():
    while True:
        decision = input("Wojna! Gracze, czy dążycie do pokoju (p) czy wojny (w)? ")
        if decision.strip().lower() in ['p', 'w']:
            return decision.strip().lower()
        else:
            print("Niepoprawna komenda. Proszę wybrać 'p' dla pokoju lub 'w' dla wojny.")

# Główna pętla gry
while player1_hand and player2_hand:
    decision1 = player_decision(1)
    if decision1 == 'p':
        print("Gracz 1 poddał się. Gracz 2 wygrywa!")
        break

    decision2 = player_decision(2)
    if decision2 == 'p':
        print("Gracz 2 poddał się. Gracz 1 wygrywa!")
        break

    card1 = player1_hand.pop(0)
    card2 = player2_hand.pop(0)

    print(f"Gracz 1 rzuca kartę: {card1}, Gracz 2 rzuca kartę: {card2}")

    if card_value(card1) > card_value(card2):
        player1_hand.extend([card1, card2])
        print("Gracz 1 wygrywa rundę!")
    elif card_value(card1) < card_value(card2):
        player2_hand.extend([card1, card2])
        print("Gracz 2 wygrywa rundę!")
    else:
        print("Remis! Wojna!")
        war_decision = resolve_war()
        if war_decision == 'p':
            print("Pokój został osiągnięty, karty są odrzucane.")
        else:
            print("Wojna kontynuowana!")
            if player1_hand and player2_hand:
                player1_hand.append(card1)
                player2_hand.append(card2)

# Wynik gry (jeśli nie został wcześniej rozstrzygnięty)
if len(player1_hand) > len(player2_hand):
    print("Player 1 wins with more cards!")
elif len(player1_hand) < len(player2_hand):
    print("Player 2 wins with more cards!")
else:
    print("It's a tie!")

# Zakończenie programu
print("Gra zakończona.")

