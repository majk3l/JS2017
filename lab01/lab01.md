# Laboratorium #01 - Zadania do samodzielnego wykonania

## Zadania obowiązkowe:

### #1:
Napisz prosty skrypt, który przyjmuje jako parametry dwie liczby oraz znak operacji (+, -, *) i wykonuje na nich proste operacje arytmetyczne. Skrypt zapisz pod nazwą ```arithmetics.py```. Do porównywania łańcuchów tekstowych wykorzystaj operator ==. Parametry powinny być oddzielone spacjami. Przykład działania (skrypt uruchomiony z wiersza poleceń):
```bash
python arithmetics.py 2 + 4
6
```

### #2:
Napisz skrypt, który wylicza na podstawie zadanego argumentu (daty w postacirrrr-mm-dd) liczbę dni od tego czasu do daty aktualnej. Skrypt zapisz pod nazwą ```days.py```. Skorzystaj z: https://docs.python.org/3/library/datetime.html#date-objects

### #3:
Napisz skrypt, który policzy ile argumentów podanych przez użytkownika (oddzielonych spacjami) ma 3 lub więcej znaków. Skrypt zapisz pod nazwą ```arguments.py```. Przykład działania:
```bash
python arguments.py o co chodzi z tym Pythonem
3
```
zmodyfikuj skrypt tak, aby z listy argumentów, wybierane były argumenty o liczbie
znaków 3 lub więcej, a następnie łączone w odwrotnej kolejności w napis. Uzyskany w ten sposób napis należy wyświetlić. Przykład:
```bash
python arguments.py o co chodzi z tym Pythonem
3
Pythonem tym chodzi
```
### #4:
Napisz program ```quadratic.py```  do obliczania miejsc zerowych równania kwadratowego. Współczynniki (a, b, c) podawane z wiersza poleceń. Wyjście programu powinno być następujące:
- pierwsza linia wyjścia: liczba miejsc zerowych
- druga linia wyjścia: miejsca zerowe oddzielone spacją, o ile istnieją. 

W przypadku braku miejsc zerowych skrypt powinien wypisać linię zawierającą liczbę 0. Przykład:

```bash
python quadratic.py 1 4 3
2
-1.0 -3.0
```
