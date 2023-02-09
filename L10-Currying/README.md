[Programación Funcional](../README.md)> 10. Aplicaciones parciales y currificación

# 10. Aplicaciones parciales y currificación

# Aplicaciones parciales

Las aplicaciones parciales son una manera de crear una nueva función basada en una función existente pero con algunos de los parámetros ya definidos con un valor selecionado.

Por ejemplo, aquí tenemos un closure base que crea una aplicación parcial de la función extandar `max`. 

```python
def maxn(n):
	def f(x):
		return max(n, x)
	return f
```

Ahora, por ejemplo, si se llama a `maxn(0)`, retorna un closure de `f(x)` con los valores de `n` ajustados a `0`. En otras palabras, retorna una función que calcula `max(0, x)`. 

```python
max0 = maxn(0)
print(max0(3)) # Equivalent to max(0, 3) -> 3 
print(max0(-1)) # Equivalent to max(0, -1) -> 0
```

Se ha creado una nueva función `max0` y un par de casos de prueba para probar que calcula `max(0, x)`. Esta función reemplaza cualquier valor negativo con `0`.

Un ejemplo del uso de la aplicación parcial con `map`. En este caso se utiliza `maxn` para crear una función anónima que es utilizada por `map`.

```python
m = map(maxn(3), [1, 2, 3, 4, 5]) 
print(list(m))
```

El resultado es `[3, 3, 3, 4, 5]` (todos lo valores menores que 3 son sustituidos por 3). Mediante la definición de la función `maxn` , se pueden realizar aplicaciones parciales de max en una forma compacta y expresiva.

# Funciones con más variables

Por ejemplo, si utilizamos la función: $y = ax^2 + bx + c$ 

Para valores dados `a`, `b`, `c` y `x`.  

```python
def quad(a, b, c, x):
	return a*x*x + b*x + c
```

Aquí tenemos una situación, donde `a`, `b`, y `c` son definidas y lo que se desea variar es `x`. Se puede hacer esto muy fácil con la ayuda de un closure.

```python
def quad_abc(a, b, c):
	def f(x):
		return quad(a, b, c, x)
	return f
```

Esto nos permite crear funciones parciales para calcular, por ejemplo:

$x^2- 3x +2$

```python
myquad = quad_abc(1, -3, 2)
print(myquad(0))  # 2
print(myquad(1))  # 0
print(myquad(2))  # 0
```

También se puede crear diferentes aplicaciones parciales, por ejemplo, suponer que se quiere aplicar valores para `a` y `c`, pero dejar `b` y `x` como variables a definirse después:

```python
def quad_ac(a, c):
	def f(b, x):
		return quad(a, b, c, x)
	return f

myquad = quad_ac(1, 2)

print(myquad(0, 1))
print(myquad(1, 2))
print(myquad(2, -1))
```

La función `myquad` es ahora una función que tiene definido como `a` el valor 1 y como `c` el valor 2. Cuando se llama `mysquad` se pasan dos argumentos, los valores correspondientes a `b` y `x`.

Al utilizar closures, se puede elegir un conjunto de combinaciones de `a`, `b`, `c` y `x` que será la aplicación parcial y dejar el resto de los parámetros a ser definidos posteriormente cuando se llame la función.

## Funciones `functools.partial`

El módulo `functools` incluye una función `partial` que pude ser utilizada para crear aplicaciones parciales de una función.

```python
from functools import partial

max0 = partial(max, 0)
    
print(max0(3))  # 3
print(max0(-1)) # 0
```

En combinación con `map`:

```python
m = map(partial(max, 3), [1, 2, 3, 4, 5])
    
print(list(m))
```

La ventaja es que no se tiene que declara el closure `maxn`. El código es más declarativo y recae solamente en una función de biblioteca estándar.

La desventaja es que la llamada de map es ligeramente más compleja y larga.

## `functools.partial` con más variables

La función `functools.partial` puede ser utilizada para crear una función parcial para funciones con más de dos variables, por ejemplo, en la función `quad`.

