from ej3 import Grafo, Vertice

# Cargar distancias entre superhéroes
matriz_distancias = [
    [675, 400, 166, 809, 720, 399, 233],
    [675, 0, 540, 687, 179, 348, 199, 401],
    [400, 540, 0, 107, 752, 521, 385, 280],
    [166, 687, 107, 0, 111, 540, 990, 361],
    [809, 179, 752, 111, 0, 206, 412, 576],
    [720, 348, 521, 540, 206, 0, 155, 621],
    [399, 199, 385, 990, 412, 155, 0, 100],
    [233, 401, 280, 361, 576, 621, 100, 0]
]

# Crear grafo
grafo = Grafo(matriz_distancias)

# Obtener recorrido de menor distancia
inicio = grafo.vertices[6]  # Nick Fury en los cuarteles de S.H.I.E.L.D.
recorrido = grafo.obtener_recorrido_menor_distancia(inicio)

# Obtener recorrido de vuelta
recorrido_vuelta = grafo.obtener_recorrido_vuelta(recorrido)

# Imprimir resultados
print("Recorrido de menor distancia:")
for vertice in recorrido:
    print(vertice.nombre)

print("Recorrido de vuelta:")
for vertice in recorrido_vuelta:
    print(vertice.nombre)
