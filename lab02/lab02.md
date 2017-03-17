# Laboratorium #02 - Zadania do samodzielnego wykonania

## Zadania obowiązkowe:

### #1:

Napisz funkcję, która jako parametr przyjmuje napis tekstowy i zwraca histogram znaków
występujących w tym napisie (czyli pary znak-liczba wystąpień). Wynikiem powinien być
słownik. Przykład:

```python
>>> histogram("Ala ma kota")
{'t': 1, 'a': 3, 'l': 1, 'A': 1, 'k': 1, 'm': 1, 'o': 1}
```

### #2:

Napisz następujące funkcje niezbędne do implementacji gry w pokera pięciokartowego dobieranego:

**#2.1:** ```deck()``` - zwraca listę reprezentującą talię kart w kolejności od najmłodszej do najstarszej. Każda karta posiada 2 atrybuty, będące łańcuchem tekstowym:
- rangę - możliwe wartości: ```'2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'D', 'K', 'A'``` (karty od 2 do 10 oraz walet, dama, król, as)
- kolor - możliwe wartości: 
  - ```'c'``` - &clubs; trefl (**c**lubs)
  - ```'d'``` - &diams; karo (**d**iamonds)
  - ```'h'``` - &hearts; kier (**h**earts)
  - ```'s'``` - &spades; pik (**s**pades)
 
Każdym elementem listy powinna być krotka, będąca parą (ranga, kolor). Przykładowo *as pik*:
 
 # &#127137;
 
 reprezentowany będzie jako ```('A', 's')```. Lista powinna zawierać 52 elementy (13 rang * 4 kolory).
 
**#2.2:** ```shuffle_deck(deck)``` - przyjmuje listę kart, zwraca karty potasowane (permutacja). Skorzystaj z: https://docs.python.org/3/library/random.html

**#2.3:** ```deal(deck, n)``` - przyjmuje talię kart (```deck```) oraz liczbę graczy (```n```), zwraca n-elementową listę 5-elementowych list z kartami rozdanymi graczom. Każda 5-elementowa lista kart gracza zawiera 5 krotek reprezentujących kartę.  

--- 

Zasady gry: https://pl.wikipedia.org/wiki/Poker 
