import random

# Función para crear un camino aleatorio de n x m baldosas
def crear_camino(n, m):
    camino = []
    for i in range(n):
        fila = []
        for j in range(m):
            fila.append(random.choice(["B", "M", "D"]))
        camino.append(fila)
    return camino

# Función para imprimir el camino en la consola
def imprimir_camino(camino):
    for fila in camino:
        print(" ".join(fila))

# Función para detectar minas armadas en el camino
def detectar_minas(camino):
    minas_detectadas = []
    for i in range(len(camino)):
        for j in range(len(camino[0])):
            if camino[i][j] == "M":
                minas_detectadas.append((i, j))
    return minas_detectadas

# Función para desactivar minas en el camino
def desactivar_minas(camino, minas_detectadas):
    for mina in minas_detectadas:
        i, j = mina
        camino[i][j] = "D"

# Función para recorrer el camino y recuperar minas desactivadas
def recorrer_camino(camino):
    minas_recuperadas = 0
    for i in range(len(camino)):
        for j in range(len(camino[0])):
            if camino[i][j] == "D":
                minas_recuperadas += 1
    return minas_recuperadas

# Crear un camino de 5x5 y mostrarlo en la consola
camino = crear_camino(5, 5)
imprimir_camino(camino)

# Detectar y desactivar las minas en el camino
minas_detectadas = detectar_minas(camino)
desactivar_minas(camino, minas_detectadas)

# Mostrar el camino actualizado en la consola
imprimir_camino(camino)

# Recorrer el camino y mostrar cuántas minas desactivadas se recuperaron
minas_recuperadas = recorrer_camino(camino)
print("Se recuperaron", minas_recuperadas, "minas desactivadas")
