
# Język skryptowy
### Wykład #1: Wprowadzenie. Typy, operatory, instrukcje.
*dr inż. Michał Kępski* 

<!-- footer: | e-mail: mkepski@ur.edu.pl | 
-->

---
<!-- footer: | Język skryptowy | Wykład #1: Wprowadzenie. Typy, operatory, instrukcje. | dr inż. Michał Kępski |
     page_number: true -->

# Język skryptowy

- Wykład
  - liczba godzin: 10 (stacjonarne) lub 10 (niestacjonarne) 
  - zaliczenie: test (>50%)
- Laboratorium
  - liczba godzin: 15 (stacjonarne) lub 12 (niestacjonarne)
  - zaliczenie: kolokwium (>50%) + rozwiązanie zadań z laboratorium

---

# Literatura

1. *Python 3 : kompletne wprowadzenie do programowania*, Mark Summerfield, Wyd. 2., Helion, 2010.

2. *Dokumentacja języka Python:* https://docs.python.org/3/

3. *Python. Wprowadzenie. Wydanie IV*, Mark Lutz, Helion, 2010.

4. Slajdy z wykładu: https://github.com/majk3l/JS2017 *(katalog lectures)*

---

# Na następne laboratoria...

1. (Wszyscy) https://git-scm.com/book/pl/v1/Pierwsze-kroki-Wprowadzenie-do-kontroli-wersji
  Rozdziały (przeczytać, wykonać przykłady, zapamiętać) :
   - Pierwsze kroki
   - Podstawy Gita

2. (Moja grupa - lab3) Założyć darmowe konto w serwisie github.com

---

# Zagadnienia

1.  **Wstęp do języka Python**.	**Typy, operatory, instrukcje podstawowe**.
2.	Funkcje i klasy
3.	Moduły
4.	Wyjątki
5.	Narzędzia wbudowane
6.	Typowe zadania w języku Python: manipulacja strukturami, danymi, plikami i programami
7.  Numpy

**i inne**

---

#  Python

### Jest językiem:

- skryptowym
- obiektowym
- interpretowanym
- typowanym dynamicznie

---
# PVM (maszyna wirtualna)

&nbsp;
    
```bash

       plik                   kod                 
     źródłowy               bajtowy               wykonanie 
    __________            ___________            ___________
   |          |          |           |          |           |
-> |   m.py   |    ->    |   m.pyc   |    ->    |    PVM    |
   |__________|          |___________|          |___________|
    
```
---

# Alternatywne implementacje

- **CPython** - standardowa implementacja, napisana w języku C.

- **Jython** - implementacja dla języka Java, kod źródłowy tłumaczony jest do kodu bajtowego JVM.

- **IronPython** - implementacja dla platformy .NET.

---

# Co mogę zrobić za pomocą Pythona?

## *Przegląd potencjalnych zastosowań i bibliotek*

---

# Programowanie systemowe

Tworzenie przenośnych i łatwych w utrzymaniu narzędzi służących do administrowania systemami. Przykłady:

- przeszukiwania plików i drzew katalogów
- uruchamianie innych programów 
- wykonywanie przetwarzania równoległego za pomocą procesów i wątków

---

# Programowanie systemowe

## *Po co używać Pythona skoro jest Bash?*

---

# Bash vs Python 
### Porównanie pod kątem programowania narzędzi powłoki

**Bash**
\+ wszechobecny  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \+ łatwe łączenie komend, np: 
```bash
ls -l|tail -n +2|sed 's/\s\s*/ /g'|cut -d ' ' -f 3|sort|uniq 
```
\- nieintuicyjna składnia, duże skrypty często nieczytelne
\- brak natywnego wsparcia dla zaaw. funkcji (np. parsowanie XML)

**Python**
\+ łatwe tworzenie i utrzymanie kodu &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  \+ OOP
\- wymaga instalacji, czasami dodatkowych pakietów, etc.

---

# Bash -  (nie)intuicyjność składni

Efektem wywołania poniższego kodu (plik bashtest.sh):

```bash
#!/bin/bash
var = 10 
```
będzie błąd:
```shell
./bashtest.sh: line 2: var: command not found
```
Natomiast:
```bash
#!/bin/bash
var=10 
```
wykona się poprawnie.

