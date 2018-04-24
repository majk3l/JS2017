# Laboratorium #04 - Zadania do samodzielnego wykonania

## Zadania obowiązkowe:

Celem laboratorium jest wprowadzenie klas do projektu aplikacji pokera pięciokartowego dobieranego. Zadanie polega na uzupełnieniu implementacji klas z przygotowanego szablonu (plik ```poker.py``` z repozytorium) tak, aby poprawnie udało się uruchomić skrypt główny (```main.py```), który korzysta z funkcjonalności dostarczanej przez klasy:

- ```Card``` - reprezentuje kartę. Powinna mieć dwa pola do przechowywania koloru i rangi, metodę zwracającą jej reprezentację w postaci krotki i metodę ```__str__``` która będzie potrzeba do wypisywania karty funkcją ```print```.

- ```Deck``` - reprezentuje talię. Powinna mieć jedno pole (listę) do przechowywania kart oraz metody do tasowania, rozdawania i ```__str__```.

- ```Player``` - reprezentuje gracza. Większość jej funkcjonalności jest już dostarczona.

Plik ```poker.py``` powinien zawierać też funkcje z poprzedniego laboratorium (histogram i funkcję do określania wysokości układu gracza: ```get_player_hand_rank```). Proszę zwrócić uwagę, że w nowym zamyśle do funkcji ```get_player_hand_rank``` przekazywana jest krotka zawierająca karty, a nie jak wcześniej listę krotek (ranga, kolor). Należy więc odpowiednio zmodyfikować implementację tej funkcji. 

Przykładowe rezultaty uruchomienia skryptu głównego po poprawnym zaimplementowaniu funkcjonalności:

```
Nowa talia:
2♣ 2♦ 2♥ 2♠ 3♣ 3♦ 3♥ 3♠ 4♣ 4♦ 4♥ 4♠ 5♣ 5♦ 5♥ 5♠ 6♣ 6♦ 6♥ 6♠ 7♣ 7♦ 7♥ 7♠ 8♣ 8♦ 8♥ 8♠ 9♣ 9♦ 9♥ 9♠ 10♣ 10♦ 10♥ 10♠ J♣ J♦ J♥ J♠ D♣ D♦ D♥ D♠ K♣ K♦ K♥ K♠ A♣ A♦ A♥ A♠ 
Talia potasowana:
4♥ 9♣ 6♦ 6♣ 2♦ 8♥ 5♥ 7♠ D♦ 4♣ D♣ 5♣ 2♣ D♠ K♥ J♠ 3♣ A♦ K♣ 2♥ 8♣ A♣ J♣ 4♦ 10♦ 6♠ 3♠ 10♠ 7♦ 4♠ 10♥ 5♦ 9♥ 7♥ 7♣ 3♥ 5♠ K♠ 3♦ J♦ 10♣ 2♠ 8♠ A♠ J♥ A♥ K♦ 6♥ 9♦ 8♦ D♥ 9♠ 
Rozdane karty 2 graczom:
9♠ 8♦ 6♥ A♥ A♠  : 1
D♥ 9♦ K♦ J♥ 8♠  : 0
```

```
Nowa talia:
2♣ 2♦ 2♥ 2♠ 3♣ 3♦ 3♥ 3♠ 4♣ 4♦ 4♥ 4♠ 5♣ 5♦ 5♥ 5♠ 6♣ 6♦ 6♥ 6♠ 7♣ 7♦ 7♥ 7♠ 8♣ 8♦ 8♥ 8♠ 9♣ 9♦ 9♥ 9♠ 10♣ 10♦ 10♥ 10♠ J♣ J♦ J♥ J♠ D♣ D♦ D♥ D♠ K♣ K♦ K♥ K♠ A♣ A♦ A♥ A♠ 
Talia potasowana:
7♦ 8♣ D♠ 5♠ K♣ 7♣ 4♦ 2♦ 6♦ K♠ A♠ 9♣ 3♠ 2♣ A♥ K♥ 5♣ J♠ D♦ A♦ 4♠ 5♥ 3♣ 5♦ 10♣ J♣ J♦ 2♠ 8♠ 4♣ 9♠ A♣ 4♥ 10♦ 2♥ D♣ 10♠ D♥ J♥ 8♥ 9♥ K♦ 6♥ 7♥ 3♦ 10♥ 6♣ 3♥ 6♠ 8♦ 9♦ 7♠ 
Rozdane karty 2 graczom:
7♠ 8♦ 3♥ 10♥ 7♥  : 1
9♦ 6♠ 6♣ 3♦ 6♥  : 3
```
