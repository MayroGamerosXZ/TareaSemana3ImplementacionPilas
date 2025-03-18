# Función para verificar si los paréntesis están balanceados
from IngresosFilas import Pila


def parentesisvalanceados(expresion):
    pila = Pila()
    pares = {")": "(", "]": "[", "}": "{"}
    for caracter in expresion:
        if caracter in pares.values():
            pila.insertar(caracter)
        elif caracter in pares.keys():
            if pila.pilavacia() or pila.quitar() != pares[caracter]:
                return False
    return pila.pilavacia()

# Entrada del usuario
cadena = input("Ingresa una cadena de texto: ")
if parentesisvalanceados(cadena):
    print("Los Parentesis están balanceados:", cadena)
else:
    print("Los paréntesis no están balanceados:", cadena)

# Funciones para la conversión a notación posfija
def es_operador(caracter):
    return caracter in ["(", ")", "*", "/", "-", "+"]

def prioridad(caracter):
    if caracter in ["*", "/"]:
        return 3
    elif caracter in ["+", "-"]:
        return 2
    else:
        return 0

expresion_salida = ""
pila_operadores = Pila()

cadena = input("Expresión: ")
for caracter in cadena:
    if caracter == "":
        continue
    if es_operador(caracter):
        if caracter == "(":
            pila_operadores.insertar(caracter)
        elif caracter == ")":
            while not pila_operadores.pilavacia() and pila_operadores.tope_pila() != "(":
                operador = pila_operadores.quitar()
                expresion_salida += operador
            pila_operadores.quitar()  # Quitar el '('
        else:
            while (not pila_operadores.pilavacia() and
                   prioridad(caracter) <= prioridad(pila_operadores.tope_pila())):
                operador = pila_operadores.quitar()
                expresion_salida += operador
            pila_operadores.insertar(caracter)
    else:
        expresion_salida += caracter

while not pila_operadores.pilavacia():
    operador = pila_operadores.quitar()
    expresion_salida += operador

print("La expresión en posfijo es:", expresion_salida)