---

# Bash -  (nie)intuicyjność składni



```bash
{ ls -l; df; echo "Done." }
# bash: syntax error: unexpected end of file

{ ls -l; df; echo "Done."; }
# wykona się poprawnie   ^     ### potrzebny średnik

ls -l; df; echo "Done."
# gdy polecenia nie są w bloku kodu, średnik 
# nie jest potrzebny
```
---

# Skrypty internetowe

Biblioteka standardowa Pythona zawiera moduły pozwalające na wykonywanie różnych zadań sieciowych zarówno w trybie klienta, jak i serwera.

- komunikacja za pomocą gniazd
- pobieranie całych stron internetowych za pomocą ich URL 
- analizowanie i generowanie XML, HTML
- obsługa protokołu FTP
---

# Obsługa baz danych

- Dla Pythona istnieją interfejsy do wszystkich najpopularniejszych relacyjnych baz danych
- Moduł do serializacji i deserializacji obiektów (```pickle```)
- Osadzony silnik bazy danych SQL (SQLite) jest standardową częścią samego języka (od wersji 2.5).
---

# Obliczenia numeryczne i programowanie naukowe

- ```numpy``` - szybkie obliczenia na macierzach
- ```scipy```- obliczenia numeryczne i naukowe
- ```scikit-learn``` - uczenie maszynowe
- OpenCV - biblioteka C/C++, metody widzenia maszynowego (computer vision), istnieje interfejs do Pythona

---
# Gry komputerowe & grafika 

- Programowanie gier oraz multimediów dzięki systemowi ```pygame```.
- Komunikacja przez port szeregowy w systemach Windows, Linux i innych dzięki rozszerzeniu ```PySerial```.
- Przetwarzanie grafiki wykonywane za pomocą ```PyOpenGL```.
-  Blender (program do modelowania) jest częściowo napisany w Pythonie, umożliwia rozszerzenia za pomocą skrytpów.

---

# GUI

- TkInter
- PySide
- PyQt
i wiele innych.

---

# Backend serwisów internetowych

Django - wolny i otwarty framework przeznaczony do tworzenia aplikacji internetowych, napisany w Pythonie. Django realizuje wzorzec architektoniczny model-template-view (pokrewny z MVC).

Wśród dobrze znanych witryn, które używają Django, znajdują się witryny Pinterest, Instagram, Fundacji Mozilla, Public Broadcasting Service i The Washington Times.

<sub><sup>źródło: https://pl.wikipedia.org/wiki/Django_(framework)
</sup></sub>

---

# Czy python przyda się podczas zajęć na UR? 

---

## Przedmiot: Aplikacje internetowe 2

Celem przedmiotu jest (cytat za syllabusem):

<sub>*"Nabycie umiejętności w posługiwaniu się frameworkami umożliwiającymi rozszerzającymi możliwości języka Python pod kątem tworzenia aplikacji webowych."*</sub>

<sub>*"Zapoznanie studentów z (...) oraz możliwościami i funkcjami frameworka Django."*</sub>

<sub>*"Nabycie umiejętności tworzenia projektowanie i tworzenia zaawansowanych aplikacji webowych przy użyciu wybranych narzędzi."*</sub>

---
## Przedmiot: Analiza i przetwarzanie  obrazów

&nbsp;

- Przedmiot na studiach magisterskich
- Prowadzący: ten sam co prowadzi Język skryptowy :) 
- Na zajęciach laboratoryjnych: OpenCV + Python 
---

# Wykonywanie programów

## - Interaktywny wiersz poleceń
## - Systemowy wiersz poleceń
## - IDE (np. *PyCharm*)

---

# Interaktywny wiersz poleceń
  
```shell
$ python  
Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:15:05) 
[MSC v.1600 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more 
information.
>>>
```
---

# Systemowy wiersz poleceń

Skrypt o nazwie hello.py:
```python
print("Hello world!")
```
uruchamiamy w konsoli systemowej:

```shell
$ python hello.py
Hello world!
```

---

# ```import```

Kod źródłowy Pythona pogrupowany jest w moduły i pakiety (więcej o modułach na kolejnych wykładach). Słowo kluczowe ```import``` pozwoli na załadowanie elementów z modułu:

```python
import module_name
from module_name import element_name
from module_name import *
```
```python
from decimal import Decimal
from fractions import Fraction
```
---

# Typy danych

         
- Liczby
``` python
10, 3.1415, 1+3j, Decimal, Fraction 
```   
- Łańcuchy znaków 
 ```python 
 'Hello world' 
 ``` 
- Listy 
``` python
[1, [2, 'trzy'], 4]
```
- Słowniki 
``` python
{'imie': 'Jan', 'nazwisko': 'Kowalski'}
```

---

# Typy danych

- Krotki
 ```python
 (1,'A', 2, 'B')
 ```
- Pliki 
 ```python
 myfile = open('dane.csv', 'r')
 ```
- Zbiory  
 ```python
 {'a', 'b', 'c'}
 ```
- Inne typy podstawowe (Boolean, None)

---

# Liczby

- całkowite 
- zmiennoprzecinkowe
- *zespolone*
- *Decimal* (ułamki dziesiętne)
- *Fraction* (ułamki zwykłe)

---


# Operatory arytmetyczne
operator| znaczenie
---|---
x + y |suma x oraz y
x - y |różnica x oraz y
x * y |iloczyn x oraz y
x / y |iloraz x oraz y
x // y |(zaokrąglony w dół) iloraz x oraz y
x % y |reszta z dzielenia x / y
-x |-x
+x |x
abs(x) | wartość bezwzględna x

---

# Operatory arytmetyczne

