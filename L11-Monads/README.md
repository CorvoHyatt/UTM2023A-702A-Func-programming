[Programación Funcional](../README.md)> 11. Functors y Monadas

# 11. Functors y Monadas

Functors y las monadas son dos tipos de objetos importantes en la programación funcional. En esencia lo que se hace es envolver un valor. El envoltorio entonces controla como las funciones son aplicadas al valor. Esto permite extender las capacidades de funciones ordinarias, por ejemplo para hacerlos trabajar automáticamente con colecciones, o permitirles trata valores que pueden no existir (llamados opcionales en algunos lenguajes).

De hecho, existen tres tipos relacionados:

- Functors son del tipo básico. Un functor tiene un método `map` que permite controlar como las funciones son aplicadas.
- Functors aplicativos (frecuentemente solo llamadas aplicativos) son un subconjunto de functors. Los functors aplicativos pueden hacer lo que un functor puede hacer, pero tienen capacidades extras, Todos los aplicativos son functors, pero no todos los functors son functors aplicativos.
- Monadas son un subconjunto de las functors aplicativos. Estos pueden hacer todo lo que un functor aplicativo hace, incluso más.

Estos objetos no son parte de la biblioteca estándar de Python, pero existen bibliotecas para implementarlos. En este ejemplo se utiliza `oslash`, una biblioteca que implementa functors.

La mayoría de las cosas vistas aquí aplica para otras bibliotecas o incluso otros lenguajes. La mayor parte de la sintaxis de `oslash` esta basada en Haskell.

Se podría determinar que el uso de functors y monadas no son muy comunes. Estos son usados en el concepto puro de programación funcional en situaciones que son difíciles de manejar son código procedural. En Python, se tienen métodos de código procedural, por lo que se utilizarán frecuentemente estas opciones en lugar de preferir monadas. Pero es muy útil saber que existen.

# Functors

En algunos casos el concepto functor se refiere a un objeto de función. Pero ese no es el significado que toma aquí.

En programación en el lenguaje Haskell y en `oslash`, los functors son  un objeto que envuelve un valor y provee un método `map` que puede ser usado para aplicar una función a este valor.

La mayoría de los functors abordados aquí son también monadas, por lo que tienen la funcionalidad de functors, aplicativos y monadas. 

## El functor `Just`

El functor `Just` es un simple envoltorio alrededor de un valor. Se pude crear un functor `Just` como este:

```python
from oslash import Just

a = Just(3)
print(a)
```

Este código imprime `Just 3`, para indicar que es un envoltorio `Just` al rededor de 3. Ahora si se desea aplicar la función de `operator` `neg` a este objeto, se obtendrá un error porque `neg` no reconoce lidiar con el functor.

```python
from operator import neg
neg(a) # Error!
```

Lo que se debe hacer es utilizar en su lugar `map` para aplicar la función. `Just` tiene una función map, porque es un functor.

```python
b = a.map(neg)
print(b)
```

Esto imprime `Just` `-3` . Esto es porque `Just.map()` sabe cómo aplicar una función al valor envuelto y retorna un resultado envuelto.

Se puede también aplicar una función a un functor utilizando el operador `%`. Este es un operador infijo que acepta la función primero, seguida del functor que será aplicado.

```python
b = neg % a
```

## El functor `Nothing`

El functor `Nothing` es muy simple. Representa a nada, en una forma muy similar al tipo None en Python. A pesar de que dijimos que un functor envuelve un valor, Nothing es la excepción. No envuelve un valor, es simplemente nada.

Se crea Nothing de la siguiente forma:

```python
from oslash import Nothing

a = Nothing()
print(a)
```

Esto imprime `Nothing`, como se espera. Qué pasa cuando se aplica una función a `Nothing`:

```python
b = neg % a
print(b)
```

El resultado es `Nothing`. De hecho, el resultado de aplicar cualquier función a `Nothing` siempre es `Nothing`.

## El functor `List`

El functor `List` envuelve una lista de valores

```python
from oslash import List
a = List([1, 2, 3]) 
print(a) 
print(type(a))
```

Esto imprime

