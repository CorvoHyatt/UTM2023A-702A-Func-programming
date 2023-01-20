[Programación Funcional](../README.md)> 8. Iteradores

# 8. Iteradores

Una secuencia es una colección ordenada de elementos, las más comunes son listas, cadenas, y tuplas. Pero las secuencias recaen en un par de tipos de bajo nivel que son importantes para la programación funcional: iteradores e iterables.

# Iteradores

En Python, un iterador es una objeto que puede ser usado para iterar sobre una serie de valores, uno después de otro. Específicamente, un iterador puede ser pasado por la función `next` y obtener el siguiente valor de la serie.

En el  siguiente ejemplo se aplica la función `round` a  todos los elementos de una lista con la ayuda de `map()`.

```python
a = [2.2, 5.6, 1.9, 0.1]
b = map(round, a)
```

Si se imprime el valor de `b`, se muestra un objeto de tipo `map` y  no una lista, como se esperaría en primera instancia.

```python
<map object at 0x000002581A529860>
```

Un objeto `map` puede actuar como un iterable (es decir, puede ser pasada por la función `next`). Por lo que puede imprimirse de la siguienre forma:

```python
print(next(b)) # 2
print(next(b)) # 6
print(next(b)) # 2
print(next(b)) # 0
print(next(b)) # throws StopIteration
```

# Iterables

Un iterable es algo que se puede iterar. Por ejemplo, las listas son iterables ( también lo son las cadenas y las tuplas).

Un iterable puede ser pasado a la función `iter`. Esta función retorna un iterador que puede ser usado para iterar. Ejemplo:

```python
a = [1, 3, 7]
b = iter(a)

print(a)
print(b)
```

`a` es una lista, y `b` es un `list_iterator`, un tipo de iterador que es configurado para iterar sobre los valores en `b`. 

```python
print(next(b))  # 1
print(next(b))  # 3
print(next(b))  # 7
```

Es muy similar al ejemplo de map, esto es porque una lista es un iterable en lugar de un iterador, es necesaria un paso extra al llamar `iter` para obtener el iterador. 

# For

Considerar que:

```python
a = [1, 3, 7]
for x in a:
	print(x)
```

El `for` require de una variable ( en este caso  `x`), y algo para recorrer (`a` en este caso). El ciclo `for` operad de la siguiente forma:

- Obtiene un iterador del iterable `a`, utilizando la función `iter`.
- Obtiene valores del iterador, uno por uno. Para cada valor, es asignado el valor a `x` y ejecuta el cuerpo del ciclo.
- Cuando el iterable lanza `StopIteration`, el ciclo termina.

# Iteradores también soportan iter

La descripción previa nos deja con un problema pontencial. La función `map` retorna un iterador, pero se necesita un iterable para usar el ciclo `for`. Por lo que, se puede recorrer un `map`, de la siguiente forma:

```python
a = [1, 3, 7]
for x in map(lambda x: x*x, a):
	print(x)
```

La respuesta es que todos los iteradores también soportan la función `iter`, pero en el caso de un iterador, al llamar a `iter` retorna al objeto en si mismo; Por lo que:

- Si se trata un loop sobre un iterable, Python utiliza la función `iter` para obtener su iterador
- Si se trata un loop sobre un iterador, Python  llamara de nuevo la función `iter`, pero regresará el iterador mismo.

De alguna y otra forma, el loop obtendrá un iterador para trabajar.

# Iteradores vs iterables

Para resumir

- Un iterador es una objeto que puede iterar sobre una secuencia de valores, a través del paso repetido de estos por la función next.
- Un iterable es un objeto sobre el que se pude iterar. Si se pasa un iterable a la función `iter`, esta devolverá un iterador que se puede utilizar para iterar sobre él.

Los iterables pueden crear un nuevo iterador para que puedas recorrer una lista varias veces, pero un iterador sólo puede usarse una vez.

# Iteradores utilizan evaluación perezosa

La unica forma de obtener valores de un iterador es solicitando el siguiente elemento. Esto significa que si se desea el 100th elemento, se tiene que pedir el siguiente elemento 100 veces. No hay otra opción.

Esto significa que un iterador no tiene que crear todos sus valores en un solo paso. De hecho, muchos iteradores calculan sus valores uno por uno cada vez, conform son requeridos. Cada vez que se solicita el siguiente elemento, el iterador lo calcula y asi sucesivamente. A este enfoque se le llama evaluación perezosa (el iterador no hace ningún trabajo hasta que lo tiene que hacer). 

Existen multiples ventajas de este enfoque:

- Cuando se solicita el primer valor, el iterador puede retornarlo directamente. Sin la evaluación perezosa, el iterador necesitaría calcular todos sus valores antes de poder devolver el primer valor. Esto puede hacer que el programa responda mejor si la serie es muy larga.
- No es necesario almacenar los valores calculados. Una serie larga podría utilizar mucha memoria si necesitara almacenarla.
- No se pierde tiempo calculando valores que podrías no utilizar.

Por ejemplo, suponer que se tiene un iterador myiter, que crea 1000 valores y se desea encontrar el primer el primer valor cero. Se pude hacer algo como:

```python
for x in my_iter:
	if x == 0:
		break
```

Sin la evaluación perezosa, `myiter`  calcularía los 1000 valores antes de que el loop comience. Si este retorna en la segunda posición fue el cero, entonces se habrán calculado los 998 valores restantes para nada. Con la evaluación perezosa, `myiter` calcula el primer valor justo antes del pase del primer loop, después el segundo valor antes del segundo pase a través del ciclo.. y después el ciclo es terminado, por loq que los 998 valores restantes nunca serían calculados.