```python
pquad3 = partial(quad, 1, -3, 2) # a, b, c = 1, -3, 2 
print(pquad3(0)) # x = 0
```

Para ser claros, `quad` toma 4 argumentos. En la llamada parcial, se proporcionan 3 argumentos para crear una función parcial `pquad3`. Cuando se llama `pquad3`, se proporciona el argumento `x`.

Se pueden proporcionar pocos argumentos de ser necesario. En el otro ejemplo, se proporcionan dos argumentos en la llamada parcial. Esto crea la función `pquad2` donde el primer argumento es `a = 4`, y `b = 1`. La llamada a `pquad2` debe proporcionar valores para `c` y `x`.

```python
pquad2 = partial(quad, 4, 1) # a, b = 4, 1 
print(pquad2(3, 1)) # c, x = 3, 1
```

Como último ejemplo, se proporciona un argumento a la llamada parcial. Esto crea la función `pquad1` donde el primer argumento a = 4. La llamada a `pquad1` debe proporcionar los valores de `b`, `c` y `x`.

```python
pquad1 = partial(quad, 4) # a = 4 
print(pquad1(1, 3, 1)) # b, c, x = 1, 3, 1
```

Algo que no se puede hacer con partials. Es lo equivalente a `myquad_ac`, donde se definen los valores de `a` y `c` en la función parcial. La sintaxis de partial no permite elegir y decidir que argumentos tendrán valores previos.

### Aplicación de argumentos `keyword`

Una función parcial pueden aplicar argumentos keyword:

```python
def make_print(sep):
	def f(*args):
		return print(*args, sep=sep)
	return f
  
print_csv = make_print(', ')
print_colon = make_print(':')
print_csv(1, 2, 3)         # 1, 2, 3
print_colon(1, 2, 3)       # 1:2:3
```

La función `make_print` retorna una aplicación parcial de la función estándar print, con el valor del argumento `keyword` `sep`  definido. `sep` es una cadena que es insertada entre los argumentos (esta es una funcionalidad de `print` estándar).

Nótese también que la función interna `f`  en `make_print` acepta `*args`. Esto significa que la aplicación parcial de `print` acepta múltiples argumentos  y los imprime todos, separados por la cadena `sep`.

Se utiliza `make_print` para crea dos nuevas funciones, `print_csv` que imprime los valores separados por comas y `print_colon` que imprime los valores se parados por dos puntos.

Se pueden utilizar `keywords` con la función `partial` también. Ejemplo:

```python
from functools import partial
print_csv = partial(print, sep=', ') 
print_colon = partial(print, sep=':')
```

## No pasar por alto las soluciones simples

Antes de querer aplicar funciones parciales a todo, siempre es importante tener en cuenta que existen alternativas. Por ejemplo, al crear `max0` 

Solución original

```python
def maxn(n):
	def f(x):
		return max(n, x)
	return f

max0 = maxn(0)
```

Si solo se utilizará `max0` (nunca se utilizará `maxn` con otro valor `n` diferente de cero), quizá sea mejor definir `max0` directamente (sin crear el closure `maxn`):

```python
def max0(x):
	return max(0, x)
```

Si solo se utiliza la función una vez:

```python
map(lambda x: max(0, x), [1, 2, 3, 4, 5])
```

No significa que  no se utilicen funciones parciales en estas situaciones, solo es necesario recordar de siempre tomar en cuenta las alternativas y elegir aquellas que hacen el código más robusto y legible.

# Currificación

La currificación es similar a las aplicaciones parciales pero con un ligero enfoque distinto. 

El término currificación deriva de Haskell Curry, el matemático que realizó una gran cantidad de trabajo en la teoría de currificación. El lenguaje de programación Haskell es también nombrado en referencia a él.

La currificación no es parte del lenguaje Python, pero existen múltiples bibliotecas de programación funcional de tipo código abierto. En esta caso utilizaremos `PyMoad`.

Se currifica una función al aplicar el decorador `@curry` en su declaración. 