```python
[1, 2, 3]
<class 'oslash.list.List'>
```

La lista es impresa de forma similar que en listas estándar de Python, pero el tipo que se muestra es un objeto `oslash`.

Si se aplica una función a esta lista.

```python
from oslash import List
from operator import neg

a = List([1, 2, 3]) 
b = neg % a print(b) 
print(type(b))
```

Esto produce:

```python
[-1, -2, -3]
<class 'oslash.list.List'>
```

Se ha aplicado la función neg a cada elemento de la lisa. Esto es lo que el functor List hace, se puede utilizar cualquier función `List.map`( llamado por el operador `%`) se aplicara a cada elemento de la lista.

# Functors aplicativos

Un functor aplicativo envuelve una función. Se puede aplicar su función a otras functors, por ejemplo:

```python
from oslash import Just
from operator import neg
    
a = Just(3)
f = Just(neg)
b = f.apply(a)
print(b)
```

Este código funciona porque `Just` no solo es un functor, es también un functor aplicativo. Un functor ordinario no  tiene un método `apply`. Por lo que, teniendo envuelta a la función `neg` en el functor aplicativo `f`, se puede aplicar a `a`. El resultado es `-3` como se vio anteriormente.

Se puede utilizar el operador `*` como su versión infija de `apply` (justo como `%` es una versión infija de map).

```python
a = Just(3)
b = add % a
print(b)
```

Esto imprime:

```python
Just functools.partial(<built-in function add>, 3)
```

Esto es muy prometedor. Una función parcial de `add`, con `3` aplicado, envuelto en un aplicativo `Just`. Se puede aplicar a hora el segundo argumento, utilizando el operador `*`.

```python
c = b * Just(6)
print(c)
```

Lo cual da como resultado `Just 9`

Veamos cómo funciona con una función de 4 argumentos, como la función `quad`.

```python
a = quad % Just(1) * Just(3) * Just(2) * Just(0)
```

Se puede pensar que `%` es el corchete que abre y el `*` es como la coma entre argumentos. no hay corchete que cierra, las analogías no son siempre perfectas. De otra forma, considerar que se envuelve `quad` en un functor `Just` y usa `*`.

```python
a = Just(quad) * Just(1) * Just(3) * Just(2) * Just(0)
```

Es importante entender que ocurre:

```python
a = Just(quad) # Just <function quad >
a = a*Just(1) # Just functools.partial(<function quad, 1)
a = a*Just(3) # Just functools.partial(<function quad, 1, 2)
a = a*Just(2) # Just functools.partial(<function quad, 1, 2, 3) 
a = a*Just(0) # Just 2
```

Cada paso crea una nueva función parcial, envuelta en un functor `Just`, con los parámetros dados en un conjunto de funciones parciales. Esto es similar a la currificación.

# Monadas

Una monada envuelve de una forma similar que un functor. Sin embargo, una monada tienen una función adicional llamada `bind` que:

- Acepta un solo parámetro
- Retorna un valor envuelto en una monada

Como `map`, la función `bind`  por si misma es responsable de envolver el valor retornado. Esto significa que la función `bind` puede decidir en que tipo de monada envolver el resultado.

En un ejemplo, la función `oneover` retorna `1/x` en una monada `Just`:

```python
from oslash import Just, Nothing

def oneover(x):
	ret = 1/x
	return Just(ret)
    
a = Just(2).bind(oneover)
print(a)
    
a = Just(0).bind(oneover)
print(a)
```

Ls primera llamada, cubre `oneover` con el valor `Just 2` correctamente retorna `Just 0`. La mona `Just` desenvuelve el valor `2`, y lo pasa la función `oneover`, el cual retorna `Just 0.5`.

La segunda llamada, sin embargo, pasa `0` a `oneover`, lo cual resulta en excepción de una división entre cero, no es alguna que se quiera en programación pura.

Una solución es que `oneover` tienen que elegir qué tipo de monada tiene que retornar. Se puede tratar la excepción y retornar la monada `Nothing`.

```python
def oneover(x):
        try:
            ret = 1/x
        except:
            return Nothing()
        return Just(ret)
```