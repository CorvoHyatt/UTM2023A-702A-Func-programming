[Programación Funcional](../README.md)> 6. Recursividad

# 6. Recursión

La idea es dado un problema difícil, encontrar un procedimiento que convierta el problema a una versión simple del mismo problema. Aplicar el mismo procedimiento repetidamente hasta hacer el problema más simple, hasta tener un problem tan simple que se resuelva en un paso.

# Factorial

El factorial de un número entero $n$ es el producto de todos los números enteros entre 1 y $n$. Por ejemplo, el factorial de 6, usualmente escrito cómo $6!$ es igual a:

$6 \times 5 \times 4 \times 3 \times 2 \times 1 = 720$ 

Solución recursiva

```python
def factorial(n):
	if n > 1:
		x = n * factorial(n - 1)
	else:
		x = 1 
	return x
    
print(factorial(6))
```

# Limites de la recursividad

La recursividad es relativamente inneficiente en comparación con los bucles. Esto es debido a que en cada paso de la recursión se realiza un llamado a una función, mientras que un bucle solo requiere un salto a un lugar diferente en el código.

La llamada a una función involucra mucho más trabajo que un simple salto, y en cualquier sistema tomará mas tiempo y uso de memoria extra (la memoria es requerida para almacenar el estado actual del a función - los valores de sus variables locales- en cada ocasión que se llama a la función así misma de manera recursiva).

En Python, la recursividad esta limitada a 1000 llamadas. El código anterior no podría calcular el factorial de un número mayor a 1000.

Esto no significa que la recursividad no sea util en Python. Si se esta procesando un árbol binario, por ejemplo, una profundidad de 1000 permite procesar un árbol que contenga al rededor de $2^{1000}$ elementos, lo cual es un número considerable. Pero si el problema se resuelve con un bucle, será probablemente la mejor solución.

# Tail recursión

La forma de recursividad exhibida en factorial es llamada tail recursión. Tail recursión es cuando la llamada recursiva esta justo al final de la función (normalmente con una condición previa para terminar la función antes de hacer la llamada recursiva).

Cuando una función es recursión de cola, generalmente se puede reemplazar con un ciclo. En Python, usualmente se debe hacer esto.

Algunos lenguajes detectan automáticamente la recursión de cola y la sustituyen por una operación de bucle. Esto se llama a menudo TCO(Tail Call Optimisation). Python no lo hace. Suele ocurrir en lenguajes funcionales puros, donde en algunos casos los bucles ni siquiera existen, Estos lenguajes suelen ser mucho más declarativos que Python lo que hace más fácil detectar la recursión de cola. 

## Recursión ineficiente

La serie Fibonacci se define de la siguiente manera:

F(0) = 0

F(1) = 1

F(2) = F(1) + F(2) = 1

F(3) = F(2) + F(1) = 2

…

F(n) = F(n-1) + F(n-2)

En otras palabras, cada elemento es la suma de los dos elementos previos:

0, 1, 1, 2, 3, 5, 8, 13, 21, …

Se pude calcular de manera recursiva de la siguiente forma:

```python
def fibonacci(n):
	if n==0:
		x=0 
	elif n==1:
		x=1 
	else:
		x = fibonacci(n-1) + fibonacci(n-2)
	return x
    
print(fibonacci(8)) # 21
```

Si se analiza el uso de las llamadas a la función, el proceso resulta ineficiente, pues en ocasiones los resultados se calculan múltiples ocasiones.

## Memoización

La función de fibonacci es pura, no tiene efectos colaterales, y en cada situación en particular que se llama con un valor, siempre se obtiene el mismo resultado.

Lo que se necesita es recordar es las veces que ha sido llamada antes, y recordar el resultado, y solo calcular el resultado para aquellos casos donde nunca ha sido utilizado anteriormente. 

```python
cache = dict()
	def fibonacci(n):
		if n in cache:
			return cache[n]
		if n==0:
			x=0 
		elif n==1:
			x=1 else:
		x = fibonacci(n-1) + fibonacci(n-2)
		cache[n] = x
		return x
    
print(fibonacci(8))
```

**functools `lru_cache`**