En algunos casos, un iterador podría ser potencialmente infinito. Por ejemplo, si se crea un iterador para gerenerar la serie de números primos, no tienen fin.  Se tendrá que definir algún límite para el número primo más grande que se pueda manejar., y después se tendrá que esperar por un largo tiempo hasta que esos números sean generados.

Con la evaluación perezosa, se pueden crear los números primitivos, uno por uno, conforme son necesitados y continuar más o menos para siempre.

Hay casos donde la generación perezosa no es el mejor enfoque. Un ejemplo seria un iterador que lea bytes de un archivo. Esto generalmente es ineficiente  al acceder un byte a la vez. por lo que el iterador podría decidir leer un bloque grande de datos una sola vez.

# Secuencias

Una secuencia es una colección ordenada de elementos que permiten acceso aleatorio. Por ejemplo, una secuencia incluye una lista, cadanedas y tuplas. 

Ordenados significa que cada elementos en la secuencia tiene un indice, y comienza en el índice `0`.

Acceso aletorio, significa que se puede acceder de manera directa al elemento a través del índice i utilizando la notación de corchetes.

```python
n = a[i]
a[i] = 3
del a[i]
```

Las secuencias inmutables como las tuplas  y las cadenas solo permiten que los elementos sean leídos, no modificados o borrados.

Todas las secuencias son iterables, es decir,  significa que soportan la función `iter` para para obtener un iterador. Esto también significa que funcionaran con ciclos.

Además, las secuencias generalmente tienen un número específico de elementos, y se puede utilizar la función `len` para conocer cuántos elementos hay en una secuencia.

La función `range` crea una secuencia inmutable:

```python
r = range(2, 8)
print(len(r))  # 6
print(r[3])    # 5
```

En este ejemplo, `r` es un objeto range. Es iterable, pero también soporta el uso de `len` y la lectura aleatoria de los elementos. Es importante, no considerar que un `range` es una lista de valores, como una `list`. Este crea los valores de forma perezosa. Los valores de `len(r)` y `r[3]` son calculados a partir de los parámetros del rango.

# Entendiendo un iterador

Algunas veces resulta util convertir un iterador en una secuencia concreta como una lista. Esto es llamada realising el iterador. Existen múltiples razones por loas que se quiera entender un iterador

- Para encontrar su tamaño
- Para acceder a sus elementos más de una vez (un iterador solo pude ser leído una sola vez)
- Para acceder a sus elementos en diferente orden
- Para imprimirlo

El procesode entender un iterador implica evaluar cada término en el iterador y hacer estos términos disponibles como una secuencia. Existen dos formas de hacer esto: utilizando un constructor de una secuencia como `list` o utilizar el operador `*`.

## Uso de constructor de una secuencia

Ejemplo, se crea un iterador con `map` y se quiere imprimir el resultado:

```r
a = [2.2, 5.6, 1.9, 0.1]
b = map(round, a)
print(b) # <map object at 0x000002470E579828>
```

El problema es que b es un iterador, por lo que cuando se imprime solo se ven detalles de objeto iterador, no los valores contenidos.

Una simple manera de realizar esto es utilizar la función list. Esto convertira casi cualquier cosa en una lista.

```r
print(list(b)) # [2, 6, 2, 0]
```

La función `list` aplica un ciclo a través del iterador, evaluando cada elemento, y crea una lista de todos los elemetos.

La función `tuple` realizará un trabajo similar, creando una tupla en lugar de una lista.

```r
print(tuple(b))  # (2, 6, 2, 0)
```

En cadenas las cosas son diferentes. En el siguiente ejemplo se utiliza `map()` y la función chr)= que convierte una lista de número a caracteres basado en su valor ASCII.

```r
a = [72, 101, 108, 108, 111]
b = map(chr, a)
print(str(b)) # <map object at 0x000001D23F1E9828>
```

Las cadenas str funcionan de forma diferente en comparación con una lista. Mientras que la lista toma un objeto e intenta tomar todos sus elementos y crear una lista, str trabaja en un nivel diferente. Esta intenta encontrar una representación de el objeto mismo.

Si se pasa un iterador a una `list()`, esta convertirá el iterador a una forma de lista a partir de sus elementos. Pero si se pasa un iterador a `str()`,  describira el iterados, en este caso al objeto mapa. No evaluará el iterador.

La solución es utilizar la función `join()`. Esta toma el iterable de valores de cadena y los une.

```python
print(''.join(b))
```

La función `join()` une a todos los elementos de b un crea una sola cadena. `‘’` Es un literal de cadena vacia que permite que join una la cadena con `‘’`.

## Iteradores de transformación

La programación funcional se prefieren los iterbales sobre las listas, porque existe menos riesgo de efectos secundarios. Frecuentemente se requiere transformar un flujo iterable de alguna forma, en Python se incluye un número de funciones estándar que realizan esto.

# Enumerate

```python
a = ('red', 'green', 'blue')
for i, s in enumerate(a):
	print(i, s)
```

Este es un lenguaje común que es utilizado si se requiere acceder al contador del ciclo con el ciclo. En este caso, el ciclo opera tres veces, con i = 0, después con 1, después con 2. El código imprime tres líneas.

```python
0 red
1 green
2 blue
```

Para comprender como funciona, se implementa `enumerate` de una manera más convencional

```python
a = ('red', 'green', 'blue')
for t in enumerate(a):
	print(t)
```

Salida:

```python
(0, 'red')
(1, 'green')
(2, 'blue')
```

