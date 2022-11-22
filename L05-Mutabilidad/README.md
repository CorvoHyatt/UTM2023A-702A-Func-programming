[Programación Funcional](../README.md)> 5. Mutabilidad

Se dice que un objeto es mutable si su valor puede cambiar una vez que ha sido creado. Un objeto es inmutable si su valor es definido cuando es creado y nunca puede ser cambiado. Los valores inmutables, son valores de solo lectura. 

# Mutabilidad de Python

En Python las listas son mutables

```python
k = [10, 20, 30] # k is now [10, 7, 30]
k[1] = 7 k.append(5) # k is now [10, 7, 30, 5]
del k[2] # k is now [10, 7, 5]
```

Existen múltiples formas de alterar una lisa.

Las tuplas son muy similares a las listas, excepto porque son inmutables. Una vez que se crea una tupla, no puede ser modificada de ninguna forma. No se pueden agregar o eliminar elementos, y no pueden ser reemplazado un elemento con otro valor distinto. 

```python
t = (10, 20, 30)
t[1] = 7    # TypeError tuple doesn’t support assignment 
t.append(5) # AttributeError tuple has no append method 
del t[2]    # TypeError tuple doesn’t support deletion
```

Las variables no son objetos, por lo tanto es posible realizar lo siguinete:

```python
t = (10, 20, 30) 
t = (3, 2, 1)
```

**Tipo de de datos mutables e inmutables**

# Los números son inmutables

```python
a = 3 
b = a 
a = 4
```

En realidad el objeto int no cambia de valor, simplemente se crea un nuevo objeto y es asignado a la variable. En el ejemplo anterior, sería un desastre si las números mutaran.

## El problema con los objetos mutables

El problema con los objetos mutables, es que si pasa como argumento a una función, no se puede garantizar que la función no cambie el objeto. Por ejemplo:

```python
def evil_func(x):
	x[0] = 0
    
k = [1, 2, 3]
evil_func(k)
print(k)     # [0, 2, 3]
```

En el ejemplo anterior cuando `k` es pasado a la función , el objeto es modificado en la llamada.

Asumamos que `evil_func` no tiene razones obvias para alterar la lista que pasa como argumento, esto será sencillo de verificar si la función es simple y forma parte del mismo módulo. Por lo menos, mientras tú o alguien más edite la función en un futuro y se de cuenta que `evil_func` no debería de cambiar `x`, o crear un bug que signifique que `x` fue cambiado accidentalmente.

Pero que pasa si evil_func es parte de una librería de terceros, y no se tiene el control del código fuente. Entonces, se confía que el desarrollador de la librería no cambiara x. Pero aun, que el desarrollador de la librería pasa la lista a otra función, evil_func2, en la biblioteca de alguien más, que también no este soportado cambios sobre la lista. Por lo tanto, no solo estas confiando en la biblioteca de alguien más, si no estas confiando en cualquiera que ellos confíen. 

### Copiar a la defensiva

Una forma de lidiar con esto es copiar. En lugar de pasar una lista a un función, se pasa una copia de la lista a la función.

```python
def evil_func(x):
	x[0] = 0

k = [1, 2, 3]
evil_func(list(k))
print(k)     # [1, 2, 3]
```

la clave es pasar un objeto nuevo que se crea con la función list(), la cual crea una copia de a lista original.

Este solución no esta del todo mal, pero tiene desventajas:

- Es necesario recordar realizar el mecanismo de copiar
- Si la lista es muy larga, se crea una copia extra la cual genera gasto de tiempo
- Puede salirse de control

Si en algún punto `function1` llama a la `function2` y  llama a la `function3`, y cada llamada hace una copia defensiva, se pude terminar con los mismo datos copiados muchas veces.

Pero aun, si algunos programadores realizan una copia dentro de la función

```python
def evil_func(x):
	xcopy = list(x)
	xcopy[0] = 0
```

Este código genera que la lista sea copiada dos veces en cada ocasión que sea llamada.

# La inmutabilidad es la respuesta

La solución básica a este problema es, cuando sea posible, utilizar objetos de datos inmutables. La primera cosa que se necesita hacer es cambiar la definición de evil_func. Se debe especificar que x es inmutable (o más precisos, que x esta permitido ser inmutable). Por lo que, se permite pasar una tupla en lugar de una lista y la función debe seguir funcionando.

Aquí el código que asume que x es una tupla:

```python
def evil_func(x):
x[0] = 0
    t = (1, 2, 3)
    evil_func(t)
    print(t)     # (1, 2, 3)
```

En esta ocasión en lugar de corromper los datos de la tupla, la función evil_func lanzará una excepción porque esta intentando realizar algo ilegal al alterar un objeto que no esta permitido al ser inmutable.

# Cambiar objetos inmutables

En ocasiones es necesario cambiar objetos inmutables. Por supuesto, se pude realizar, pero se realiza mediante la copia del objeto original, modificado de algún modo. Existen diferentes maneras de hacerlo.

Un ejemplo simple, la función `tail()` toma una lista y retorna una lista que es idéntica excepto que el primer elemento es eliminado. Por lo que `[1, 2, 3]` se convierte en `[2, 3]`.

