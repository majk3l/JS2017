# Język Python – podstawowe informacje

Python to język skryptowy, interpretowany - co oznacza, że piszemy skrypt, a następnie
wykonujemy go za pomocą interpretera. Istnieją dwie główne wersje Pythona, Python 2
i Python 3. Na zajęciach laboratoryjnych wykorzystywana będzie wersja 3.,

Przez skrypt rozumiemy plik tekstowy o rozszerzeniu .py. By go wykonać wydajemy
polecenie:

```
python nazwa_pliku.py
```

## Hello, World!

Do wypisywania łańcuchów tekstowych w Pythonie służy polecenie print. Uruchom skrypt hello_world.py z repozytorium i zaobserwuj jego działanie.

```python
print("""Hello world""")
print("Hello again")
print('Hello again')
# print('Ta linia rozpoczynajaca sie od # jest komentarzem i nie zostanie wykonana')
```


W Pythonie napisy zamykane są poprzez pojedynczy lub podwójny cudzysłów. Istnieje
możliwość ograniczenia tekstu potrójnymi cudzysłowami (dowolnego typu) - tekst będzie
mógł wtedy zajmować więcej niż jeden wiersz.

Kolejny fragment kodu prezentuje wykorzystanie operatora indeksowania. Indeksowanie, podobnie jak w C++ czy Javie, rozpoczynamy od 0. 
Wykonaj poniższy przykład w środowisku Pythona:

```python
A = "Welcome to Python's world!"
i = 0
j = 7
print(A[0]) #1
print(A[i:j]) #2
```
Wyjściem skryptu są:

1. pierwszy znak łańcucha, 
2. określony jego fragment fragment łańcucha tekstowego, który jest ograniczony półotwartym przedziałem.  Taki fragment nazywamy wycinkiem (ang. slice).

Indeksowanie  w formie A[i:j], oznacza: „Zwróć wszystko z A od
przesunięcia i aż do przesunięcia j, ale bez elementu A[j]". Dopuszczalnymi indeksami są nie tylko dodatnie, ale i ujemne liczby całkowite. Oznaczają
one indeksowanie od końca. Wykonaj poniższy kod:

```python
print (A[-1]) # Pierwszy element od konca, formalnie taki zapis jest rownowazny A[len(A)-1]
print (A[-2]) # Drugi element od końca
print (a[-5:])  
```

## Wcięcia






