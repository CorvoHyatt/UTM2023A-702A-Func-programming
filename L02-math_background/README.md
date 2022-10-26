[Programación Funcional](../README.md)> Fundamentos matemáticos

## Conjuntos

Los conjuntos `set` almacenan múltiples valores en una variable. Recordar que un conjunto es una colección de elementos desordenados, no intercambiables, no tienen un posición en la estructura y no se permiten elementos duplicados.

- Desordenados: Los elementos del conjunto no tienen un orden definido, por lo que pueden aparecer en un orden diferente cada vez que son utilizados y no pueden ser referidos por un índice o clave.
- No intercambiables: No puede ser cambiado ningún elemento después de ser creado el `set`.
- No permite duplicados: No se pueden agregar elementos con el mismo valor.

```python
fruits = {'apple', 'banana', 'cherry', 'orange', 'pear'}
favorite_fruits = {'apple', 'banana', 'cherry', 'orange', 'pear', 'apple'}
numbers = {1, 5, 7, 9, 3}
things = {"abc", 34, True, 40, "male"}
```

**Obtener el tamaño de un conjunto**

```python
fruits = {'apple', 'banana', 'cherry', 'orange', 'pear'}
print(len(fruits))
```

**Ciclos con conjuntos**

```python
fruits = {"apple", "banana", "cherry"}

for fruit in fruits:
  print(fruit)
```

**Verificar si un elemento esta en el conjunto**

```python
fruits = {"apple", "banana", "cherry"}
print('banana' is fruits)
```

**Agregar un elemento al conjunto**

```python
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
```

**Agregar un conjunto al conjunto con `update()`**

```python
fruits = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

fruits.update(tropical)
```

**Agregar cualquier iterable al conjunto con `update()`**

```python
fruits = {"apple", "banana", "cherry"}
list_of_fruits = ["kiwi", "orange"]

fruits.update(tropical)
```

**Eliminar elementos de un conjunto con `remove()` o `discard()`**

```python
fruits = {"apple", "banana", "cherry"}
fruits.remove('banana')
```

En el caso de que el elemento no exista, `remove()` lanzará un error.

```python
fruits = {"apple", "banana", "cherry"}
fruits.discard('banana')
```

En el caso de que el elemento no exista, `discard()` no lanzará un error.

**Eliminar el último elemento con `pop()`**

```python
fruits = {"apple", "banana", "cherry"}
new_fruits = fruits.pop()

print(fruits)
print(new_fruits)
```

Dado que los elementos están desordenados al utilizar `pop()` no se sabe cuál elemento será eliminado.

**Vaciar el conjunto con `clear()`**

```python
fruits = {"apple", "banana", "cherry"}
fruits.clear()

print(fruits)
```

**Eliminar el conjunto con `del`**

```python
fruits = {"apple", "banana", "cherry"}
del fruits

print(fruits)
```

## Operaciones con conjuntos

**Unión de dos conjuntos**

```python
letters = {"a", "b" , "c"}
numbers = {1, 2, 3}

alophanumerics = letter.union(numbers)
print(alphanumerics)
```

**Intersección de dos conjuntos con `intersection_update()`**

```python
fruits = {"apple", "banana", "cherry"}
logos = {"google", "microsoft", "apple"}

fruits.intersection_update(logos)

print(fruits)
```

**Intersección de dos conjuntos con `intersection()`**

```python
fruits = {"apple", "banana", "cherry"}
logos = {"google", "microsoft", "apple"}

my_set = fruits.intersection(logos)

print(my_set)
```

**Mantener a todos menos a los duplicados con `simmetric_difference_update()`**

```python
fruits = {"apple", "banana", "cherry"}
logos = {"google", "microsoft", "apple"}

fruits.simmetric_difference_update(logos)

print(fruits)
```

**Mantener a todos menos a los duplicados `simmetric_difference()`**

```python
fruits = {"apple", "banana", "cherry"}
logos = {"google", "microsoft", "apple"}

x = fruits.simmetric_difference(logos)

print(x)
```

**Métodos a utilizar sobre conjuntos**

| Método | Descripción |
| --- | --- |
| add() | Agregar un nuevo elemento al conjunto |
| clear() | Remueve todos los elementos del conjunto |
| copy() | Devuelve una copia del conjunto |
| difference() | Devuelve un conjunto que contiene la diferencia entre dos o más conjuntos |
| difference_update() | Elimina un elemento den el conjunto que también esta incluido en otro conjunto. |
| discard() | Elimina un elemento |
| intersection() | Devuelve un conjunto, que es la intersección de dos conjuntos |
| intersection_update() | Elimina los elementos de un conjunto que no están presentes en otro conjunto o en otros conjuntos especificados. |
| isdisjoint() | Devuelve si dos conjuntos tienen una intersección o no |
| issubset() | Devuelve si otro conjunto esta contenido en un conjunto |
| issuperset() | Devuelve si un conjunto esta contenido en otro conjunto |
| pop() | Eliminar un elemento del conjunto |
| remove() | Elimina el elemento especifico |
| symmetric_difference() | Devuelve un conjunto con la diferencia simétrica de dos conjuntos |
| symmetric_difference_update() | Inserta la diferencia simétrica de un conjunto en otro conjunto  |
| union() | Devuelve un conjunto que contiene la unión de dos conjuntos |
| update() | Actualiza el conjunto con la unión de un conjunto con otro conjunto. |