
def hand_rank(hand):
    hand_rank_list = []  # TODO: pobierz liste rang kart gracza. Uzyj listy skladanej.
    hand_color_list = [] # TODO: pobierz liste kolorow kart gracza. Uzyj listy skladanej.

    # histogramy rang kart graczy  okresla ile razy wystapila karta o tej samej randze,
    # potrzebne do ustalenia ukladu kart
    # TODO: uzyj funkcji 'histogram' z poprzedniego laboratorium!
    hand_rank_histogram = histogram(hand_rank_list)
    # histogramy kolorow kart graczy, jesli 5 in hand_color_histogram.values() == True
    # to wszystkie karty sa jednego koloru
    hand_color_histogram = histogram(hand_color_list)
    # czy karty sa "po kolei" (konieczne w: poker krolewski, pokerze, strit)
    # TODO: zaimplementuj funkcje is_rank_sequence(hand) ktora zwraca True jesli karty sa po kolei
    #       w przeciwnym razie zwraca false. Pobiera liste kart jako parametr
    is_hand_rank_sequence = is_rank_sequence(hand) 

    hand_strength = 0 # zwracana zmienna, ja trzeba ustawic
    # ------ sprawdzamy uklad gracza 1:
    # --- sprawdzamy poker krolewski: 5 kart w tym samym kolorze, po kolei, najwyzsza to as
    if( (5 in hand_color_histogram.values()) and ( 'A' in hand_rank_list ) and is_hand_rank_sequence):
        hand_strength = 10
    # --- sprawdzamy poker: 5 kart w tym samym kolorze, po kolei
    elif( ( 5 in hand_color_histogram.values()) and is_hand_rank_sequence):
        hand_strength =  9
    # TODO: za pomoca instrukcji elif oraz else sprawdz ponizsze warunki i ustaw
    #       wartosc zmiennej hand_strength:
    #        - sprawdzamy karete: 4 karty tej samej rangi
    #        - sprawdzamy full house: 3 karty tej samej rangi i 2 karty tej samej rangi
    #        - sprawdzamy kolor
    #        - sprawdzamy strit
    #        - sprawdzamy trojke 
    #        - sprawdzamy wysoka karte
    #        - sprawdzamy dwie pary
    #        - sprawdzamy jedna pare

    return(hand_strength)
