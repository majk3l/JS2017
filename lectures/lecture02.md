
# Język skryptowy
### Wykład #2: Funkcje, zakresy nazw.
*dr inż. Michał Kępski* 

<!-- footer: | e-mail: mkepski@ur.edu.pl | 
-->

---
<!-- footer: | Język skryptowy | Wykład #2: Funkcje, zakresy nazw. | dr inż. Michał Kępski | https://github.com/majk3l/JS2017/
     page_number: true -->

# O typach danych raz jeszcze

## Metody listy:

- ``` s.append(x) ``` - dodaje nowy element ```x``` na końcu ```s```
- ``` s.extend(t) ``` - dodaje nową listę ```t``` na końcu ```s```
- ``` s.count(x) ``` - zlicza wystąpienie ```x``` w ```s```
- ``` s.index(x) ``` - zwraca najmniejszy indeks ```i```, gdzie ```s[i] == x```
- ``` s.pop([i]) ``` - zwraca ```i```-ty element i usuwa go z listy. Jeżeli nie podamy parametru to usunięty zostanie ostatni element
- ``` s.remove(x) ``` - odnajduje ```x``` i usuwa go z listy ```s```
- ``` s.reverse() ``` - odwraca w miejscu kolejność elementów ```s```
- ```s.sort([f]) ``` - sortuje elementy, ```f``` to funkcja porównawcza

---

# Konwersja niektórych typów danych

- Pyton dostarcza gotowe mechanizmy konwersji typów sekwencyjnych.

- Obiekt musi być iterowalny, tzn. posiadać metody ```__iter__()``` lub ```__getitem__()```.

- Konwersja:

```python
>>> t = (1,2,3)        # krotka 
>>> list(t)
[1, 2, 3]              # lista na podstawie krotki
>>> set(t)
{1, 2, 3}              # zbior na podstawie krotki
>>> tuple([1, 2, 3])   
(1, 2, 3)	       # krotka na podstawie listy

```

---

#  ```range```


Klasa ```range``` reprezentuje niemodyfikowalną sekwencję liczb w pewnym zakresie. Zazwyczaj używana w instrukcji pętli ```for```.


*class* **range**(*stop*)
*class* **range**(*start, stop*[, *step*])


Elementy sekwencji ``` r ``` typu **range** określone są następująco:

&nbsp; ``` r[i] = start + step * i ```

Parametr ``` step``` może być dodatni lub ujemny:			
 
- jeśli ```step > 0``` to: ```i >= 0 oraz r[i] < stop```

- jeśli ```step < 0``` to: ```i >= 0 oraz r[i] > stop```

---

# *List Comprehensions*

### to:

- zwięzłe mechanizmy definiowania listy,
- przydatne gdy nowa lista jest wynikiem pewnych operacji na elementach listy istniejącej.



---

# *List Comprehensions*


```python
squares = []
for x in range(10):	   # tworzymy listę wykorzystując
    squares.append(x**2)   # pętlę for
```
po wykonaniu kodu otrzymamy listę:

```python
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```
powyższą listę można zdefiniować w sposób bardziej zwięzły:

```python
squares = [x**2 for x in range(10)] # list comprehension
```

---

# *List Comprehensions*

Składnia dopuszcza opcjonalną instrukcję warunkową:

```python
>>> squares = [x**2 for x in range(10) if x % 2 == 0]
>>> squares
[0, 4, 16, 36, 64]
```

oraz możliwość zagnieżdżania:

```python
>>> matrix = [
...     [1, 2, 3],
...     [4, 5, 6],
...     [7, 8, 9]
... ]
>>> matrix_T = [[row[i] for row in matrix] for i in range(3)]
>>> matrix_T
[[1, 4, 7], [2, 5, 8], [3, 6, 9]]
```
---

# Słowniki

```python 
d = {'name':'Jack', 'age': 26}
```

Dostęp do elementów poprzez operator indeksowania ``` [] ```, w którym podajemy wartość klucza:

``` python 
>>> d['name']
'Jack'

>>> d['city'] = 'London'
>>> d
{'city': 'London', 'name':'Jack', 'age': 26}

```
---

# Słowniki

Usuwanie elementów ze słownika:
```
>>> del d['city']
>>> d
{'name':'Jack', 'age': 26}
```
### Słowniki mogą być zagnieżdżane:

```python
rec = {'dane osobowe': {'imię': 'Ireneusz', 'nazwisko': 
'Zielony'}, 'zawód': ['konstruktor', 'inżynier'],
'wiek': 28}
```

Dostęp do zagnieżdżonych elementów:
```python
>>> rec['dane osobowe']['nazwisko']
'Zielony'
```
---

# Słowniki
```python
rec['zawód'].append('mechanik') # Rozszerzenie listy
>>> rec
{'wiek': 28, 'zawód': ['konstruktor', 'inżynier', 
'mechanik'], 'dane osobowe': {'nazwisko': 'Zielony', 
'imię': 'Ireneusz'}}
```

lista kluczy:

```python 
>>> rec.keys()
dict_keys(['dane osobowe', 'wiek', 'zawód'])
```
---
# Zmienne, obiekty i referencje

**Zmienna** (czyli nazwa)  tworzona jest, kiedy kod pierwszy raz przypisuje jej wartość. Przyszłe przypisania zmieniają wartość utworzonej wcześniej zmiennej.

Zmienna nigdy nie ma dołączonych żadnych informacji o **typie**. Pojęcie to wiąże się z obiektami, a nie nazwami.

---

# Zmienne, obiekty i referencje

Kiedy zmienna pojawia się w wyrażeniu, jest zastępowana przez obiekt, do którego się odnosi.

Wszystkie zmienne muszą mieć jawnie przypisane wartości, zanim będzie można ich użyć.