Lo que hace enumerate es retornar una serie de tuplas. En la versión original del ciciclo, simplemente se desempaca esta tupla a `i, s` por lo que `i` toma los valores de `0`, `1,` y `2`; y `s` toma los valores de `red`, `green` y `blue`.

Esta es una transformación muy util. En `numerate` es opcional colocar el valor inicial, si no se quiere iniciar desde cero.

```python
a = ('red', 'green', 'blue')
for i, s in enumerate(a, 15):
	print(i, s)
```

Salida

```python
15 red
16 green
17 blue
```

# Zip

`zip` permite aplicar un ciclo sobre más de una secuencia en el mismo ciclo:

```python
first = ('John', 'Anne', 'Mary', 'Peter') 
last = ('Brown', 'Smith', 'Jones', 'Cooper') 
age = (25, 33, 41, 28)
for f, l, a in zip(first, last, age):
	print(f, l, a)
```

Salida

```python
John Brown 25
Anne Smith 33
Mary Jones 41
Peter Cooper 28
```

En la primera pasada a través del ciclo, `f`, `l` y `a` son asignados al primer elemento `first`, `last`, y `age` respectivamente. En la segunda pasada `f`, `l` y `a` son asignados al segundo elemento de `first`, `last` y `age`, y así sucesivamente. Se puede suponer, que `zip` produce tuplas que son empacadas en `f`, `l` y `a`.

## Como `zip` transforma iterables.

zip acepta conjunto de iterables, y los transforma en un iterador de tuplas:

```python
a = (10, 11, 12, 13) 
b = (20, 21, 22, 23) 
c = (30, 31, 32, 33)

z = zip(a, b, c)
print(list(z))
```

Si se convierte el iterador `z` a una lista, se verá de la siguiente forma:

```python
[(10, 20, 30), (11, 21, 31), (12, 22, 32), (13, 23, 33)]
```

Este es reorganizado de manera que cada tupla de salida contiene el n-ésimo elemento de cada interable de entrada. Exactemente como se vio en el ejemplo de los nombres.

¿Qué sucede cuando se utiliza un ciclo sobre el flujo de zip? Por ejemplo:

```python
for t in zip(a, b, c):
	print(t)
```

Se imprimira cad tupla en turno:

```python
(10, 20, 30)
(11, 21, 31)
(12, 22, 32)
(13, 23, 33)
```

Y, por supuesto, si se desempaca la tupla en el ciclo:

```python
for x, y, x in zip(a, b, c):
	print(x, y, z)
```

Se estarán procesando las tres listas originales, `a`, `b` y `c` al mismo tiempo. Justo como en el ejemplo de los nombres.

## Flujo con diferentes tamaños

Si accidentalmente, los flujos originales tiene diferente tamaño, zip terminara con el flujo más pequeño:

```python
a = (10, 11, 12)
b = (20, 21)
c = (30, 31, 32, 33)

z = zip(a, b, c)
print(list(z))
```

Esto imprimirá lo siguiente:

```python
[(10, 20, 30), (11, 21, 31)]
```

## `zip` en auto-reversa

Para realizar lo contrario a zip, este mismo permite au auto-reversa.  Considerando la salida del ejemplo anterior:

```python
[(10, 20, 30), (11, 21, 31), (12, 22, 32), (13, 23, 33)]
```

El primer elemento de cada tupla da `(10, 11, 12, 13)` el cual es exactamente la misma tupla original, el problema es que la salida de la función zip, es un iterador que provee un conjunto de tuplas. Pero no podemos solo pasar el iterador de nuevo a través de zip, ya que espera que las tuplas que se pasen esten separadas como argumentos diferentes.

Afortunamente, podemos utilizar el operador `*` que conveierte el iterador a una lista de argumentos. `*z` es equivalente a convertir `z` a una lista y entonces pasar a `z[0]`, `z[1]`, `z[2]`, `z[3]`:

```python
a = (10, 11, 12, 13) 
b = (20, 21, 22, 23) 
c = (30, 31, 32, 33)

z = zip(a, b, c)

restored = zip(*z)
print(list(restored)) 
```

Esto nos devuelve nuestros datos originales:

```python
[(10, 11, 12, 13), (20, 21, 22, 23), (30, 31, 32, 33)]
```

# `filter`

La función `filter` puede ser utilizada para eliminar elementos de un iterable, basado en una función de prueba. Este retorna un iterador que accesa al resultado. Aquí el ejemplo:

```python
a = [3, 2, 1, 6, 7, 0]
f = filter(lambda x: x > 2, a)
```

Este código utiliza una lambda como función de prueba. En esta caso, la función retorna true si el valor de `x` es mayor que `2`. Esta prueba es aplicada a cada elemento del iterable `a`. Solamente aquellos elementos que pasan a prueba son incluidos en el iterable de salida. Si se imprime `list(f)`, son tendremos dos elementos que son menores a `2`:

```python
[3, 6, 7]
```

Se puede utilizar `filter` en un ciclo `for`, este loop utiliza `filter` para imprimir solo aquellas cadenas no vacías:

```python
strings = ('red', '', 'green', '', 'blue') 
for s in filter(len, strings):
	print(s)
```

La lista de cadenas contiene tanto cadenas vacías como no vacías, se utiliza `filter` para aplicar la función `len`. Para aquellos string que esta vacíos, len retorna `0`. Python trata al `0` como `False`, por lo que esas cadenas serán filtradas. 

```python
red
green
blue
```

# `map`

La función `map` aplica la una función proporcionada, a un conjunto de argumentos. Esta retorna un iterador para acceder a los resultados.

