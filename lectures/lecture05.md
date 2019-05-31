
# Język skryptowy
### Wykład #5. Praktyczne zastosowania Pythona: komunikacja sieciowa (przykład). Wirtualne środowiska. NumPy
*dr inż. Michał Kępski*

<!-- footer: | e-mail: mkepski@ur.edu.pl |
-->
<!-- footer: | Język skryptowy | Wykład #5. | dr inż. Michał Kępski | https://github.com/majk3l/JS2017/
     page_number: true -->


---
# Biblioteka standardowa - moduł ```socket```

## Klient
```python
# utworzenie gniazda INET
sockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# połączenie z serwerem na porcie 80
sockt.connect(("www.python.org", 80))
```
---
# Biblioteka standardowa - moduł ```socket```

## Serwer
```python
# utworzenie gniazda INET
servsockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# dowiązanie gniazda do określonego portu
servsockt.bind((socket.gethostname(), 80))
# nasłuchiwanie przychodzących połączeń
servsockt.listen(5)
```
---
# Moduł ```socket``` - schemat typowej komunikacji

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

# Komunikacja sieciowa - przykład


---
# Wirtualne środowiska

---
# Wirtualne środowiska - motywacja

W przypadkach gdy:

- potrzebujemy używać różnych wersji tych samych pakietów, lub gdy pakiety mają różne zależności;
- *legacy code*;
- uruchamianie programów w tzw. *sandbox*-ie.

---

# Co mamy do wyboru?

### Conda

### virtualenv

---
# Czym conda jest a czym nie?

- nie jest dystrybucją pythona (ale Anaconda już tak);
- nie jest tylko i wyłącznie managerem pakietów (jak pip);
- zawiera własny menadżer środowisk wirtualnych (envs);

---
# pip

*pip is the package installer for Python. You can use pip to install packages from the Python Package Index and other indexes.*

---

# pip

```text

$ pip install SomePackage
[...]
Successfully installed SomePackage

```
---
# pip - requirements files

Wygodny sposób umieszczenia listy wszystkich zależności w jednym pliku.

```text
pip install -r requirements.txt
```

---

# conda - instalacja

```

# silent mode installation
wget https://repo.continuum.io/miniconda/Miniconda3-3.7.0-Linux-x86_64.sh -O ~/miniconda.sh
bash ~/miniconda.sh -b -p $HOME/miniconda
export PATH="$HOME/miniconda/bin:$PATH"

```

---
# conda - podstawowe polecenia

```
conda create --name py35 python=3.5

conda env list

conda list

```
---
# conda - ściąga


http://tiny.cc/CondaCheats

---


# NumPy

NumPy jest pakietem Pythona do obliczeń naukowych. Posiada m. in.:

- wydajną implementację obiektu tablic n-wymiarowych,
- mechanizmy *broadcasting* ułatwiające pracę z macierzami,
- narzędzia do integracji kodu w językach C/C++/Fortran,
- implementacje funkcji przydatnych w zagadnieniach algebry liniowej, transformat Fouriera, liczb pseudolosowych (i wielu innych).

Licencja: BSD

---

# Podstawy: typ danych ndarray

Trzonem funkcjonalności NumPy jest obiekt n-wymiarowej tablicy ```ndarray```. Obiekt ten przechowuje dane tego samego typu w wielowymiarowej strukturze i zapewnia szybkie operacje na tych danych (dzięki prekompilowanemu natywnemu kodowi źródłowemu).


---

# ndarray a sekwencje *Pythona* (różnice)

Rozmiar tablic NumPy jest definiowany w momencie utworzenia obiektu i nie może zmieniać się dynamicznie (jak w przypadku list znanych z Pythona). Zmiana rozmiaru będzie skutkowała utworzeniem nowego obiektu ```ndarray``` i usunięciem dotychczasowego.

Elementy tablicy muszą być tego samego typu - każdy element tablicy ma dzięki temu identyczny rozmiar w pamięci.

Obiekty ```ndarray``` dostarczają za to zaawansowanych operacji matematycznych (i nie tylko), które mogą być wydajnie wykonywane na dużych ilościach danych. Pozwala to na pisanie programów szybszych w działaniu i krótszych pod względem liczby linii kodu źródłowego niż programy realizujące te same zadania napisane w Pythonie bez wykorzystania biblioteki NumPy.

---

# ndarray - przykład

```python

>>> import numpy			
>>> a = numpy.zeros((3,5)) # create 3 rows, 5 cols
>>> a                    
array([[0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.]])

```
#### default type is float64

---

# ndarray - dostęp do elementów

```text
[row] [column]  indeksowanie od 0
```

```python
>>> a[0][2] = 5
>>> a
array([[0., 0., 5., 0., 0.],
       [0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.]])

```

---

# ndarray - tworzenie na podstawie innych obiektów

```python
b = numpy.array( [ 1., 2., 3. ] ) # 1-D from list

b = numpy.array( range(20) ) # 1-D from range

b = numpy.array( ( 2., 4., 6. ) ) # 1-D from tuple

```

---

# zmienne, obiekty, referencje


```python

>>> a = numpy.zeros( (3, 3) )
>>> b = a   
>>> c = a.copy()  # c is a new array

>>> b is a
True
>>> c is a
False

```

