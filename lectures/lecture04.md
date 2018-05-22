
# Język skryptowy
### Wykład #4: Wyjątki, pliki. Biblioteka standardowa.
*dr inż. Michał Kępski* 

<!-- footer: | e-mail: mkepski@ur.edu.pl | 
-->

---
<!-- footer: | Język skryptowy | Wykład #4: Wyjątki, pliki. Biblioteka standardowa. | dr inż. Michał Kępski | https://github.com/majk3l/JS2017/
     page_number: true -->


# Błędy 


- błędy składniowe kodu wychwytywane są na etapie parsowania pliku przez interpreter;

- wyjątkami nazywamy błędy, które wystąpiły w trakcie uruchomienia skryptu;

- niekoniecznie muszą zakończyć działanie - Python dostarcza mechanizmów obsługi wyjątków.

---
# Błędy - przykłady

```python
>>> 10 * (1/0)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    10 * (1/0)
ZeroDivisionError: division by zero
```

```python
>>> 4 + a * 3
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    4 + a * 3
NameError: name 'a' is not defined
```
---
# Przykłady wyjątków
### Exception - podstawowa klasa dla wyjątków. 
### Poniżej kilka przykładów (nazwa - kiedy występuje):
- NameError - gdy w przestrzeniach nazw (lokalnych lub globalnej) nie znaleziono nazwy. 
- IOError - gdy występuje błąd operacji wejścia/wyjścia.
- ImportError - gdy nie można odnaleźć importowanego pakietu.
- IndexError - gdy indeks sekwencji jest poza zakresem.
- KeyError - gdy nie można odnaleźć danego klucza w słowniku.
---


# Błędy składniowe:

```python

>>> while 1 print('Cześć świecie')

SyntaxError: invalid syntax
```

---

# Klauzula ```try-except``` - ogólna składnia

```
try:
    pass
except Exception:
    pass
except Exception as e:
    pass
else:
    pass
finally:
    pass
```
---
# Klauzula ```try-except```

```python
>>> f = open('1.tx')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    f = open('1.tx')
FileNotFoundError: [Errno 2] No such file or directory:'1.tx'
```
---

# Klauzula ```try-except```
&nbsp;
```python
try:
    f = open('1.tx')
except Exception:
    print('Plik nie istnieje!')
```
---
# Klauzula ```try-except```
&nbsp;
###  ```Exception``` może być zbyt ogólne.
&nbsp;
###  Funkcje mogą wyrzucać wiele wyjątków.

---
# Klauzula ```try-except```
&nbsp;
```python
try:
    f = open('1.tx') 
except FileNotFoundError: #obsługa wyjątku konkretnego typu
    print('Plik nie istnieje!')
except Exception as e: # wszystkie inne wyjątki
    print('Błąd! Coś poszło nie tak.')
    print(e)
```
---

# Klauzula ```try-except-else```
&nbsp;

### blok ```else:``` to kod do wykonania gdy wyjątek nie wystąpił:

```python
try:
    f = open('1.tx')
except FileNotFoundError:
    print('Plik nie istnieje!')
else:
    print(f.read())
    f.close()
```
---
# Klauzula ```try-except-else-finally```
&nbsp;

```python
try:
    f = open('1.tx')
except FileNotFoundError:
    print('Plik nie istnieje!')
else:
    print(f.read())
    f.close()
finally:
    print("Ostatecznie (...)")
```

---
# Czy można za pomocą klauzuli ```try-except``` przechwytywać błędy składniowe?
---

# Czy można za pomocą klauzuli ```try-except``` przechwytywać błędy składniowe?

### Tylko przy wywołaniach funkcji ```eval``` lub ```exec```

---
## ``` eval(expression, globals=None, locals=None)```

The arguments are a string and optional globals and locals.

The expression argument is parsed and evaluated as a Python expression (technically speaking, a condition list) using the globals and locals dictionaries as global and local namespace.

The return value is the result of the evaluated expression. 

**Syntax errors are reported as exceptions.** 

---

## ``` eval(expression, globals=None, locals=None)```
&nbsp;

```python
>>> x = 1
>>> eval('x+1')
2
```

---
# ```eval``` vs ```exec```

```eval``` accepts only a single expression, ```exec``` can take a code block that has Python statements: loops, ```try:``` ```except:```, class and function/method definitions and so on.

```eval``` returns the value of the given expression, ```exec``` ignores the return value from its code, and always returns ```None```.

---

# Obsługa plików

Składnia:

```python
file_object = open(file_name [, access_mode][, buffering])
```

Przykład

```python
file = open('test.txt', 'w')
```

---

# Access mode (tryby dostępu do pliku)