```python
def tail(x):
	if x: # If x is already empty do nothing
		del x[0]

k = [1, 2, 3]
tail(k)
print(k)     # [2, 3]
```

Esto solo funciona para una lista. Si la lista es pasada a la función y es modificada. Pero esto fallaría si se pasa una tupla como parámetro.

Si se desea realizar una función que trabaje con tuplas tanto como con lista. No es necesario realizar una modificación a los argumentos, en su lugar se puede hacer que la función retorne una tupla modificada.

```python
def tail(x):
	return x[1:]

t = (1, 2, 3)
t = tail(t)
print(t)     # (2, 3)
```

Este código hace lo mismo que la lista, pero de una forma más clara. La forma en como se llama la función cambia, ahora se asigna el valor que retorna a `t`.

El uso de slices para crear una nueva tupla es apropiado, pero es necesario considerar que se crea una copia de la lista. Si la tupla es muy grande, y se realiza esta operación múltiples ocasiones, habra una reducción en el desempeño en terminos de tiempos de ejecución y uso de memoria. Esto ocurre en el caso de que la tupla se extremadamente grande, caso contrario no debe ser preocupante. 

Un bonus adicional de esta función es que no solo funciona con tuplas o listas, sino también, con cadenas. Se utiliza el término secuencia, para referirse a listas, tuplas, cadenas o estructuras de datos similares.

Existen diferentes formas de procesar datos inmutables:

## Uso de slices

Para realizar la agregación de un elemento `3` en medio de una tupla en la posición `n`.

```python
u = v[:n] + (3) + v[n:]
```

Alternativamente, para eliminar un elemento de una posición n de la tupla:

```python
u = v[:n] + v[n+1:]
```

El único detalle que hay que tener en cuenta, es la creación de múltiples copias de la tupla. 

## Uso de list comprenhensions

Agunas ocasiones es necesario realizar operaciones sobre cada uno de los elementos de la secuencias. Por ejemplo, suponer que se desea agregar un 1 a cada elemeno en una tupla. Por lo que (1, 5, 7) se convierte en (2, 6, 8). Un list comprenhension es ideal para realizar el cambio:

```python
u = [x + 1 for x in v] 
t = tuple(u)
```

## Uso de un ciclo

Suponer que se desea duplicar todos los ceros contenidos en las tuplas, entonces (1, 0, 2, 0, 5) se convierte en (1, 0, 0, 2, 0, 0, 5). No se puede realizar esto fácilmente con un list comprenhension, por lo que un ciclo resulta más simple:

```python
u = []
    for x in v:
        u.append(x)
        if x == 0:
            u.append(x)
    t = tuple(u)
```

## Convertir los datos a una lista

Si resulta demasiado complicado procesar una tupla, se puede convertir a una lista, realizar lo necesario, y convertir nuevamente el resultado a una tupla.

# El problema con los objetos inmutables

A pesar de que los datos inmutables resuelven muchos problemas con la modificación accidental de datos cuando son pasados a través de un programa, tiene un costo:

- Quizá sea necesario pasar a través de algunos obstáculos para procesar datos
- Se puede acabar haciendo varias copias de los datos

En la mayoría de los casos vale la pena hacer uso de datos inmutables. La principal excepción es cuando se utilizan datos muy grandes. En este caso, realizar copias de los datos no es práctico y es mejor utilizar datos mutables, y simplemente tener cuidado dónde y cuándo se modifican.

# La inmutabilidad es superficial

Si se utilizan estructuras más complejas, es importante entender exactamente que significa la inmutabilidad.

Considerar el caso de la tupla que contiene múltiples listas:

```python
t = ([1, 2], [4, 6], [5, 9])
```

Se puede acceder a los datos de distintas formas

```python
print(t[1])    # [4, 6]
print(t[2][1]) # 9
```

La primera sentencia accede a `t[1]`, el segundo elemento de la tupla `t`, el cual es la lista `[4, 6]`. La siguiente sentencia accede a `t[2][1]` . Por supuesto, que `t[2]` es el tercer elemento de `t`, la lista `[5, 9]`. Esto significa que `t[2][1]` es el segundo elemento de ese arreglo, el cual es `9`.

Pero que ocurre, si se intenta modificar estos valores:

```python
t[1] = 0 # Error
t[2][1] = 0 # t becomes ([1, 2], [4, 6], [5, 0])
```

no se puede cambiar `t[1]`  porque se estaría alterando la tupla. Pero se puede cambiar `t[2][1]` porque es solo un cambio en la lista que ocurre al interior de la tupla.

Si no has utilizado tuplas de arreglos antes, esto puede parecer un poco absurdo, porque parece somo si se alterará la tupla. Pero en realidad, no se esta alterando la tupla del todo. Piensa en eso como:

- Inicialmente, la tupla contiene 3 referencias, a tres listas de objetos.
- Si se cambia un valor de uno de los elementos de la lista de objetos
- La tupla aun sigue conteniendo tres referencias a las mismas tres listas de objetos. Una de estas listas ahora contiene diferentes valores, pero todavía es la misma lista de objetos. La tupla no ha cambiado.