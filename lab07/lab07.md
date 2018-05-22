# Laboratorium #07 - Powtórka przed kolokwium

## Zadania:

### #1: 
Zdefiniuj funkcję ```substr_conc(str)``` przyjmującą jako parametr niepusty łańcuch tekstowy
o długości ```n```, zwracającą łańcuch tekstowy, który jest wynikiem złączenia ```k```-elementowych
fragmentów parametru ```str```, rozpoczynających się od jego pierwszego znaku ```(k = 1, ... , n)```:
```python
substr_conc ("Test")→ "TTeTesTest"
substr_conc ("abcd")→ "aababcabcd"
```

### #2: 
Zdefiniuj funkcję ```count_2sub_match(a, b)``` przyjmującą jako parametr 2 niepuste łańcuchy
tekstowe ```a``` i ```b```, zliczającą ile unikalnych, dwuelementowych fragmentów łańcucha ```b``` jest
w łańcuchu ```a```.
```python
count_2sub_match('abcdz', 'ababdz')→ 2
count_2sub_match('abcdab', 'ab')→ 2
```
### #3:  
Załóżmy, że chcemy zbudować mur z dużych i małych cegieł. Mała cegła ma długość 1 cala, a duża
5 cali. Napisz ```metodę is_build_pos(small, large, goal)```, która zwróci wartość
```True```/```False``` w zależności od tego, czy da się zbudować mur o długości ```goal``` mając określoną liczbę
małych i dużych cegieł (parametry ```small```, ```large```). 
*Podpowiedź: nie wszystkie cegły muszą zostać użyte.*
is_build_pos(3, 1, 8) → True
is_build_pos (3, 2, 9) → False

### #4:
Napisz skrypt, który pobiera nazwę pliku tekstowego jako parametr podawany z linii poleceń i liczy
średnią długość słowa w tym pliku. Obliczona wartość ma zostać wypisana na ekranie.

### #5:
Napisz skrypt, który pobiera nazwę pliku tekstowego jako parametr podawany z linii poleceń
i tworzy nowy plik, który zawiera te same linie tekstu co plik źródłowy ale ponumerowane od 1 do n
(gdzie n liczba linii tekstu w pliku źródłowym).
