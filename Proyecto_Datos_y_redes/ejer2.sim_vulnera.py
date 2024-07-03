class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vulnerabilidades = []

    def agregar_vulnerabilidad(self, vulnerabilidad):
        self.vulnerabilidades.append(vulnerabilidad)

class Vulnerabilidad:
    def __init__(self, nombre):
        self.nombre = nombre

class Simulador:
    def __init__(self):
        self.red = {}

    def agregar_nodo(self, nodo):
        self.red[nodo.nombre] = nodo

    def simular_ataque(self, atacante, objetivo):
        if atacante in self.red and objetivo in self.red:
            for vulnerabilidad in self.red[objetivo].vulnerabilidades:
                if vulnerabilidad in self.red[atacante].vulnerabilidades:
                    print(f"¡Ataque exitoso! {atacante} comprometió {objetivo}.")
                    return
            print(f"El ataque de {atacante} a {objetivo} falló.")
        else:
            print("Nodo no encontrado en la red.")

# Crear nodos y vulnerabilidades
nodo1 = Nodo("Servidor1")
nodo1.agregar_vulnerabilidad(Vulnerabilidad("XSS"))

nodo2 = Nodo("Servidor2")
nodo2.agregar_vulnerabilidad(Vulnerabilidad("Fuerza Bruta"))

# Construir la red
simulador = Simulador()
simulador.agregar_nodo(nodo1)
simulador.agregar_nodo(nodo2)

# Simular un ataque
simulador.simular_ataque("Servidor2", "Servidor1")