## `map` con un parámetro

Ejemplo

```python
def square(x):
	return x*x

a = [2, 5, 6]
m = map(square, a)
```

La función map aplica square a cada valor en a, retornado los valores al cuadrado a través de un iterador. Si convertimos m a una lista y se imprime, se obtiene:

```python
[4, 25, 36]
```

## Evaluación perezosa

Todas las funciones descritas anteriormente utilizan la evaluación perezosa. Esto se ilustra agregando alguna sentencia extra print al ejemplo anterior:

```python
def square(x):
	print('Evaluating square', x)
	return x*x

a = [2, 5, 6]
print('Calling map')
m = map(square, a)
print('Called map')
    
print('Entering loop')
for x in m:
	print('Start of loop body')
	print(x)
```

El código imprime:

```python
Calling map
Called map
Entering loop
Evaluating square 2
Start of loop body
4
Evaluating square 5
Start of loop body
26
Evaluating square 6
Start of loop body
36
```

## `map` con más de un parámetro

Se puede utilizar map con funciones que utilizan más de un parámetro. Se debe aplicar map con parámetros iterables extra, uno para cada argumento que la función de aplicación toma.

Por ejemplo, en el código previo, la función square solo toma un argumento, map requiere dos argumentos (la función y un iterable pupliendo una serie de valores para el argumento de la función).

En el siguiente ejemplo, add toma dos argumentos, por lo que map requiere tres argumentos (la función, y dos iterables supliendo una serie de valores para el primer y segundo argumento).

```python
import operator

a = [20, 30, 40]
b = range(3)

m = map(operator.sub, a, b)
```

Esta ocasión utilizamos la función `operator.sub`. Esta función toma dos argumentos `x, y` y retorna `x-y`. Es necesario importar el módulo `operator` para utilizar `sub`.

Se requieren dos iterables debido a que `operator.sub` toma dos argumentos, `a` es una lista, `b` es un `range(3)`, el cual provee `0, 1, 2`. Por lo que `map` calcula:

```python
sub(20, 0)
sub(30, 1)
sub(40, 2)
```

El resultado, si se imprime `list(m)` es:

```python
[20, 29, 38]
```

# `reversed`

`reversed` es una función util que retorna un iterador que invierte el orden de los elementos de la secuencia original. Por ejemplo:

```python
a = [2, 4, 6, 8]
r = reversed(a)
print(list(r))
```

Aquí r es un iterador que accede a los elementos de `a` en un orden inverso. Cuando se crea una lista de `r`, esta contiene:

```python
[8, 6, 4, 2]
```

Nótese que reverse no trabaja con todo tipo de iterables. Este solo trabaja sobre secuencias (list, tuples, strings, etc.) No se puede hacer lo siguiente:

```python
a = [2, 5, 6]
m = map(square, a)
r = reversed(m)
```

Esto es porque `m` no es una secuencia. Se puede arreglar este problema al convertir `m` a una lista o tupla antes de pasarla a `reversed`:

```python
a = [2, 5, 6]
    m = map(square, a)
    r = reversed(list(m))
```

Para más detalles de como ordenar objetos que no soportan reversed, se puede crear un objeto reversible.

## `reversed` sobre un rango

Se puede utilizar `reversed` con `range`, resulta muy útil para conteos regresivos. Por ejemplo, para contar de 9 a 0 se puede utilizar este `range`:

```python
for i in range(9, -1, -1):
	print(i)
```

Este código puede resultar poco intuitivo. De forma alterna, se pude utilizar:

```python
for i in reversed(range(10)):
	print(i)
```

## `reverse`

las listas tienen un método reverse que no hace los mismo que reversed, pero opera sobre una lista.

```python
k = [1, 3, 7]
k.reverse()
print(k)    # [7, 3, 1]
```

Este método no retorna nada, solo invierte la lista. 

# `sorted`

sorted no es como las otras funciones de transformación. Funciona sobre cualquier iterable pero no produce un iterador como salida, en su lugar crea una lista. 

Comparación entre `sorted` y `reversed:`

- `reversed` require una secuencia como entrada pero crea un iterador perezoso como salida. Esto es porque, lo primero que se requiere al invertir los elementos, es el último elemento. No se pude invertir una serie a menos que se tenga un acceso aleatorio a los elementos, por lo que una secuencia es requerida como entrada.
- sorted puede aceptar iteradores perezosos como entrada pero crea una lista como salida, Python utiliza un algoritmo de ordenamiento llamado Timsort, que es un híbrido entre el ordenamiento merge y el ordenamiento sort. El algoritmo acepta los datos elemento por elemento pero requiere acceso aleatorio a la lista de salida para colocar los elementos en la posición final correcta.

## Ordenamiento por mes y año

```python
dates = ['2019/04/06',
             '2017/04/15',
             '2019/03/21',
             '2018/04/10',
             '2019/04/08',
             '2017/03/20',
             '2018/06/30',
             '2019/09/30',
             '2018/04/11',
             '2017/03/14']
sorted_dates = sorted(dates)
```

Salida es:

```python
		2017/03/14
    2017/03/20
    2017/04/15
    2018/04/10
    2018/04/11
    2018/06/30
    2019/03/21
    2019/04/06
    2019/04/08
    2019/09/30
```

Si  se ordena através del mes:

```python
sorted_by_month = sorted(sorted_dates, key=lambda x: x[5:7])
```

```python
		2017/03/20
    2017/03/14
    2019/03/21
    2017/04/15
    2018/04/10
    2018/04/11
    2019/04/06
    2019/04/08
    2018/06/30
    2019/09/30
```

