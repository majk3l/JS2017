from poker import *

num_players = 2
players = []

for i in range (0, num_players):
    players.append(Player(1000))

print("Nowa talia:")
deck = Deck()
print(deck)

print("Talia potasowana:")
deck.shuffle()
print(deck)

print("Rozdane karty 2 graczom:")

hands = deck.deal(players)
for player in players:
    print(player.cards_to_str() + " : " + str(get_player_hand_rank(player.get_player_hand_immutable())))
