[Programación Funcional](../README.md)> Introducción

## Contenido

- [Contenido](#contenido)
- [Listas](#listas)
- [Uso de listas](#uso-de-listas)
- [Slides](#slides)
- [Tuplas](#tuplas)
- [Dictionaries](#dictionaries)
- [Anidamiento de estructuras](#anidamiento-de-estructuras)
- [Una lista de diccionarios](#una-lista-de-diccionarios)
- [Una lista en un diccionario](#una-lista-en-un-diccionario)
- [Un diccionario en un diccionario](#un-diccionario-en-un-diccionario)
- [List Comprehensions](#list-comprehensions)
	- [Ejercicios 1.1:](#ejercicios-11)
- [Dictionary comprehensions](#dictionary-comprehensions)
	- [Ejercicios 1.2](#ejercicios-12)

## Listas

Recuerda que una lista es una colección de elementos en un orden en particular. Se pueden crear listas que incluyan letras, dígitos, cadenas. Se puede colocar cualquier tipo de dato en una lista y los elementos de la lista no necesitan estar en un orden en particular. 

```python
colors = ['red', 'blue', 'white', 'yellow', 'orange']
print(colors)
```

**Acceso de un elemento de la lista**

```python
print(colors[0])
```

**Modificar elementos de una lista**

```python
colors = ['red', 'blue', 'white', 'yellow', 'orange']
print(colors)

colors[0] = 'black'
print(colors)
```

**Agregar elementos a una lista**

```python
colors = ['red', 'blue', 'white', 'yellow', 'orange']
print(colors)

colors.append('black')
print(colors)
```

**Insertar un elemento en una lista**

```python
colors = ['red', 'blue', 'white', 'yellow', 'orange']

colors.insert(0,'black')
print(colors)
```

**Eliminar elementos de una lista**

```python
colors = ['red', 'blue', 'white', 'yellow', 'orange']
print(colors)

del colors[0]
print(colors)
```

**Eliminar un elemento de la lista con `pop()`**, elimina el último elemento de la lista.

```python
colors = ['red', 'blue', 'white', 'yellow', 'orange']
print(colors)

popped_colors = colors.pop()
print(colors)
print(popped_colors)
```

**Eliminar un elemento de la lista con `pop()`**, de una posición en particular.

```python
colors = ['red', 'blue', 'white', 'yellow', 'orange']
print(colors)

first_popped = colors.pop(0)
print(colors)
print(first_popped)
```

**Eliminar un elemento de la lista por valor**

```python
colors = ['red', 'blue', 'white', 'yellow', 'orange']
print(colors)

colors.remove('white')
print(colors)
```

**Ordenar una lista con `sort()` de forma permanente**

```python
figures = ['rectangle', 'traingle', 'square', 'circle']
figures.sort()
print(figures)
```

El método s`ort()` cambian permanentemente el orden de los elementos. También se pueden ordenar de manera inversa.

```python
figures = ['rectangle', 'traingle', 'square', 'circle']
figures.sort(reverse=True)
print(figures)
```

**Ordenar una lista con `sorted()` de forma temporal**

```python
figures = ['rectangle', 'traingle', 'square', 'circle']

print(sorted(figures))
print(figures)
```

**Imprimir una lista en orden inverso**

```python
figures = ['rectangle', 'traingle', 'square', 'circle']
figures.reverse()
print(figures)
```

La función `reverse()` no ordena los elementos en orden inverso, solo invierte el orden de la lista.

**Tamaño de una lista**

```python
figures = ['rectangle', 'traingle', 'square', 'circle']
len(figures)
```

## Uso de listas

**`for()` sobre una lista**

```python
rock_stars = ['Bowie', 'Jagger', 'Morrison', 'Ozzy']

for rock_star in rock_stars:
	print(rock_star)
```

**Listas numéricas**

```python
for value in range(1,10):
	print(value)
```

**Uso de `range()` para crear una lista de números:**

```python
numbers = list(range(1,10))
print(numbers)

even_numbers = list(range(1,11, 2))
print(even_numbers)
```

Crear una lista de los primeros diez números elevados al cuadrado.

```python
squares = []
for values in range(1, 11):
	square = value ** 2
	squares.append(square)

print(squares)
```

**Estadística simple con lista de números.**

```python
numbers = [4, 6, 2, 7, 9, 3, 1, 5, 8, 0]
min(numbers)
max(numbers)
sum(numbers)
```

Más detalles en [statistics](https://docs.python.org/3/library/statistics.html).

## Slides

**Slicing**

```python
rock_stars = ['Bowie', 'Jagger', 'Morrison', 'Ozzy']

print(rock_stars[0:3])
```

El código imprime una rebanada de la lista, incluyendo los tres primeros nombres.

**Copiar una lista**

```python
rockstars = ['Bowie', 'Jagger', 'Morrison', 'Ozzy']

my_favorite_rockstars = rockstars[:]
print(my_favorite_rockstars)
```

## Tuplas

En algunos casos es deseable crear listas de elementos que no puedan ser modificados, caso contrario a lo que sucede con las listas revisadas anteriormente.

**Definición de una tupla**

```python
coordenates = (200, 50)
print(coordenates[0])
print(coordenates[1])
```

**Ciclos en tuplas**

```python
coordenates = (200, 50)
for coordenate in coordenates:
	print(coordenate)
```

**Sobreescribir una tupla**

A pesar de que las tuplas no pueden ser modificadas, es posible volver asignar un nuevo valor a la variable.

```python
coordenates = (200, 50)
print(coordenates)

coordenates = (400, 100)
print(coordenates)
```

## Dictionaries

Un diccionario permite conectar piezas de información relacionada. Los diccionarios permiten almacenar casi cualquier tipo de información. 

**Un diccionario simple**

```python
alien_o = {'color': 'green', 'points': 5}

print(alien_o['color'])
print(alien_o['points'])
```

**Agregar nuevos pares de datos**

```python
print(alien_o)

alien_o['x_position'] = 0
alien_o['y_position'] = 25
print(alien_o)
```

**Inicializar un diccionario vacío**

```python
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)
```

**Modificar valores de un diccionario**

```python
alien_0['color'] = 'yellow'
```

**Eliminar un par clave-valor**

```python
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)
```

**Diccionario de objetos similares**

```python
favorite_languages = {
	'antonio' : 'python',
	'daniela' : 'c',
	'fabian' : 'javascript',
	'diego' : 'python'
}

print(favorite_languages['daniela'])
```

**Ciclos sobre todos los pares clave-valor**

```python
user = {
	'username' : 'galactico',
	'first' : 'angel',
	'last' : 'leguizamo'
}

for key, value in user.items():
	print("\nKey: " + Key)
	print("Value" + value)
```

Otro ejemplo

```python
favorite_languages = {
	'antonio' : 'python',
	'daniela' : 'c',
	'fabian' : 'javascript',
	'diego' : 'python'
}

for name, language in favorite_languages.items():
	print(name)
	print(language)
```

**Ciclo sobre todas las llaves en un diccionario**

```python
favorite_languages = {
	'antonio' : 'python',
	'daniela' : 'c',
	'fabian' : 'javascript',
	'diego' : 'python'
}

for name in favorite_languages.keys():
	print(name)
```

**Ciclo sobre todas las llaves en un diccionario en orden**

```python
favorite_languages = {
	'antonio' : 'python',
	'daniela' : 'c',
	'fabian' : 'javascript',
	'diego' : 'python'
}

for name in sorted(favorite_languages.keys()):
	print(name)
```

**Ciclos sobre todos los valores de un diccionario**

```python
favorite_languages = {
	'antonio' : 'python',
	'daniela' : 'c',
	'fabian' : 'javascript',
	'diego' : 'python'
}

for language in favorite_languages.values():
	print(language)
```

## Anidamiento de estructuras

## Una lista de diccionarios

```python
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
	print(alien)
```

## Una lista en un diccionario

```python
pizza = {
	'crust' : 'think',
	'toopings' : ['mushrooms', 'extra cheese']
}

for topping in pizza['toopings']:
	print(topping)
```

Otro ejemplo:

```python
favorite_languages = {
	'antonio' : ['python', 'ruby'],
	'daniela' : ['c'],
	'fabian' : ['javascript', 'go'],
	'diego' : ['python', 'haskell']
}

for name, languages in favorite_languages.items():
	print(name)
	for language in languages:
		print(language)
```

## Un diccionario en un diccionario

```python
users = {
	'ironman' : {
		'first' : 'tony',
		'last' : 'stark',
		'location' : 'manhattan'
		},

	'spiderman' : {
		'first' : 'peter',
		'last' : 'parker',
		'location' : 'queens'
		}
}

```

## List Comprehensions

Un ***list comprenhension*** combina el ciclo `for` y la creación de nuevos elementos en una sola línea y automáticamente agrega cada nuevo elemento a la lista.

```python
squares = [value**2 for value in range(1, 11)]
print(squares)
```

Sintaxis:

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ad7a2195-f95a-48f5-8345-3724dbb5b6f3/Untitled.png)

Ejemplo 1. Crear una lista de números elevados al cuadrado que no son divisibles entre tres.

```python
def run():
    squares = [i**2 for i in range(1,101) if i % 3 != 0]
    

if __name__ == "__main__":
    run()
```

Crear una lista con todos números (máximo 5 dígitos(¡) que a la vez sean múltiplos de 4, 6 y de 9.

```python
def run():
    solution = [i for i in range(1,100000) if i %  36 == 0 ]
    print(solution)

if __name__ == '__main__':
    run()
```

### Ejercicios 1.1:

A partir de de la definición de la tupla `students`, crear las siguientes listas:

- Todos los estudiantes con una edad mayor o igual a 18
- Todos las estudiantes con una edad menor a 18 y sexo ‘M’
- Todos los estudiantes con un promedio mayor o igual a 6.0

```python
from statistics import mean

def run():
		students = (
			('Jairo', [4.5, 3.2, 6.1], 21, 'H'),
			('Yaneth', [5.4, 2.3, 1.6], 19, 'M'),
			('Carlos', [8.5, 8.2, 8.1], 23, 'H'),
			('Anabel', [9.5, 9.2, 8.1], 17, 'M'),
			('Roberto', [7.5, 7.2, 7.1], 16, 'H'),
		)
    
		solution = []
        print(solution)

if __name__ == '__main__':
    run()
```

## Dictionary comprehensions

Al igual que los list comprehensions se puede crear diccionarios a partir de una lista o cualquier iterable.

```python
def run():

    my_dict = {i:i**3 for i in range(1, 101) if i % 3 != 0}

    print(my_dict)

if __name__ == '__main__':
    run()
```

La sintaxis es:

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/07e32965-b5aa-478e-bb1d-f54884233e50/Untitled.png)

Ejemplo: crear, con un diccionary comprehension, un diccionario cuyas llaves sean los 1000 primeros números con sus raíces cuadradas como valores

```python
from math import sqrt

def run():
    my_dict = {i:sqrt(i) for i in range(1, 1001) if i % 3 != 0}

    print(my_dict)

if __name__ == '__main__':
    run()
```

### Ejercicios 1.2

A partir de de la definición de la tupla `students`, crear los siguientes diccionarios, donde su nombre sea su clave y los demás valores:

1. Todos los estudiantes
2. Todos los estudiantes con una edad mayor o igual a 18
3. Todos las estudiantes con una edad menor a 18 y sexo ‘M’
4. Todos los estudiantes con un promedio mayor o igual a 6.0

```python
from statistics import mean

def run():
    students = (
        ('Jairo', [4.5, 3.2, 6.1], 21, 'H'),
        ('Yaneth', [5.4, 2.3, 1.6], 19, 'M'),
        ('Carlos', [8.5, 8.2, 8.1], 23, 'H'),
        ('Anabel', [9.5, 9.2, 8.1], 17, 'M'),
        ('Roberto', [7.5, 7.2, 7.1], 16, 'H'),
    )
    solution = {}
    print(solution)     


if __name__ == '__main__':
    run()
```