```python
from pymonad import curry
    
@curry
def quadc(a, b, c, x):
	return a*x*x + b*x + c
```

Se puede utilizar `quadc` de la misma forma que `quad`

```python
y = quadc(1, -3, 2, 0)
```

Se puede también llamar `quadc` con solo tres argumentos. En ese caso, retorna un objeto invocable (un objeto que puede ser utilizado como un objeto función). Este objeto invocable `f`, puede ser llamado con un solo argumentos para obtener el resultado `y`.

```python
f = quadc(1, -3, 2) 
y = f(0)
```

Es muy similar a crear una función parcial:

```python
pquad3 = partial(quad, 1, -3, 2)
y = pquad3(0)
```

Se puede llamar `quadc` con dos argumentos. Y retorna una objeto invocable que necesita dos argumentos extras:

```python
 f = quadc(1, -3)
    y = f(2, 0)
```

Nuevamente esto es similar a crear una función parcial con `a` y `b` previamente asignados , y después pasar los argumentos `c` y `x`. y por supuesto, es posible currificar la función con un solo argumento.

```python
f = quadc(1)
y = f(-3, 2, 0)
```

De hecho se puede crear mayor flexibilidad, ya que se puede separa la llamada de la función muchas veces, por ejemplo:

```python
f = quadc(1)
g = f(-3, 2)
y = g(0)
```

En este caso, `f` es un invocable que requiere 3 argumentos. Si pasamos dos argumentos, se obtiene un objeto `g` invocable que necesita un argumento. Se se llama a `g` con un argumento se obtiene el resultado de `y`.

## Cuándo utilizar la currificación

EL uso de la currificación y la aplicación parcial son muy similares. Se puede utilizar ambos con `map`.

Ejemplo de uso de aplicación parcial (`functools partial`)

```python
c = [1, 2, 3, 4, 5]
x = [2, 4, 6, 8, 10]
m = map(partial(quad, 1, 2), c, x)
```

Se ha creado una función parcial de `quad`, con `a =1` y `b = 2`. Después se mapea esta función en dos listas que contienen los valores de `c` y `x`.

Mediante currificación la solución es:

```python
c = [1, 2, 3, 4, 5]
x = [2, 4, 6, 8, 10]
m = map(quadc(1, 2), c, x)
```

- Esta solución funciona por el uso del decorador `@curry`
- La segunda implementación resulta más simple, ya que no requiere el uso de `partial`
- El uso de `@curry` permite crear una función `quadc` que puede ser invocada de diferentes maneras:
    
    ```python
    quadc(1, 2, 3, 4)
    quadc(1,2)(3, 4)
    quadc(1, 2)(3)(4)
    quadc(1)(2, 3, 4)
    ```
    

Un punto a considerar que la llamada a funciones currificadas es menos eficiente que el llamado a funciones normales. 

La consideración más importante es que la currificación crea funciones se comportan un tanto absurdas.

Comparado con la función partial. El código resulta más explícito. 

# Composición

```python
square(math.sin(x))

reversed(range(n))
```

Cuando una función opera en el resultado de una función, se refiere a la composición de funciones.

```python
from operator import add, mul
   
add(2, mul(3, x))
```

El ejemplo anterior compone a dos funciones, donde cada una toma dos argumentos, haciendo difícil la generalización. Se puede mejorar esto utilizando funciones parciales.

```python
from functools import partial
    
f = partial(add, 2)
g = partial(mul, 3)

f(g(x))
```

o en una línea

```python
partial(add, 2)(partial(mul, 3)(x))
```

## Creación de una función compuesta

En el capítulo de closures, se revisó una forma de realizar una composición mediante una función `compose`. En esta sección se renombra esta función a `compose2` 

```python
def compose2(f, g):      
	def fn(x):
		return f(g(x))
	return fn
```

En lugar de utilizar `reversed` y `range` para crear directamente un iterador en cuenta regresiva, se puede componer estas dos funciones para crear una nueva función, `countdown`, que crea un iterador que cuenta en forma regresiva.