---

# Zmienne, obiekty i referencje

```python
A = [1, 2, 3]
```
Efektem powyższego przypisania Pythonie jest następująca struktura w pamięci operacyjnej:

```python
      zmienna          referencja            obiekt
      (nazwa)
      _______                              ___________
     |       |             |              |           |
     |   A   | - - - - - - | - - - - - - >| [1, 2, 3] |
     |_______|             |              |___________|
     
     				# wartość licznika referencji
                                # obiektu wynosi 1  
```
---

# Zmienne, obiekty i referencje

```python
B = A
```

```python
      zmienna          referencja          obiekt
      (nazwa)
      _______                              
     |       |             |                         
     |   A   |             |             ___________
     |_______| - - - - - - | - - - - - >|           |    
      _______              |            | [1, 2, 3] |
     |       | - - - - - - | - - - - - >|___________|
     |   B   |             |
     |_______|             |          
 
     				# wartość licznika referencji
                                # obiektu wynosi 2
```
--- 

# Zmienne, obiekty i referencje


Zmienne A i B wskazują na ten sam obiekt:


```python
>>> B.append(4)
>>> B
[1, 2, 3, 4]
>>> A
[1, 2, 3, 4]
```

--- 
# Zmienne, obiekty i referencje
 
- **Zmienne** - wpisy w tabeli systemowej z miejscem na łącze do obiektów.

- **Obiekty** - fragmenty pamięci z ilością miejsca wystarczającą, by zmieścić reprezentowane wartości; ponadto posiadają:
	-   licznik referencji,
	-   pole określające ich typ.

- **Referencje** - powiązania między zmiennymi a obiektami, za którymi automatycznie podąża Python.

---

# Definiowanie funkcji


Funkcje definiuje się używając słowa ```def```:

```python
def name(arg1, arg2,... argN):
    statements
```

Przykład:

```
def maximum(x, y):
    if x > y:
        return x
    else:
        return y
```

---

# Definiowanie funkcji - istotne informacje

- ```def``` def to kod wykonywalny - funkcja nie istnieje dopóki Python nie dotrze do jej definicji i nie wykona instrukcji ```def```,
- ```return``` przesyła wynikowy obiekt z powrotem do wywołującego,
- argumenty przekazywane są przez referencję.


---

# Definiowanie funkcji

- Zmienne w definicji funkcji, nie są połączone w żaden sposób z innymi zmiennymi o tych samych nazwach, ale użytych w innej części programu. 

- Zmienne są **lokalne** dla funkcji.

- Każda zmienna ma swój zakres, czyli blok, w którym została zadeklarowana, zaczynając od miejsca zdefiniowania jej nazwy.

---

# Zakresy nazw

### Python wyszukuje zmiennych w przestrzeni nazw (ang. *namespace*).

### Zakres (ang. *scope*) związany jest miejscem definicji i wyszukiwania zmiennej w przestrzeni nazw.

### Tworzenie zmiennych w Pythonie wiąże się z:

- przypisaniem do zmiennej wartości (konieczne przed pierwszym użyciem),
- wykorzystaniem przez Pythona miejsca przypisania do powiązania zmiennej z przestrzenią nazw.

---
# Zakresy nazw

```python
      __________________________________________________
     |                                                  |
     | ZAKRES WBUDOWANY (Python)                        |
     |  ______________________________________________  |
     | |                                              | |
     | | ZAKRES GLOBALNY                              | |   
     | |  __________________________________________  | |
     | | |                                          | | |
     | | | ZAKRESY LOKALNE FUNKCJI ZAWIERAJĄCYCH    | | |
     | | |  ______________________________________  | | |
     | | | |                                      | | | | 
     | | | | ZAKRES LOKALNY                       | | | |
     | | | |______________________________________| | | |
     | | |__________________________________________| | |
     | |______________________________________________| |
     |__________________________________________________|

```
---
# Zakresy nazw - istotne informacje

- zakres globalny rozciąga się jedynie na jeden plik,
- każde wywołanie funkcji tworzy nowy zakres lokalny,
- przprzypisane nazwy są lokalne o ile nie zostaną zadeklarowane jako globalne.

---

# ```global```


```python
globvar = 0

def set_globvar_to_one():
    global globvar    
    globvar = 1

def print_globvar():
    print(globvar)    

set_globvar_to_one()
print_globvar()     
```

---

# Przykłady

```python
X = 99 

def func(Y): 
Z = X + Y 
return Z

func(1)
```
---

# Przykłady

### Wcięcia! Kod z poprzedniegu slajdu nie wykona się poprawnie!

```python
X = 99 

def func(Y): 
    Z = X + Y 
    return Z

func(1)
```
---

# Przykłady

```python
X = 99 # przypisane w module - zatem globalne

def func(Y): 
    Z = X + Y 
    return Z

func(1) # func w module: wynik = 100
```

---

# Przykłady


```python
X = 99 # Zmienna z zakresu globalnego — nieużywana

def f1():
    X = 88 # Zmienna lokalna z zakresu zawierającego
    def f2():
        print(X) # Referencja w zagnieżdżonej instrukcji def
   f2()

f1()
```

---

# Przykłady


```python
X = 99 # Zmienna z zakresu globalnego — nieużywana

def f1():
    X = 88 # Zmienna lokalna z zakresu zawierającego
    def f2():
        print(X) # Referencja w zagnieżdżonej instrukcji def
   f2()

f1()
```
---

# Przykłady


```python
X = 99 # Zmienna z zakresu globalnego — nieużywana

def f1():
    X = 88 # Zmienna lokalna z zakresu zawierającego
    def f2():
        print(X) # Referencja w zagnieżdżonej instrukcji def
   f2()

f1() # wypisuje 88
```