La función sort es estable. Esto significa que cuando se ordena por mes, todas las entradas que tiene el mismo mes mantienen su posición original, relativo a la otra. Por lo que se verá que primero se agrupan las fechas por mes, pero en cada grupo del mismo mes los elementos son ordenados por año.

Esto produce una lista que es primero ordenada por mes, y después ordenada por fecha por cada grupo, primero se debe ordenar por date y después por mes.

## Algunas funciones `key` útiles.

Se tiene la siguiente lista:

```python
people = [('John', 'Brown', 25), ('Anne', 'Smith', 33), ('Mary', 'Jones', 41),
              ('Peter', 'Cooper', 28)]
```

Se pueden ordenar pos su segundo nombre:

```python
sorted_by_surname = sorted(people, key=lambda x: x[1])
```

Para comprender el código es necesario analizar la función lambda (obtiene el segundo elemento de la tupla).

El modulo operator tiene una función: `itemgetter`, para ayudar en esta situación. La función `itemgetter` reemplaza el indexado de una lista (el operador `[]`).

```python
from operator import itemgetter
sorted_by_surname = sorted(people, key=itemgetter(1))
```

`itemgetter(1)` no retorna el segundo elemento. Este retorna una función que toma el segundo elemento de cualquier secuencia que se pase. Actúa como un closure:

```python
f = itemgetter(1)
t = ('Anne', 'Smith', 33) 
s = f(t) # 'Smith'
```

Otro operador de función útil es `methodcaller`. Este retorna una función que llama a un método en particular en cualquier objeto que se le pase.

```python
fruits = ['Banana', 'apple', 'Apricot', 'Clementine', 'avocado']
sorted_names = sorted(fruits)
```

El resultado, puede no ser el deseado dado que las cadenas al ser ordenada son sensibles al uso de mayúsculas. Para solucionar esto se puede utilizar:

```python
sorted_names = sorted(fruits, key=lambda x: x.lower()))
```

Una mejor solución es:

```python
from operator import methodcaller
sorted_names = sorted(fruits, key=methodcaller('lower'))
```

`methodcaller` crea una función. Esta nueva función llama al método `lower` para cualquier objeto que se le pase.

```python
f = methodcaller('lower')
s = f('Banana') # 'banana' equivalent to 'Banana'.lower()
```

## Invirtiendo el orden del ordenamiento

```python
sorted_dates = sorted(dates, reverse=True)
```

## `sort`

Las listas tiene un método sort que hace exactamente lo mismo que sorted, pero opera sobre la lista.

```python
k = [1, 7, 2, 4, 1]
k.sort()
print(k) # [1, 1, 2, 4, 7]
```

Este método no retorna nada, solo ordena a la lista misma.

`sort` tienen el mismo parámetro opcional, `key` y `reverse`, que tienen `sorted`. La función es exactamente la misma.

# Combinación de funciones

Es muy útil combinar funciones, en una sola expresión. 

## `map` y `filter`

```python
import math
k = [1, 4, -2, 16, -3, 36, -1]
f = filter(lambda x: x>=0, k) 
m = map(math.sqrt, f)
print(list(m)) #[1.0, 2.0, 4.0, 6.0]
```

```python
m = map(math.sqrt, filter(lambda x: x>=0, k))
```

## Pipelines

Cuando se encadenan dos o más funciones que utilizan evaluación perezosa, se crea un pipeline. 

Ejemplo de `map` y `filter`.

```python
def same(s):
	print('Same', s)
	return s
```

La función same solo imprime un mensaje y retorna el mismo valor que recibe. 

```python
def not_empty(s):
	if s:
		print('True', s)
		return True
	else:
		print('False')
		return False
```

Esta función retorna True si la cadena no esta vacía. False de otro modo. También imprime que se hizo.

```python
k = ['a', '', 'b', '']
m = map(same, filter(not_empty, k)) 
print('Start')
for s in m:
	print('In loop', s)
```

Salida

```python
		Start
    True a
    Same a
    In loop a
    False
    True b
    Same b
    In loop b
    False
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0a25cc40-d482-4f63-9609-9214f32f5d28/Untitled.png)

La primer iteración del ciclo imprime esto:

```python
		True a
    Same a
    In loop a
```

Primero, un conjunto de peticiones ocurren sobre el pipeline

1. El ciclo solicita un valor del iterador map
2. El iterador map solicita un valor del iterador filter
3. El iterador filter solicita un valor del iterador de la lista

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/edc37fd0-5685-46df-8f09-f365ff1b0674/Untitled.png)

En seguida, las respuestas son mandadas de vuelta en el pipeline. Es cuando la función en realidad es llamada

1. El iterador de la lista pasa el valor `‘a’` a través del iterador `filter`.
2. El iterador `filter` pasa el valor `‘a’` a la función `not_empty`, la cual imprime `‘True a’` porque la cadena es no vacía.
3. El iterador `filter` pasa el valor `‘a’` hacia el iterador `map`.
4. El iterador `map` pasa el valor `‘a’` a la función `same`, la cual imprime `‘same a’`.
5. El iterador `map` pasa el valor `‘a’` al iterador del ciclo.

En este punto, el ciclo imprime ‘in loop a’.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e9fc6042-0946-4bfe-88db-c4adca89fa9e/Untitled.png)

La segunda iteración del ciclo imprime:

```python
		False
    True b
    Same b
    In loop b
