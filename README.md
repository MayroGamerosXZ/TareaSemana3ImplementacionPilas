# TareaSemana3ImplementacionPilas
Requisitos
Python 3.x


# Proyecto de Evaluación de Expresiones

Este proyecto contiene una implementación de una pila para evaluar expresiones matemáticas y verificar el balance de paréntesis en cadenas de texto. Se utilizan dos clases principales: `Pila` y funciones para manejar la lógica de evaluación de expresiones.

## Clases

### Pila

La clase `Pila` implementa una estructura de datos de tipo pila (LIFO - Last In, First Out). Proporciona métodos para insertar y quitar elementos, así como para verificar si la pila está vacía.

#### Métodos

- `__init__()`: Inicializa una nueva pila vacía.
- `insertar(elemento)`: Agrega un elemento a la parte superior de la pila.
- `quitar()`: Elimina y devuelve el elemento en la parte superior de la pila. Lanza un `IndexError` si la pila está vacía.
- `tope_pila()`: Devuelve el elemento en la parte superior de la pila sin quitarlo. Lanza un `IndexError` si la pila está vacía.
- `pilavacia()`: Devuelve `True` si la pila está vacía, de lo contrario, devuelve `False`.

### Funciones

#### `parentesisvalanceados(expresion)`

Verifica si los paréntesis en una cadena de texto están balanceados. Utiliza una instancia de la clase `Pila` para realizar la verificación.

**Parámetros:**
- `expresion`: Una cadena de texto que contiene paréntesis.

**Retorna:**
- `True` si los paréntesis están balanceados, `False` en caso contrario.

#### `es_operador(caracter)`

Determina si un carácter es un operador matemático (paréntesis o signos de operación).

**Parámetros:**
- `caracter`: Un carácter a evaluar.

**Retorna:**
- `True` si el carácter es un operador, `False` en caso contrario.

#### `prioridad(caracter)`

Devuelve la prioridad de un operador matemático.

**Parámetros:**
- `caracter`: Un carácter que representa un operador.

**Retorna:**
- Un entero que representa la prioridad del operador (mayor número indica mayor prioridad).

## Ejemplo de Uso

1. **Verificación de Paréntesis Balanceados:**

   ```python
   cadena = input("Ingresa una cadena de texto: ")
   if parentesisvalanceados(cadena):
       print("Los Paréntesis están balanceados:", cadena)
   else:
       print("Los paréntesis no están balanceados:", cadena)

#Conversion de Notacion Fija a Postfija  
cadena = input("Expresión: ")
expresion_salida = ""
pila_operadores = Pila()

for caracter in cadena:
    if es_operador(caracter):
        # Lógica para manejar operadores
        ...
    else:
        expresion_salida += caracter

while not pila_operadores.pilavacia():
    operador = pila_operadores.quitar()
    expresion_salida += operador

print("La expresión en posfijo es:", expresion_salida)

