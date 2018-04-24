import random

class Card:
    # słownik symboli unicode
    unicode_dict = {'s': '\u2660', 'h': '\u2665', 'd': '\u2666', 'c': '\u2663'}
       
    def __init__(self, rank, suit):
    # TODO: definicja metody
        pass
    def get_value(self):
    # TODO: definicja metody (ma zwracać kartę w takiej reprezentacji, jak dotychczas, tzn. krotka)
        pass
    def __str__(self):
    # TODO: definicja metody, przydatne do wypisywania karty    
        pass

class Deck():
    
    def __init__(self, *args):
    # TODO: definicja metody, ma tworzyć niepotasowaną talię (jak na poprzednich lab)
        pass
    def __str__(self):
    # TODO: definicja metody, przydatne do wypisywania karty
        pass
    def shuffle(self):
    # TODO: definicja metody, tasowanie
        pass
    def deal(self, players):
    # TODO: definicja metody, otrzymuje listę graczy i rozdaje im karty wywołując na nich metodę take_card z Player
        pass

class Player():

    def __init__(self, money, name=""):
        self.__stack_ = money
        self.__name_ = name
        self.__hand_ = []

    def take_card(self, card):
        self.__hand_.append(card)

    def get_stack_amount(self):
        return self.__stack_

    def get_player_hand_immutable(self):
        return tuple(self.__hand_)

    def cards_to_str(self):
    # TODO: definicja metody, zwraca stringa z kartami gracza
        pass

def histogram(text):
# TODO: wstawić metodę z poprzedniego lab
    pass

# slownik wartosci kart w postaci int, dwojka - 2, ...., as - 14
card_rank_values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
                    "8": 8, "9": 9, "10": 10, "J": 11, "D": 12,
                    "K": 13, "A": 14}


def get_player_hand_rank(hand):
# TODO: wstawić metodę z poprzedniego lab
    pass
 