```

Este paso es muy similar a la primera iteración, excepto que cuando el iterador de filter solicita un valor del iterador list, toma una cadena vacía (el segundo valor dek). Esto significa que la función `not_empy` imprime `‘false’`  y retorna `False`.

Ahora en el siguiente punto, el paso de `filter` es filtrar los casos cuando `not_empty` retorna `False`. Por lo que, `filter` no  pasa este valor de vuelta al iterador `map`. en su lugar lo evita. Después solicita el siguiente valor del iterador de `list`, el cual es `‘b’` en esta ocasión, este es pasado a través del pipeline como se hizo anteriormente con `‘a’`.

En el último intento del ciclo, `filter` toma el último elemento del iterador `list`, el cual es otra cadena vacía. Esto lo descarta  y el operador del ciclo lanza una excepción `StopIteration`, y el ciclo termina.

## `map` y `zip`

En el siguiente código se utiliza map para dar formato a datos de nombres:

```python
def format_person(first, last, age):
	return '{}, {} - age {}'.format(last, first, age)

first = ('John', 'Anne', 'Mary', 'Peter') 
last = ('Brown', 'Smith', 'Jones', 'Cooper') 
age = (25, 33, 41, 28)

m = map(format_person, first, last, age)

list(map(print, m)) # Prints the result
```

La salida es:

```python
		Brown, John - age 25
    Smith, Anne - age 33
    Jones, Mary - age 41
    Cooper, Peter - age 28
```

Suponer:

```python
people = [('John', 'Brown', 25), ('Anne', 'Smith', 33), ('Mary', 'Jones', 41),
              ('Peter', 'Cooper', 28)]
```

Para utilizar `map`, primero es necesario desempaquetarlos. Se pude utilizar `zip` para desempaquetar los datos:

```python
m = map(format_person, *zip(*people))
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/535dc9b3-9ca8-4c32-b910-77d6e5829469/Untitled.png)

## Iterables de reducción

Un función de reducción toma todos los valores de un iterable y los reduce a un solo valor. Por ejemplo, `sum` suma todos los valores de un iterable y retorna el valor total.

# `len`

