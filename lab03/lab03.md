# Laboratorium #03 - Zadania do samodzielnego wykonania

## Zadania obowiązkowe:

### #1:

Zaimplementuj funkcję ```hand_rank(hand)```, która będzie przyjmować jako parametr 5-elementową listę krotek reprezentujących karty
(zob. lab02.md) i zwracać liczbę całkowitą w zakresie od 10 do 1 reprezentującą rangę układu tych 5 kart w pokerze pięciokartowym 
dobieranym (http://pl.wikipedia.org/wiki/Poker), gdzie 10 - to poker królewski, 9 - poker, 8 - kareta, 7 - full itd. Do implementacji wykorzystaj 
szablon funkcji umieszczony w repozytorium, w pliku ```poker.py```. Umieść w tym pliku swoją definicję funkcji ```histogram```.

Zwróć uwagę, że o starszeństwie decydują różne reguły, które opierają się na 3 atrybutach:

- czy wszystkie karty są jednego koloru,
- czy karty są "po kolei",
- czy w układzie występują powtórzenia, tzn. zawiera 4, 3, 2 karty o tej samej randze.

Do sprawdzenia ile rang kart powtarza się, najłatwiej będzie użyć zaimplementowanej na poprzednich laboratoriach funkcji ```histogram``` - 
funkcja ta przyjmowała łańcuch tekstowy, ale jeżeli została zaimplementowana z użyciem pętli ```for``` nic nie stoi na przeszkodzie wywołać
ją z listą jako parametr. Gdy wywołamy ją na liście rang karty, możemy sprawdzić czy występują powtórzenia kart, natomiast gdy wywołamy ją
na liście kolorów kart możemy sprawdzić czy wszystkie karty są jednego koloru. Przykładowo mamy listę:

```[('A','c'), ('A','s'), ('A','h'), ('9','c'), ('8','s')]```

która reprezentuje następujący układ kart:

 # &#127153; &#127185; &#127137; &#127193; &#127144;

możemy stworzyć listę samych rang z układu, która będzie wyglądać następująco:

```['A', 'A', 'A', '9', '8']```

po wywołaniu funkcji ```histogram``` na powyższej liście otrzymamy słownik:

```{'8': 1, '9': 1, 'A': 3}```

po sprawdzeniu wartości słownika wiemy, czy karta o jakiejś randze pojawiła się więcej niż raz (w tym wypadku as).
