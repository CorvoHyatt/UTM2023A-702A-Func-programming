[Programación Funcional](../README.md)> 9. Generadores

# 9. Generadores

En el capítulo de iteradores se ha visto como crear iteradores, por definición de una clase con a especificación de un par de métodos. Este método funciona bien, pero involucra a código que específica la lógica del iterador.

Los generadores proveen un método simple para la implementación de muchos tipos de iteradores, utilizando una sintaxis simple y frecuentemente un flujo más intuitivo.

# Iterador alphabet

En un ejemplo del capítulo de iteradores se desarrollo un iterador donde este retorna las letras del alfabeto, una por una, y después se detiene. De hecho, solo se retorno desde la letra `a` a la letra `e`. Aquí esta el equivalente mediante un generador.

```python
def alphabet():
	for c in 'abcde':
		yield c
    
for x in alphabet():
	print(x)
```

`alphabet` luce mas como una función normal, pero en realidad es un generador. La diferencia es que tiene un `yield` en lugar de un `return`.

Sin el uso de un ciclo, `alphabet` es utilizado de forma similar a `range`. Si se utiliza `range(5)` se cicla a través de los valores del 0 al 4. `alphabet` hace algo similar, pero cicla entre los caracteres de la `a` a `e`.

Este generador es solo para ilustración. El ciclo funciona perfectamente bien si solo se utiliza la cadena ‘abce’ en lugar de la llamada a `alphabet`.

# Como funciona un generador

Para entender como funciona un generador, sustituiremos el loop por los siguiente:

```python
def alphabet():
	for c in 'abcde':
		yield c
    
g = alphabet()
    
x = next(g)
print(x)
    
x = next(g)
print(x)
```

Primero, se llama a alphabet. Como una función regular, un generador retorna un `generator object` que es almacenado en `g`. La clave en este punto es que `alphabet` contiene un sentencia `yield` en lugar de un `return`. Esa es la situación que lo diferencia de una función normal. Python sabe como crear un generador en su lugar.

El objeto `generator` actúa como un iterador. Cuando se llama a `next` sobre el objeto. este responde con el primer valor en la secuencia `‘a’`. Si se llama a `next` nuevamente este responde con el siguiente valor `‘b’`. y así sucesivamente.

¿Qué es lo que realmente sucede? El primer punto a entender es que el código en el cuerpo del generador no es ejecutado cuando se llama a `alphabet().` En el estilo de un iterador, un generador utilizar la evaluación perezosa. No hace nada hasta que se le solicita un valor.

La primera ocasión que es llamado `next`, Python inicia la ejecución del código en `alphabet`. Este comienza el ciclo `for`, entrando al ciclo por primera vez con el valor inicial de `c` igual a `‘a’.` Después se encuentra con la sentencia `yield`.

Esto ocasiona que Python detenga la ejecución del código de `alphabet` y retorne el valor de `c` al código de la llamada principal. La cuestión critica de `yield`, es que almacena el estado actual del código de `alphabet` antes de salir.

Ahora el código principal ejecuta `print(x)` para mostrar en pantalla el valor `‘a’`. Este entonces llamará a `next` de nuevo. Pero esta ocasión, en lugar de comenzar en el inicio del código de `alphabet`, este pasa al punto previo de la sentencia `yield`. Es estado de restaurado al momento exacto de cuando la sentencia `yield` fue ejecutada.

`alphabet` se cicla nuevamente en la próxima iteración del ciclo `for`. Esta ocasión toma el segundo carácter de la cadena,`‘b’`. Este es retornado con la sentencia `yield`.

Esto continua ocurriendo cada vez que el ciclo principal llama a `next`. Eventualmente el ciclo en el código de `alphabet` es agotado. En lugar de llamar al método `yield`, el código de `alphabet` alcanza el final. El objeto `generator` lanza un error de tipo `StopIteration` en ese punto , para notificar al código de llamada que la iteración se ha completado.

Como se puede apreciar, la ejecución pasa de atrás a delante entre las llamadas del código y el código de `alphabet`. En algunas ocasiones los generadores son llamados co-rutinas por esta razón. Esto contrasta con una función normal, la cual en ocasiones es llamada subrutina. En una subrutina, el código llamado pasa el control completo a las subrutina hasta que este termina, con una co-rutina, el control pasa de un lado al otro y regresa.