```python
countdown = compose2(reversed, range) 
countdown(n)
```

Esto resulta más práctico cuando se utilizan funciones parciales. En lugar de directamente utilizar `partial` en `add` y `mul` como antes, se crea una nueva función que las compone:

```python
addmul = compose2(partial(add, 2), partial(mul, 3)) 
addmul(x)
```

Es mucho más claro en este caso lo que ocurre en código. 

Existen múltiples implementaciones de código abierto, pero antes de abordarlas retomemos `compose2` que acepta más de dos funciones.

Se desea componer las funciones `p`, `q`, `r`, `s`. Para crear una sola función:

```python
p(q(r(s(x))))
```

Se puede crear esto mediante la repetición de la función `compose2`:

```python
f = compose2(p, q) # f calculates p(q(x))
g = compose2(f, r) # g calculates p(q(r(x)))
h = compose2(g, s) # h calculates p(q(r(s(x))))
```

Para comprender el siguiente paso, imaginemos a los valores con números `a`, `b`, `c`, `d` y la función `compose2` con `add`. La cadena de operaciones luce como:

```python
x = add(a, b)
y = add(x, c)
z = add(y, d)
```

O mas sucinta:

$((a + b) + c) + d)$

Esta es simple la suma de todos los números.  Visto de otra forma se ha reducido la lista de números utilizando el operador `add`.

Lo mismo ocurre para las composiciones. Para componer una lista de funciones, simplemente reducimos la lista de funciones utilizando la operación `compose2`:

```python
def compose(*f):
	def compose2(f, g):
		def fn(x):
			return f(g(x))
		return fn
	return functools.reduce(compose2, f)
```

Se ha introducido el closure `compose2` como función interna de `compose`. Esto lo convierte a privado, no necesitamos que `compose2` sea accesible, porque `compose` puede componer 2 funciones, o 3 o 4, etc. Se utiliza internamente `compose2` para reducir la lista de funciones.

El valor retornado de compose es el resultado de reducir la lista de funciones de entrada, f, con la función compose2, resultado en una sola función compuesta.

Un punto final, la función reduce, da como resultado un error si es llamado con una lista vacía, a menos que se proporcione un tercer parámetro como valor inicial. Si se desea evitar esto, se provee un valor ajustable, pero que se debe utilizar?

El valor inicial, debe ser el valor identidad para el operador que se esta utilizando. Si estamos utilizando el operador `add`, se utiliza 0, porque x +  0 = x. Si se utiliza la `mul` debe ser 1, porque x * 1 = x. En el caso de la composición, se requiere un valor que actúe como identidad cuando se compone con cualquier función. Esta es la función f(x) que retorna x. Para evitar este error, se cambia la última línea del `compose`:

```python
return functools.reduce(compose2, f, lambda x: x)
```

## Bibliotecas que soportan la composición

Existen bibliotecas de código abierto que proveen soporte de programación funcional. incluyendo la función `compose`. `funcy` y `fn.py` son dos bibliotecas que pueden ser utilizadas [github.com](http://github.com) o con `pip`.

PyMonad provee composición de funciones currificadas.

En lugar de utilizar la función compose, PyMonad utiliza un operador compose `*`

Primero se crea una versión currificada de las funciones `reversed` y `range`

```python
from pymonad import curry

@curry
def reversedc(x):
	return reversed(x)

@curry
def rangec(n):
	return range(n)
```

Una vez que están definidas, se realiza la composición:

```python
countdown = reversedc * rangec
```

Dado que todas las funciones que son currificadas, se vuelve más fácil realizar funciones parciales. Ejemplo de funciones currificadas `add` y `mul`:

```python
@curry

def addc(a, b):
	return a + b
    
@curry
def mulc(a, b):
	return a * b
```

La función `addmul`:

```python
addmul = addc(2) * mulc(3)
```

Esto es claramente más legible que la versión previa:

```python
addmul = compose2(partial(add, 2), partial(mul, 3))
```

a