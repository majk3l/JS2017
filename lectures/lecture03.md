
# Język skryptowy
### Wykład #3: Moduły, pakiety i klasy
*dr inż. Michał Kępski* 

<!-- footer: | e-mail: mkepski@ur.edu.pl | 
-->

---
<!-- footer: | Język skryptowy | Wykład #3: Moduły, pakiety i klasy. | dr inż. Michał Kępski | https://github.com/majk3l/JS2017/
     page_number: true -->

# Jeszcze o funkcjach

&nbsp;

```python
def sub(a, b):
	return a - b
    
>>> sub(2, 1)
1
```

---

# Jeszcze o funkcjach

&nbsp;

```python
def sub(a, b):
	return a - b
    
>>> sub(a = 2, b = 1)
1
```
Możemy używać nazw w wywołaniach funkcji (tzw. *keyword arguments*), w dowolnej kolejności.

---
# Wiele argumentów

```python
def many(*args, **kwargs):
    print(args)
    print(kwargs)
    

```

---


# Moduły

## To:

- jednostki organizacji programu Pythona,
- pakują kod w celu ponownego wykorzystania,
- odpowiadają pojedynczym plikom programu Pythona.

---

# Moduły
## Pozwalają na:
- ponowne wykorzystanie kodu źródłowego,
- dzielenie przestrzeni nazw systemu,
- implementowanie współdzielonych usług oraz danych.

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

# Ścieżka wyszukiwania modułów

- lista katalogów
- można ją ustawiać za pomocą zmiennej środowiskowej ```PYTHONPATH```
- można ją modyfikować z poziomu skryptu, zmieniając listę ```sys.path```

---
# Kolejność wyszukiwania modułów

Kiedy moduł o (przykładowej) nazwie **spam** ma zostać zaimportowany, interpreter zaczyna od przeszukania modułów wbudowanych.

Jeśli nie znaleziono tam modułu, wtedy poszukiwany jest plik ```spam.py``` wśród katalogów znajdujących się na liście ```sys.path```, która jest zainicjalizowana następującymi lokalizacjami:

- katalogiem zawierającym główny skrypt,
- katalogami ze zmiennej środowiskowej ```PYTHONPATH```,
- katalogiem instalacyjnym Pythona.

---

# Pakiety modułów

- to katalogi z plikami kodów źródłowych Pythona,
- udostępniają możliwość organizowania plików kodu źródłowego w większe systemy,
- upraszczają i systematyzują ścieżki wyszukiwania modułów.

---

# Importowanie pakietów

Zamiast nazwy modułu podajemy ścieżkę nazw rozdzielonych kropkami:

```python
import dir1.dir2.mod
```

co oznacza, że istnieje katalog ```dir1```, a w nim podkatalog ```dir2``` zawierający plik modułu ```mod.py```.


---

# Definiowanie klas

Najprostsza formą definicji klasy:

```python
class NazwaKlasy:
    <instrukcja1>
    .
    .
    .
    <instrukcjaN>
```
---
# Definiowanie klas

Z jedną klasą bazową:

```python
class NazwaKlasyPotomnej(NazwaKlasyBazowej):
    <instrukcja-1>
    .
    .
    .
    <instrukcja-N>
```
Z wieloma klasami bazowymi:

```python
class NazwaKlasyPotomnej(Bazowa1, Bazowa2, Bazowa3):
    <instrukcja-1>
    .
    .
    .
    <instrukcja-N>
```

---

# Definiowanie klas

Definiowanie pustej klasy:

```
class Pracownik:
    pass

janek = Pracownik() # Tworzy pusty rekord pracownika

# Wypełnienie pól w rekordzie
janek.nazwa = 'Jan Kowalski'
janek.miejsce = 'laboratorium komputerowe'
janek.pensja = 4000

```

Można wykorzystać je aby zgrupować pewną liczbę nazwanych elemtów w jednym ,,zasobniku''.

---

# Zmienne klasy a zmienne obiektu

```python

class Connection:
	
    verbose = 0

    def debug(self):
    	verbose = 1

```

```python
>>> c = Connection()
>>> c.debug()
>>> c.verbose  # jaki będzie wynik działania tej instrukcji? 
```

---

```python

class Connection:
	
    verbose = 0

    def debug(self):
    	verbose = 1

```

```python
>>> c = Connection()
>>> c.debug()
>>> Connection.verbose  #  a wynik tej instrukcji? 
```

---

```python
>>> c = Connection()
>>> c.debug()
>>> c.verbose 
0
>>> Connection.verbose
0
```

***Dlaczego?***

---

```python
>>> c = Connection()
>>> c.debug()
>>> c.verbose 
0
>>> Connection.verbose
0
```

***Dlaczego?***

```python
    def debug(self):
    	verbose = 1
```

```verbose``` jest tutaj zmienną lokalną funkcji ```debug()```. Nie odnosi się ani do klasy, ani do obiektu. 

---

```python

class Connection:
	
    verbose = 0

    def debug(self):
    	self.verbose = 1
        
```
```
>>> c = Connection()
>>> c.debug()
>>> c.verbose
1
>>> c = Connection()
>>> c.verbose
0
```
---
# ```__init__()``` i ```__del__()``` 


- Metody wywoływane odpowienio przy tworzeniu i usuwaniu obiektów. 

- Obiek usuwamy słowem kluczowym ```del```

---
# Przeciążanie za pomocą sygnatur wywołań

- Część obiektowych języków programowania (np. Java) pozwala na przeciążanie funkcji w oparciu o sygnatury typów argumentów.

- Nie ma to zastowania w Pythonie (dynamiczne typowanie)

---

# Przeciążanie

### Czy w takim razie poniższy kod źródłowy się nie uruchomi? (błąd składniowy?)

```python

class C:
    def meth(self, x):
        pass
    def meth(self, x, y, z):
        pass

```
---


# Przeciążanie

### Czy w takim razie poniższy kod źródłowy się nie uruchomi? (błąd składniowy?)

```python

class C:
    def meth(self, x):   # 1
        pass
    def meth(self, x, y, z):  # 2
        pass

```

Kod wykona się poprawnie, widoczna będzie definicja druga (zastąpi pierwszą).

---