operator| znaczenie
---|---
int(x)  |x zamienione na typ całkowity
long(x) |x zamienione na typ całkowity nieskończony
float(x)|x zamienione na typ zmiennoprzecinkowy
complex(re,im)| liczba zespolona z częścią rzeczywistą re, urojoną im.
divmod(x, y) | para (x // y, x % y)
pow(x, y) | x do potęgi y
x ** y |x do potęgi y

---

# Łańcuchy tekstowe

W Pythonie napisy zamykane są poprzez pojedynczy, podwójny lub potrójny cudzysłów:

```python
A = """Witaj świecie!"""
B = "Witaj ponownie"
C = 'Witaj ponownie'
# D = 'Witaj' 
```

Do wypisywania służy polecenie ```print```

```python
print("Witaj świecie!")
```
---

# Operator indeksowania

```python
A = "Witaj w świecie Pythona!"
i = 0
j = 5
print(A[0]) #1
print(A[i:j]) #2
```

Wyjście:

 ```W```
 
 ```Witaj```

Uwagi:
- Indeksowanie rozpoczynamy od 0
- A[i:j] oznacza: „Zwróć wszystko z A od przesunięcia i aż do przesunięcia j, ale bez elementu A[j]". 

---
# Operator indeksowania

Dopuszczalnymi indeksami są też ujemne liczby całkowite:
```python
print (A[-1])  # pierwszy element od konca
print (A[-2])  # drugi element od końca
print (a[-5:]) # pięć ostatnich elementów
```
&nbsp;
Zapis  postaci ```A[-1]``` jest równoważny ```A[len(A)-1]```, gdzie ```len(A)``` jest funkcją zwracającą liczbę elementów w A. 

---
# Łańcuchy tekstowe

```python
>>> S = "To jest napis"
>>> S[0]
'T'
>>> S[0] = 't'

# jaki będzie efekt działania ostatniej instrukcji?

```
---
# Łańcuchy tekstowe

```python
>>> S = "To jest napis"
>>> S[0]
'T'
>>> S[0] = 't'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```
---
# Łańcuchy tekstowe

```python
>>> S = "To jest napis"
>>> S[0] = 't'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

**UWAGA**: Łańcuchy tekstowe są niemodyfikowalne (ang. *immutable*). Można jednak używać istniejących łańcuchów do tworzenia nowych:

```python
>>> S = "To jest napis"
>>> S = 't' + S[1:] # + jest operatorem łączenia
>>> print(S)
to jest napis
```
---

# Listy



- Kontenery ogólnego przeznaczenia, uporządkowane pod względem pozycji.
- Przechowują dowolny typ obiektów, także inne listy.
- Obiekty w zakresie jednej listy mogą być różnego typu.
- Są modyfikowalne (ang. *mutable*).


---
# Listy

Definicja listy:

```python
A = [1, 2, 'trzy', 4, 3.1415] # używamy nawiasów kwadratowych
```

Lista jest indeksowana podobnie jak łańcuch tekstowy:

```python
A[0]  # początkowy element, o indeksie 0
A[-1] # element ostatni
```
Podobnie jak w przypadku łańcuchów tekstowych, możemy użyć ```:``` w operatorze indeksowania. 


---
# Listy

Zagnieżdżanie - dowolna kombinacja i głębokość:

```python
A = [1, 2, ['jeden', 'dwa'], [['x', 'y'], 'z'], 3.1415] 
```
Funkcja ```len()``` zwraca długość listy:
```python
>>> len(A)
5
```

--- 

# Krotki (ang. *tuple*)

Od list różnią się tym, że są niemodyfikowalne (podobnie jak łańcuchy tekstowe).

Definicja krotki:
```python
T = (1, 2, 'x', 4)
```

Podobnie jak w przypadku łańcuchów tekstowych i list mamy do dyspozycji operator konkatenacji:

```python
>>> T2 = T + (5, 6)
>>> print(T2)
(1, 2, 'x', 4, 5, 6)
```
---

# Instrukcja warunkowa ```if```


Test wyrażenia logicznego ```if```, następnie opcjonalne sekcje ```elif``` (*else if*) oraz opcjonalna sekcja ```else```:

```python
if testA: # test logiczny
    instrukcjaA1             # B  K	  
    ...                      # L  O
    ...                      # O  D
    instrukcjaAn             # K  U
elif testB: # test opcjonalny
    instrukcjaB1             # B  K  
    ...                      # L  O
    ...                      # O  D
    instrukcjaBn             # K  U
else: # opcjonalny blok else
    instrukcjaC
```
Bloki kodu w Javie czy C++ definiowane w nawiasach klamrowych w Pythonie określane są wcięciami!

---

# Instrukcja warunkowa ```if```

**Java:**

```C 
if (x > y) {
    x = 1;
    y = 2;
}
```

**Python**:

```Python
if x > y:
    x = 1
    y = 2
```
- wiersz nagłówka zakończony dwukropkiem,
- koniec wiersza jest końcem instrukcji (```;``` jest niepotrzebny),
- koniec wcięcia to koniec bloku.

---

# Instrukcja warunkowa ```if```

```Python
x = -10
y = 5
if x > y:
    x = 1
    y = 2
```
x = ? 
y = ?

---

# Instrukcja warunkowa ```if```

```Python
x = -10
y = 5
if x > y:
    x = 1
    y = 2
```
x = -10
y = 5

---

# Instrukcja warunkowa ```if```

```Python
x = -10
y = 5
if x > y:
    x = 1
y = 2
```
x = ? 
y = ?

---

# Instrukcja warunkowa ```if```

```Python
x = -10
y = 5
if x > y:
    x = 1
y = 2 # ta instrukcja nie należy już do bloku if!
```
x = -10 
**y = 2**

---

# Instrukcja pętli ```while```

Instrukcja ```while``` powtarza wykonanie bloku (uwzględniającego odpowiednie wcięcia) dopóki wynik testu logicznego jest prawdziwy:

```python
while test: # test logiczny
    instrukcje  # ciało pętli
else: # opcjonalny blok else wykonywany
    instrukcje # gdy pętla zakończyła się bez wywołania break
```

- ```break```- przerywa wykonanie pętli i powoduje ominięcie instrukcji w bloku else (jeśli taki istnieje),
- ```continue``` - przejście do następnej iteracji najściślej otaczającej ją pętli.

---

# Instrukcja pętli ```while```

Co jest wyjściem poniższego skryptu?

```Python
num = 10
while num > 3:
    num = num - 1
print(num)
```
---

# Instrukcja pętli ```while```

Co jest wyjściem poniższego skryptu?

```Python
num = 10
while num > 3:
    num = num - 1
print(num)
```
Rezultat:
```
> python loop.py
3
```
---

# Instrukcja pętli ```for```

Uniwersalny iterator po sekwencjach:

```python
for item in sequence: # 
    instrukcje  # tu zazwyczaj używany jest item
else: # opcjonalny blok else
    instrukcje 
``` 
