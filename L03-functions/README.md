[Programación Funcional](../README.md)> 3. Funciones

## Funciones

Las funciones son bloques de código que son diseñados para realizar un trabajo específico.

Ejemplo de la definición de una función.

```python
def greet_user():
    """Display a simple greeting."""
    print("Hello!")
```

Llamada de la función:

```python
 greet_user()
```

Uso de parámetros en funciones:

```python
def greet_user(username):
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")

# Llamada de la función
greet_user('jesse')
```

La variable username en la definición de la función `greet_user()` es un **parámetro** y es una pieza de información necesaria para que la función pueda realizar su trabajo. El valor `‘jesse’` en la llamada `greet_user('jesse')` es un ejemplo de un **argumento**.

Cuando se llama a un función, Python debe realizar la correspondencia entre cada argumento de la llamada de la función y con los parámetros de la definición de la función. Los valores que deben de corresponden a cada parámetro son llamados **argumentos posicionales**.

```python
def describe_pet(animal_type, pet_name): 
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# Llamada a la función
describe_pet('hamster', 'harry')

# El oden importa en los argumentos posicionales
describe_pet('harry', 'hamster')
```

**Argumentos de palabra clave**

Se asocia directamente el nombre y el valor con el argumento, por lo que cuando se pase el argumento a la función, no exista confusión.

```python
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')
```

**Valores por defecto**

```python
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# Llamada a la función
describe_pet(pet_name='willie')
describe_pet('willie')
```

**Argumentos opcionales:**

```python
def get_formatted_name(first_name, last_name, middle_name=''): 
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
    full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
```

**Equivalencia de llamadas a función:**

```python
# A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')
# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')
```

**Retorno de valores:**

```python
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

# Llamada a la función
musician = get_formatted_name('jimi', 'hendrix') 
print(musician)
```

**Retorno de un diccionario:**

```python
def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)
```

```python
def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
  
musician = build_person('jimi', 'hendrix', age=27)
print(musician)
```

**Modificación de una lista en una función**

Cuando se pasa una lista a una función, la función puede modificar la lista, cualquier cambio realizado a lista dentro de la función será permanente, con la finalidad de hacer eficiente el trabajo cuando se trabaja con una gran cantidad de datos.

```python
# Start with some designs that need to be printed.

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
   
# Simulate printing each design, until none are left.
#  Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()

    # Simulate creating a 3D print from the design.
    print("Printing model: " + current_design)
    completed_models.append(current_design)

# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
```

```python
def print_models(unprinted_designs, completed_models): 
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # Simulate creating a 3D print from the design.
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed.""" 
    print("\nThe following models have been printed:") 
    for completed_model in completed_models:
        print(completed_model)

    unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
    completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
```

**Prevenir que una función modifique una lista**

Mandar una copia de la lista

```python
function_name(list_name[:])
```

**Pasar un número arbitrario de argumentos**

```python
def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
  print("\nMaking a pizza with the following toppings:")
  for topping in toppings:
        print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
```

El asterisco indica a Python la creación de una tupla que empaca cualquier valor recibido.

**Mezcla de argumentos posicionales y arbitrarios**

El argumento arbitrario debe ser colocada al final de la lista de parámetros en la definición de la función. Es decir, los argumentos posicionales y de palabra clave deben ir primero.

```python
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

**Uso de argumentos arbitrarios de palabras clave**

Si desea aceptar un número arbitrario de argumentos, pero no se sabe que tipo de información se recibirá, se puede utilizar pares de claves-valor.

```python
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)
```

El doble asterisco en el parámetro de la definición de la función crea un diccionario.

# Módulos

Crear módulo `pizza.py`

```python
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) +
        "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
```

**Importar un módulo completo**

```python
import pizza
```

**Importar una función en específico**

```python
from pizza import make_pizza
```

**Uso de un alias para una función**

```python
from pizza import make_pizza as mp
```

**Uso de un alias para aun módulo**

```python
import pizza as p
```

**Importar todas las funciones de un módulo**

```python
from pizza import *
```

# Type hits

Uso de type hits