len retorna el tamaño del item (el número de elementos si es una lista o una tupla, el número de caracteres si es una cadena.

```python
len ([1, 2, 30]) #3
len('uvwxyz') # 6
```

`len` no funciona con iterables perezosos  (como la salida de `map` o `filter`). Se puede convertir un iterable perezoso a una lista y aplicar `len` al resultado. Otra alternativa es utilizar uno de los métodos para map (ver más adelante).

# `sum`

`sum` acepta un iterable y retorna la suma (el resultado de combinar todos los elementos utilizando el operador `+`. Por ejemplo:

```python
a = [2, 5, 7, 1]
print(sum(a))  # 15
```

Se puede dar un valor inicial a sum. Este será agregado al total:

```python
a = [2, 5, 7, 1]
print(sum(a, -3))  # 12
```

`sum` también funciona con secuencias como las listas. Sin embargo, el código siguiente no funciona:

```python
a = [[2, 4], [0, 0], [5, 3]]
print(sum(a)) # ERROR
```

El problema es que `sum` tiene un valor inicial por defecto igual a 0, por lo que el código anterior intenta calcular:

```python
0 + [2, 4] + [0, 0] + [5, 3]
```

Esto es incorrecto porque no se puede agregar una lista a un entero. La solución es sumar una lista vacía como valor inicial, por lo que suma realizará la siguiente operación:

```python
[0] + [2, 4] + [0, 0] + [5, 3]
```

Esto es ahora un código valido:

```python
a = [[2, 4], [0, 0], [5, 3]]
print(sum(a, [])) # [2, 4, 0, 0, 5, 3]
```

Una alternativa de unir iterables es con `itertools.chain`.

La función `sum` no funciona con cadenas. Python deliberadamente previene esto porque es terriblemente ineficiente sumar un conjunto de cadenas utilizando `add`. Es mejor utilizar `join` para concatenar cadenas:

```python
a = ['abc', 'pqr', 'xyz']
s = ''.join(a)
```

# `min`

min acepta un iterable y retorna el valor mínimo del iterable. Por ejemplo:

```python
a = [2, 5, 7, 1]
print(min(a))  # 1
```

El iterable puede contener elementos de cualquier tipo, y pueden ser comparados con los otros. Por ejemplo, puede contener cadenas, las cuales serán comparadas de la forma estándar. Ejemplo:

```python
a = [[1, 2, 3], [1, 1, 5], [6, 7, 8], [1, 1, 5]] 
print(min(a)) # [1, 1, 5]
```

 Las listas comparan elemento por elemento, por lo que `[1, 1, 5]` es menor que `[1, 2, 3]`. Se puede notar que hay dos listas con valor `[1, 1, 5]`. Estos son diferentes objetos que tiene los mismos valores. `min` siempre retornará el primer objeto es este tipo de casos.

## Argumento por default

Si se llama a `min` en un iterable vacío, se obtiene una excepción `ValueError`. Se pude evitar esto utilizando el argumento por defecto. Esto es una palabra reservada que se utiliza de la siguiente forma:

```python
a = []
print(min(a, default=0)) # 0
```

Dado que la lista esta vacía, `min` retorna el valor por default 0. Este valor solamente es utilizado cuando el iterador esta vacío, por ejemplo:

```python
a = [2, 5, 7, 1]
print(min(a, default=0))  # 1
```

A pesar de que el valor por defecto es menor que 1, `min` retorna 1 ya que es el valor más pequeño de la lista.

## Argumento key

`min` tiene un argumento opcional key que puede ser utilizado para modificar el orden de comparación. Es un argumento de palabra reservada y funciona de la misma forma que en la función `sorted`.

`min` tiene un argumento opcional key que puede ser utilizado para modificar el orden de comparación. Es un argumento de palabra reservada y funciona de la misma forma que en la función `sorted`. Ejemplo, que utiliza una función lambda que retorna el tercer elemento de la lista:

```python
 a = [[1, 2, 3], [1, 1, 5], [6, 7, 8], [1, 1, 5]] 
print(min(a, key=lambda x: x[2])) # [1, 2, 3]<
```

Dado que se esta comparando el tercer elemento `x[2]`, la lista `[1, 2, 3]` es la más pequeña.

# `max`

`max` funciona de forma muy similar a `min`, excepto que retorna el valor máximo de un iterable.

# `any`

`any` acepta cualquier iterable. Retorna un valor `True` si alguno de los elementos tiene un valor `True`. Retorna `False` si ninguno de los elementos tiene un valor `True` o si el iterable esta vacío:

```python
print(any([1, 0, 2]))      #1
print(any(['a', '', 'z'])) #2
print(any([0, '', False])) #3
print(any([]))             #4
```

1. `True` porque el valor `1` y `2` cuentan como `True`.
2. `True` porque `‘a’` y `‘z’` cuentan como `True`.
3. `False` porque `0`, `‘’`, `False` cuentan como `False`.
4. `False` porque el iterable `[]` esta vacío.

# `all`

`all` acepa un iterable. Retorna `True` si todos los elementos tienen un valor `True`. Retornará `False` si alguno de los elementos tienen un valor falso. A diferencia de `any`, `all` retornará `True` si el iterable esta vacío.

```python
print(all([1, 0, 2]))      #1
print(all(['a', '', 'z'])) #2
print(all([1, 'a', True])) #3
print(all([]))             #4
```

1. `False` porque el valor `0` cuentan como `False`.
2. `False` porque `‘’` cuentan como `False`.
3. `True` porque `1`, `a` y `True` cuentan como `True`.
4. `True` porque el iterable `[]` esta vacío.

# `reduce functools`

Si las funciones reduce anteriores no cumplen con tus necesidades, se puede crear una propia utilizando la función `reduce`. 

Esta función permite definir un comportamiento. Por ejemplo, suponer que se quiere reducir una lista mediante la multiplicación de los elementos. Se puede realizar lo siguiente:

```python
import functools, operator
a = [2, 3, 5, 2] 
print(functools.reduce(operator.mul, a)) # 60
```

El `operator.mul` es una función equivalente al operador `*`. Esto sería igual a:

```python
(((2 * 3) * 5) * 2)
```

`reduce` acepta una función y un iterable. La función que se proporciona debe tomar dos parámetros. `reduce` funciona de la siguiente manera:

1. Toma el primer y el segundo valor del iterable y los combina utilizando la función.
2. Tomo el siguiente valor del iterable. Combina el resultado previo con el nuevo valor utilizando la función.
3. Repite el paso dos para todos los elementos.

## Valor inicial

reduce acepta un tercer argumento opcional, initializer. Este provee un valor inicial cuando la primera reducción comienza:

```python
a = [2, 3, 5, 2]
print(functools.reduce(lambda x, y: x*y, a, 10)) # 600
```

En este caso se tiene un inicialización de 10, por lo tanto el cálculo es:

```python
((((10 *2) * 3) * 5) * 2)
```

dando `600`. Al agregar un initializer es similar a agregar un valor extra al inicio del iterador de entrada.

## Casos especiales

Sin inicializador:

- Si el iterable esta vacío, `reduce` lanzará un `TypeError`.
- Si el iterable solamente tiene un elemento, `reduce` retornará ese elemento.

Con `initializer`:

- Si el iterable esta vacío, `reduce` retornará el valor del `initializer`.
- Si el iterable solo tiene un elemento, `reduce` retornará el valor del `initializer`.

# El patrón `map`-`reduce`

El patrón `map`-`reduce` es una forma de procesar una conjunto de datos grande en una forma que puede ser distribuido entre muchas computadoras.

La idea básica es iniciar por el procesamiento de elementos de datos individualmente, y finalmente combinarlos para dar el resultado requerido.

Para dar un simple ejemplo, suponer que se desea calcular la longitud media de las palabra de un bloque de texto:

```python
The joy of coding Python should be in seeing short, concise, readable classes that express a lot of action in a small amount of clear code -- not in reams of trivial code that bores the reader to death.
```

Se pude separa esta tarea en dos pasos:

- Contar el número de letras en cada palabra.
- Sumar el total de número de letras en todas las palabras.

Al dividir la suma por el número de palabras dará el resultado deseado, la longitud media las palabras. Aquí una lista de las palabras, sin puntuación:

```python
strings = ['the', 'joy', 'of', 'coding', 'Python', 'should', 'be', 'in', 'seeing', 'short', 'concise',
'readable', 'classes', 'that', 'express', 'a', 'lot', 'of', 'action', 'in', 'a', 'small', 'amount', 'of', 'clear', 'code', 'not', 'in', 'reams', 'of', 'trivial', 'code', 'that', 'bores', 'the', 'reader', 'to', 'death']
```

Contar el número de letras en cada palabra es fácil, se mapea la función `len` sobre la listas de cadenas:

```python
lengths = map(len, strings)
```

lengths es ahora un iterador que tiene un flujo de las palabras individuales. Se pude imprimir utilizando:

```python
print(list(lengths))
```

Sin olvidar convertir el iterador a una lista se pueden imprimir sus valores.

```python
[3, 3, 2, 6, 6, 6, 2, 2, 6, 5, 7, 8, 7, 4, 7, 1, 3, 2, 6, 2, 1, 5, 6, 2, 5, 4, 3, 2, 5, 2, 7, 4, 4, 5, 3, 6, 2, 5]
```

Ahora se necesita calcular la longitud media de cada palabra (esto es simplemente la suma de lo largo de todas las palabras, dividido por el número de palabras):

```python
average = sum(lengths)/len(strings)
```

Por lo tanto, se puede calcular la longitud media de la palabra de una lista de cadenas utilizando dos sencillas y obvias líneas de código:

```python
lengths = map(len, strings)
average = sum(lengths)/len(strings)
```

Si realmente se quiere, se puede incluso tomar esto a una sola línea. Que tan legible sea depende de que tan familiarizado se este con la lectura de código funcional, pero el siguiente no es probablemente complejo en exceso:

```python
average = sum(map(len, strings))/len(strings)
```

## Ignorar palabras cortas

Como ejemplo de esto, si se intenta lo mismo que el ejemplo anterior, pero el lugar de tomar la longitud media de todas las palabras, se excluyen `‘a’` y `‘the’`. Se pude realizar esto filtrando `strings` de la siguiente forma:

```python
filter(lambda x : x not in ('a', 'the'), strings)
```

Este código retorna un iterable de todas las cadenas en `strings` que no son `‘a’` o `‘the’` . Se puede calcular el promedio de la lista de forma similar al ejercicio anterior utilizando `filter`.

```python
s = filter(lambda x : x not in ('a', 'the'), strings) 
average = sum(map(len, s))/len(s) # ERROR
```

Pero aquí hay un problema. No se pude obtener el `len` de `s` porque `s` es un iterador. Los iteradores no soportan la función len. Una forma fácil de arreglarlo, es a través de algo que no es parte del paradigma de programación funcional, es convertir el filtrado de palabras en una lista. 

```python
s = list(filter(lambda x : x not in ('a', 'the'), strings)) 
average = sum(map(len, s))/len(s)
```

## Una solución mas de Programación Funcional

La solución anterior tiene un ligero problema, ya que es necesario guardar la lista entera de valores en memoria antes de calcular el promedio. Esto, usualmente no es un problema, de hecho si no se tomará un enfoque de programación funcional, probablemente no se le daría una segunda revisión.

Suponer que se desea encontrar la longitud media de palabra de todas las páginas de Wikipedia. Al momento de escribir, un computadora típica podría fallar en mantener todo el contenido en memoria en un solo momento.

Cómo se podría modificar el código  para trabajar con cualquier número de palabras, con memoria limitada.

La solución más obvia sería contar el número de palabras sumandolas. Se podría crear una función de reducción propia:

```python
def sumcount(it):
	sum = 0;
	count = 0;
	for x in it:
		sum += x
		count += 1
	return sum, count
```

Esta función se comporta de forma similar a la función estándar sum, pero también cuenta el número de elementos. Al final retorna una tupla de la suma de todos los elementos y el número de elementos. Se puede utilizar esta para calcular la media de la siguiente forma:

```python
s = filter(lambda x : x not in ('a', 'the'), strings) 
total, count = sumcount(map(len, s))
average = total/count
```

Esta solución calcula la media sin tener que almacenar una copia de todas las palabras. Si realmente se necesitara procesar todas las palabras de Wikipedia, por supuesto, no se podría utilizar la lista de cadenas para almacenar todas las palabras. Se podría crear algún tipo de iterador que traiga todas la palabras de la web, una a la vez.

Esta es una solución razonable, el código principal es puramente funcional. la función sumcount utiliza un ciclo, el cual no es ideal, pero esta bastante escondido.

## Utilizando `enumerate` y `reduce`

Se puede mejorar las cosas aun más, revisando ese molesto ciclo. Lo que se necesita hacer es sumar los valores y contarlos al mismo tiempo. Quizé la función `enumerate` pueda ayudar. Se puede enumerar la salida del `map`:

```python
s = filter(lambda x : x not in ('a', 'the'), strings) 
m = map(len, s)
e = enumerate(m, 1)
```

El segundo parámetro en la función enumerate es el valor de inicio. Se comienza la cuenta a partir del 1 en lugar del cero. El iterador `e` da los siguientes valores:

```python
(1, 3), (2, 2), (3, 6), (4, 6), (5, 6)...
```

El primer elemento de cada tupla es el contador de palabras. El segundo elemento es el largo de la palabra actual. Lo que se necesita hacer es reducir esta secuencia de una manera que el contador de la palabra se mantenga (se puede mantener la versión más reciente) pero la longitud es sumada.

Se pude utilizar `functools.reduce` para hacer esto. Aquí se implementa `reduce` para simular la función `sum`:

```python
functools.reduce(operator.add, m) # same as sum(m)
```

Pero se acumula una serie de tuplas, se necesita una alternativa a la función add. Cómo la siguiente:

```python
def opsumcount(a, b):
	return(b[0], a[1] + b[1])
```

esta función acepta dos tuplas, `a` y `b`. Esta retorna un tupla. El primer elemento de la tupla retornada, si la más reciente  contador de palabra `b[0]`. El segundo elemento es la suma acumuladade las longitudes de palabras `a[1] + b[1]`. La solución completa, sin ciclo o almacenando en una lista:

```python
import functools

def opsumcount(a, b):
	return(b[0], a[1] + b[1])

s = filter(lambda x : x not in ('a', 'the'), strings)
m = map(len, s)
length, total = functools.reduce(opsumcount, enumerate(m, 1)) 
average = total/length
print(average)
```
