# Język PYTHON – Podstawowe informacje

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
#!/usr/bin/env python
print("""Hello world""")
print("Hello again")
print('Hello again')
```

W Pythonie napisy zamykane są poprzez pojedynczy lub podwójny cudzysłów. Istnieje
możliwość ograniczenia tekstu potrójnymi cudzysłowami (dowolnego typu) - tekst będzie
mógł wtedy zajmować więcej niż jeden wiersz.
Kolejny fragment kodu prezentuje wykorzystanie operatora indeksowania. Wykonaj go w środowisku
Pythona:

```
#!/usr/bin/env python
a = "Welcome to Python's world!"
i = 0
j = 7
print(a[0])
print(a[i:j])
```
Wyjściem skryptu jest określony fragment łańcucha tekstowego, który jest ograniczony
półotwartym przedziałem <i; j). Zwróć uwagę, że takie indeksowanie pomija element a[j].
Indeksowanie rozpoczynamy od 0. Operatorem konkatenacji (łączenia) jest +.
dopuszczalnymi indeksami są nie tylko dodatnie, ale i ujemne liczby całkowite. Oznaczają
one dostęp do końcowych elementów tablicy. Wykonaj poniższy kod:

```
print (a[-2])
print (a[-5:])
```