- ```r```	Opens a file for reading only. The file pointer is placed at the beginning of the file. This is the default mode.
- ```rb```	Opens a file for reading only in binary format. The file pointer is placed at the beginning of the file. 
- ```r+```	Opens a file for both reading and writing. The file pointer placed at the beginning of the file.
- ```rb+```	Opens a file for both reading and writing in binary format. The file pointer placed at the beginning of the file.

---
# Access mode (tryby dostępu do pliku)

- ```w```	Opens a file for writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.
- ```wb```	Opens a file for writing only in binary format. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.
- ```w+```	Opens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.

- ```wb+```	Opens a file for both writing and reading in binary format. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.

---
# Access mode (tryby dostępu do pliku)

- ```a```	Opens a file for appending. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
- ```ab```	Opens a file for appending in binary format. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.

---
# Access mode (tryby dostępu do pliku)


- ```a+```	Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.
- ```ab+```	Opens a file for both appending and reading in binary format. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.

---
# Używanie pliku
&nbsp;
## Pamiętamy o zamykaniu plików!
&nbsp;
Składnia:

```python
file_object.close()
```
---
# Co się stanie jeśli pliku nie zamkniemy?

```python
files = []
for x in range(100000):
    files.append(open('test.txt', 'w'))
```

```python
OSError: [Errno 24] Too many open files: 'test.txt'
```

---

# Używanie pliku - *context managers*
&nbsp;
### Sposób na uniknięcie konieczności zamykania ręcznego:
&nbsp;


```python
with open('test.txt', 'r') as f:
    pass
# po wyjsciu z bloku plik zostanie zamkniety
print(f.closed())
>>>True
```
---
# Używanie pliku - czytanie zawartości
&nbsp;
```python
with open('test.txt', 'r') as f:
    lines = f.readlines()
    print(lines)
```
---

# Używanie pliku - czytanie zawartości
&nbsp;
```python
with open('test.txt', 'r') as f:
    for line in f:
        print(line)
```
---
# Używanie pliku

- metoda ```write()``` - zapisywanie
- metoda ```read()``` - czytanie, opcjonalny parametr z liczbą bajtów do odczytania
- metoda ```tell()``` - zwraca aktualną pozycję w pliku
- metoda ```seek()``` - służy do poruszania się po otwartym pliku. Jej drugi argument określa znaczenie pierwszego argumentu; jeśli argument drugi wynosi 0, oznacza to, że pierwszy argument odnosi się do pozycji bezwzględnej, 1 oznacza przeskok do innej pozycji względem pozycji. aktualne
---
# Biblioteka standardowa - moduł ```os```

## Przykład

&nbsp;
```python
import os 

print(os.getcwd())
```
---

# Biblioteka standardowa - moduł ```os```

## Przydatne funkcje

```os.chdir()```  - zmiana bieżącego katalogu
```os.getcwd()``` - pobranie ścieżki bieżącego katalogu
```os.mkdir()``` - tworzy pojedynczy folder
```os.makedirs()``` - tworzy wiele zagnieżdżonych folderów na podstawie podanej ścieżki
```os.path.exists``` - sprawdza, czy dana ścieżka istnieje

**i wiele innych**

---
# Biblioteka standardowa - moduł ```socket```

## Klient
```
# utworzenie gniazda INET
sockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# połączenie z serwerem na porcie 80
sockt.connect(("www.python.org", 80))
```
---
# Biblioteka standardowa - moduł ```socket```

## Serwer
```
# utworzenie gniazda INET
servsockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# dowiązanie gniazda do określonego portu
servsockt.bind((socket.gethostname(), 80))
# nasłuchiwanie przychodzących połączeń
servsockt.listen(5)
```
---

```
         *client*                       *server*
       
                                         socket
                                           |    
                                          bind
                                           |
                                         listen
                                           |
          socket                         accept
            |                              | 
         connect - - - - - - - - - - - - ->|
            |                              |
        -->send - - - - - - - - - - - - ->recv<--
       |    |                              |     |
        --recv<- - - - - - - - - - - - -  send --
            |                              |
          close - - - - - - - - - - - - ->recv
                                           |
                                          close
```
---
# Komunikacja sieciowa

### Moduł ```socket``` zapewnia mechanizmy niskopoziomowej komunikacji.

### Inne moduły pythona do komunikacji sieciowej to np. ```http.client```

---

# ```http.client```
```python
>>> import http.client
>>> conn = http.client.HTTPSConnection("www.python.org")
>>> conn.request("GET", "/")
>>> r1 = conn.getresponse()
>>> print(r1.status, r1.reason)
200 OK
>>> data1 = r1.read()  # This will return entire content.
>>> # The following example demonstrates 
>>> # reading data in chunks.
>>> conn.request("GET", "/")
>>> r1 = conn.getresponse()
>>> while not r1.closed:
...     print(r1.read(200))  # 200 bytes
b'<!doctype html>\n<!--[if"...
```






