class Pila:
    def __init__(self):  # Cambiar _init_ a __init__
        self.items = []

    def insertar(self, elemento):
        self.items.append(elemento)

    def quitar(self):
        if not self.pilavacia():
            return self.items.pop()
        raise IndexError("Quitar de Pila Vacia")

    def tope_pila(self):
        if not self.pilavacia():
            return self.items[-1]
        raise IndexError("tope de Pila Vacia")

    def pilavacia(self):
        return len(self.items) == 0