Es una buena solución, pero agrega código extra a la función fibonacci. El código extra, poco tiene que ver con lo que la función esta haciendo, tienen más que ver con la eficiencia que es posible que se desee utilizar con otras funciones y no solo con fibonacci.

 Los decoradores permiten solucionar este tipo de situaciones. La implementación de un decorador evitará  que se utilice una variable global -chache. Solo funciona para funciones que toman exactamente un argumento. También permite que la cache crezca hasta cualquier tamaño, cuando a veces sería más sensato establecer un tamaño máximo. 

El decorador, `lru_cache` resuelve este problema. Se encuentra en el módulo `functools`, y solo toma una línea de código:

```python
from functools import lru_cache
    
@lru_cache()
def fibonacci(n):
	print('Enter', n)
	if n==0:
		x=0 
	elif n==1:
		x=1 
	else:
		x = fibonacci(n-1) + fibonacci(n-2)
	print('Exit', n)
	return x

print(fibonacci(8))
```

Solo es necesario importar el decorador y agregar `@lru_cache` antes de la definición de la función y solo será llamada una vez la función fibonacci para cada valor `n`.

## Listas aplanadas

Considerar la lista:

```python
unflatten_list = [1, [2, 3], 4, [[5, 6], 7]]
```

Esta lista contiene una mezcla de enteros y listas. Estas listas pueden incluso contener una mezcla de enteros y listas, y puede repetirse de manara anidada el cualquier profundidad. Se quiere convertir en una sola lista que contenga los números enteros en el orden que ocurririan en la lista original.

```python
flatten_list = [1, 2, 3, 4, 5, 6, 7]
```

Una solución simple, requiere el uso de recursión. Se toma la lista original y se divide en dos partes, la primera parte de la lista, la cual la llamaremos `head` y el resto de la lista, la cual la llamaremos `tail`.

El método básico es aplanar la cabeza y aplanar la cola, después unirla de nuevo. Dado que ambas parte de la lista han sido aplanadas, entonces se unen y se tienen una lista completamente aplanada. Por supuesto, se llama de manera recursiva la función para aplanar a `head` y a `tail`.

Se requiere de una condición de parada. Se se pide aplanar algo que no es una lista (un entero, por ejemplo), se crea una lista del valor y se retorna. Y si se pide aplanar una lista vacía, se retorna una lista vacía.

```python
def flatten(x):
	if not isinstance(x, list):
		return [x]
	if x == []:
		return x
	return flatten(x[0]) + flatten(x[1:])
```

La función anterior funciona considerando que:

- Si se aplana correctamente `head` y `tail`, y se concatenan, se obtiene una lista aplanada.
- Cada iteración divide la lista, por lo que la hace más pequeña.
- Cada camino resulta finalmente en un valor que no es una lista (un valor entero) o una lista vacía. Estos dos casos se tratan correctamente devolviendo la representación de lista que se añadirá a otra lista para crear una solución.

**Una solución menos recursiva**

La función anterior funciona, la principal desventaja es que crea por lo menos un nivel de recursión por cada elemento de la lista. Esto es porque en cada nivel aplana a la cola de lista y no para hasta que la cola esta vacía. si el largo de la lista tienen 100 elementos entonces la profundidad de la recursión será de al menos de 100. Si el largo de la lista es mayor que 1000, incluso si la lista ya esta aplanada, fallará debido a la limitación de recursión de Python.

El problema principal es que, en cuestiones de funcionalidad pura se concluye en una solución que fallará tratando de aplanar una lista que ya esta aplanada. Se puede mejorar las cosas aplanando elementos que son realmente una lista. 

```python
def flatten(x):
	if not isinstance(x, list):
		return [x]
	if x == []:
		return x r = []
	for e in x:
		if isinstance(e, list):
			r += flatten(e)
		else:
			r.append(e)
	return r
```

Este método es recursivo, pero no aplica automáticamente la recursividad automáticamente en la cabeza y la cola en todas las ocurrencias. Itera sobre los elementos de `x`, y solo aplana cualquier lista que encuentre. SI las listas son anidadas, continuará de forma recursiva hasta aplanarlas, pero la profundidad de la recursión, no por el número de elementos en la lista original. Si la lista original esta plana, la función no realizará llamadas recursivas del todo.