---

# przykład: *element-wise* multiplication




---
# *"pure" Python*

```python

c = []
for i in range(len(a)):
    c.append(a[i]*b[i])

```

---

# C

```c
for (i = 0; i < rows; i++) {
  c[i] = a[i]*b[i];
}

```
# MATLAB

```matlab
C = A .* B
```

---
# numpy
&nbsp;

```python
c = a * b
```

---
# Dlaczego NumPy jest szybki? Wektoryzacja

Zwektoryzowany kod źródłowy to taki, w którym brak wprost definicji pętli, złożonego indeksowania itd.

- taki kod jest bardziej zwięzły co zazwyczaj poprawia jego czytelność,
- mniej lini kodu -> mniej błędów,
- kod bardziej przypomina notację matematyczną.

---

# Dlaczego NumPy jest szybki? Wektoryzacja


**Pętle, indeksowanie, itd. - są obecne w programie, niejako “pod maską”  biblioteki, w zoptymalizowanym, prekompilowanym kodzie języka C.**


---

# Arytmetyka macierzy w numpy
### (z wartością skalarną)


```
a + 5
a – 3
a * 5
a / 3.14
a.sum()
a > 15
```
---
# Arytmetyka macierzy w numpy
### (2 macierze, operacje *elementwise*)

```python
x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)

# Elementwise sum; both produce the array
# [[ 6.0  8.0]
#  [10.0 12.0]]
print(x + y)
print(np.add(x, y))

# Elementwise difference; both produce the array
# [[-4.0 -4.0]
#  [-4.0 -4.0]]
print(x - y)
print(np.subtract(x, y))

```
---

# Arytmetyka macierzy w numpy
### (2 macierze, operacje *elementwise*)

```python

# Elementwise product; both produce the array
# [[ 5.0 12.0]
#  [21.0 32.0]]
print(x * y)
print(np.multiply(x, y))

# Elementwise division; both produce the array
# [[ 0.2         0.33333333]
#  [ 0.42857143  0.5       ]]
print(x / y)
print(np.divide(x, y))

```
---

# Arytmetyka macierzy w numpy
### (wektor - wektor, wektor - macierz)

```python

import numpy as np

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

v = np.array([9,10])
w = np.array([11, 12])

# Inner product of vectors; both produce 219
print(v.dot(w))
print(np.dot(v, w))

# Matrix / vec product;produce the rank 1 array [29 67]
print(x.dot(v))
print(np.dot(x, v))
```
---

# Arytmetyka macierzy w numpy
### (macierz - macierz)

```python

# Matrix / matrix product;
# both produce the rank 2 array
# [[19 22]
#  [43 50]]

print(x.dot(y))
print(np.dot(x, y))

```
---
# Inne przydatne operacje

```python
import numpy as np

x = np.array([[1,2],[3,4]])

print(np.sum(x))  # Compute sum of all elements;
print(np.sum(x, axis=0))  # Compute sum of each column;
print(np.sum(x, axis=1))  # Compute sum of each row;

```


---

# Inne przydatne operacje

```python

x = np.array([[1,2], [3,4]])
print(x)    # Prints "[[1 2]
            #          [3 4]]"
print(x.T)  # Prints "[[1 3]
            #          [2 4]]"

# Note that taking the transpose of a rank 1 array does nothing:
v = np.array([1,2,3])
print(v)    # Prints "[1 2 3]"
print(v.T)  # Prints "[1 2 3]"

```
---

# Broadcasting


Broadcasting to mechanizm pozwalający na wykonywanie operacji arytmetycznych na tablicach różniących się wielkościami.

---

# Przykład niezbyt wydajny

```python
# We will add the vector v to each row of the matrix x,
# storing the result in the matrix y
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = np.empty_like(x)
# Create an empty matrix with the same shape as x

# Add the vector v to each row of
#the matrix x with an explicit loop
for i in range(4):
    y[i, :] = x[i, :] + v

# Now y is the following
# [[ 2  2  4]
#  [ 5  5  7]
#  [ 8  8 10]
#  [11 11 13]]

print(y)
```
---
# Przykład bardziej wydajny
```python
# We will add the vector v to each row of the matrix x,
# storing the result in the matrix y
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
vv = np.tile(v, (4, 1))   
# Stack 4 copies of v on top of each other
print(vv)                 
# Prints "[[1 0 1]
#          [1 0 1]
#          [1 0 1]
#          [1 0 1]]"
y = x + vv  # Add x and vv elementwise
print(y)  # Prints "[[ 2  2  4
          #          [ 5  5  7]
          #          [ 8  8 10]
          #          [11 11 13]]"

```
---



# Przykład użycia broadcasting

```python
# We will add the vector v to each row of the matrix x,
# storing the result in the matrix y
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = x + v  # Add v to each row of x using broadcasting
print(y)  # Prints "[[ 2  2  4]
          #          [ 5  5  7]
          #          [ 8  8 10]
          #          [11 11 13]]"

```

---

# Literatura

1. https://docs.conda.io/en/latest/
2. https://docs.python.org/3/reference/
3. McKinney, W. (2012). Python for Data Analysis: Data Wrangling with Pandas, NumPy, and IPython.
4. http://cs231n.github.io/python-numpy-tutorial/
