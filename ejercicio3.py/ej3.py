class Vertice:
    def __init__(self, nombre):
        self.nombre = nombre
        self.visitado = False

class Grafo:
    def __init__(self, matriz_distancias):
        self.vertices = []
        self.matriz_distancias = matriz_distancias
        for i in range(len(matriz_distancias)):
            self.vertices.append(Vertice(i))
    
    def obtener_distancia(self, origen, destino):
        return self.matriz_distancias[origen][destino]
    
    def obtener_vertice_no_visitado(self):
        for vertice in self.vertices:
            if not vertice.visitado:
                return vertice
        return None
    
    def obtener_recorrido_menor_distancia(self, origen):
        recorrido = []
        vertice_actual = origen
        vertice_actual.visitado = True
        recorrido.append(vertice_actual)
        while True:
            siguiente_vertice = None
            distancia_minima = float('inf')
            for i in range(len(self.vertices)):
                if not self.vertices[i].visitado:
                    distancia = self.obtener_distancia(vertice_actual.nombre, i)
                    if distancia < distancia_minima:
                        siguiente_vertice = self.vertices[i]
                        distancia_minima = distancia
            if siguiente_vertice is None:
                break
            siguiente_vertice.visitado = True
            recorrido.append(siguiente_vertice)
            vertice_actual = siguiente_vertice
        return recorrido
    
    def obtener_recorrido_vuelta(self, recorrido):
        recorrido_vuelta = recorrido.copy()
        recorrido_vuelta.reverse()
        return recorrido_vuelta

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

grafo = Grafo(matriz_distancias)
inicio = grafo.vertices[6]  # Nick Fury en los cuarteles de S.H.I.E.L.D.
recorrido = grafo.obtener_recorrido_menor_distancia(inicio)
recorrido_vuelta = grafo.obtener_recorrido_vuelta(recorrido)

print("Recorrido de menor distancia:")
for vertice in recorrido:
    print(vertice.nombre)

print("Recorrido de vuelta:")
for vertice in recorrido_vuelta:
    print(vertice.nombre)