No confundir con multihilos, en multihilos, dos conjuntos diferentes de código se  ejecutan al mismo tiempo (incluso en diferentes núcleos o por tiempo compartido sobre un núcleo). Con las co-rutinas solo hay un hilo de ejecución que se intercambia entre dos fuentes de código en una forma predecible.

# Ejemplo, fibonacci iterator

```python
def fibonacci(): 
	c=0
	n=1
	while True:
		yield c
		c, n = n, c + n
    
for i in fibonacci():
	print(i)
	if i > 100:
		break
```

# Iteradores encadenados

Se puede encadenar dos iteradores, se puede obtener un iterador que retorne todos los valores de un iterador seguido de todos los valores de otro iterador.

Primero, veamos el generador identidad. Esto provee una forma de iterar sobre un iterador existente. No muy util por si mismo (se pude iterar sobre el iterador original directamente) pero es un paso en el camino.

```python
def identity(it):
	for x in it:
		yield x
    
for i in identity(range(4)):
	print(i)
```

Lo que hace `identity` es iterar sobre este, produciendo cada valor. Dado que `range(4)` crea la serie 0, 1, 2, 3, el generador identidad crea exactamente la misma serie.

Al encadenar dos iteradores simplemente involucra mejorar la operación identidad sobre el primer iterador, entonces haciendo esto mismo con el segundo iterador. Esto es realmente fácil en un generador:

```python
def chain2(it1, it2):
	for x in it1:
		yield x
	for x in it2:
		yield x

for i in chain2(range(4), reversed(range(3))): 
	print(i)
```

Se encadena `range(4)` - 0, 1, 2, 3 - y el reverso de `range(3)` - 2, 1, 0. Esto crea un único iterador que produce la serie 0, 1, 2, 3, 2, 1, 0.

Este código sería un poco más complicado utilizando un objeto iterable, pero es mucho más simple y obvio utilizando generadores.

# Generator comprehensions

Un generator comprehension es similar a un list comprehension. La diferencia radica en que el generator comprehension utiliza evaluación perezosa., lo cual utiliza menos memoria, y permite iteradores infinitos para ser procesados.

Convertir un list comprehension en un generator comprehension es muy simple, al reemplazar los corchetes por paréntesis. Por ejemplo, este código crea una lista de cadenas `‘0’`, `‘1’`, `‘2’`, etc:

```python
a = [str(i) for i in range(100)]
```

Si solo se necesita un iterador y no una lista, se pude hacer lo siguiente:

```python
g = (str(i) for i in range(100))
```

`g` es una objeto de tipo generador que libera una serie de valores ‘0’, ‘1’, ‘2’. etc. A diferencia del list comprehension, estos 100 valores no son creados en memoria, lo cual resulta importante si se esta utilizando una serie muy larga.

## Variantes de `map`

Una ventaja de los generators comprehension es que pueden ser utilizados para reemplazar funciones como `map`, muy util si se requiere una ligera variante. Ejemplo:

```python
# con map
map(fn, it)
# con generatos comprehension
(fn(x) for x in it)
```

En esta instancia, map es probablemente la mejor opción. Pero si se desea mapear f(x) + 1, resultaría en algo como estp:

```python
# map
map(lambda x: fn(x)+1, it)
# generator comprehension    
(fn(x)+1 for x in it)
```

Regularmente es un asunto de gusto persona, y cualquier que se utilice es mejor que utilizar un enfoque imperativo.

# Variaciones `filter`-`map`

Es posible reemplazar un `filter`, o combinación de `filter`-`map` con un comprehension:

```python
# amp
map(fn filter(cmp, it))
# generator comprehension    
(fn(x) for x in it if cmp(x))
```

Una vez mas, si la función o comparación es un poco más compleja, el comprehension tiene la ventaja de que se puede utilizar una expresión normal en lugar de utilizar una función lambda.

También es posible, realizar operaciones de filtrado especial, por ejemplo, este filtro selecciona cada segundo elemento del iterador de entrada:

```python
(x for i, x in enumerate(it) if i%2==0)
```

Este utiliza enumerate para obtener un contador, `i`, para cada elemento y solamente retorna elementos donde `i` es par (modulo de `i` entre `2` es igual a cero).

En resumen, si se utiliza un list comprehension pero no se necesita la lista actual, considerar el uso de un generador comprehension para ahorrar memoria. Pero si se prefiere el uso de funciones estándar como map p filter en su lugar, que usualmente sera la mejor opción.