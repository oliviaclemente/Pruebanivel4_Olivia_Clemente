from ej1 import Graph

# Crear el grafo y cargar los datos
mcu_graph = Graph()

mcu_graph.add_vertex("Iron Man")
mcu_graph.add_vertex("The increíble Hulk")
mcu_graph.add_vertex("Khan")
mcu_graph.add_vertex("Thor")
mcu_graph.add_vertex("Captain América")
mcu_graph.add_vertex("Ant-Man")
mcu_graph.add_vertex("Nick Fury")
mcu_graph.add_vertex("The Winter Soldier")

mcu_graph.add_edge("Iron Man", "The increíble Hulk", 6)
mcu_graph.add_edge("Iron Man", "Khan", 0)
mcu_graph.add_edge("Iron Man", "Thor", 1)
mcu_graph.add_edge("Iron Man", "Captain América", 8)
mcu_graph.add_edge("Iron Man", "Ant-Man", 7)
mcu_graph.add_edge("Iron Man", "Nick Fury", 3)
mcu_graph.add_edge("Iron Man", "The Winter Soldier", 2)

mcu_graph.add_edge("The increíble Hulk", "Khan", 6)
mcu_graph.add_edge("The increíble Hulk", "Thor", 0)
mcu_graph.add_edge("The increíble Hulk", "Captain América", 6)
mcu_graph.add_edge("The increíble Hulk", "Ant-Man", 1)
mcu_graph.add_edge("The increíble Hulk", "Nick Fury", 8)
mcu_graph.add_edge("The increíble Hulk", "The Winter Soldier", 9)

mcu_graph.add_edge("Khan", "Thor", 0)
mcu_graph.add_edge("Khan", "Captain América", 1)
mcu_graph.add_edge("Khan", "Ant-Man", 2)
mcu_graph.add_edge("Khan", "Nick Fury", 1)
mcu_graph.add_edge("Khan", "The Winter Soldier", 5)

mcu_graph.add_edge("Thor", "Captain América", 1)
mcu_graph.add_edge("Thor", "Ant-Man", 1)
mcu_graph.add_edge("Thor", "Nick Fury", 5)
mcu_graph.add_edge("Thor", "The Winter Soldier", 9)

mcu_graph.add_edge("Captain América", "Ant-Man", 2)
mcu_graph.add_edge("Captain América", "Nick Fury", 4)
mcu_graph.add_edge("Captain América", "The Winter Soldier", 5)

mcu_graph.add_edge("Ant-Man", "Nick Fury", 1)
mcu_graph.add_edge("Ant-Man", "The Winter Soldier", 6)

mcu_graph.add_edge("Nick Fury", "The Winter Soldier", 1)


# Árbol de expansión máximo desde el vértice que contiene a Iron-Man, Thor y The Winter Soldier
max_spanning_tree = mcu_graph.max_spanning_tree("Iron Man")
print("Árbol de expansión máximo:")
for vertex in max_spanning_tree.vertices:
    print(vertex, "->", max_spanning_tree.vertices[vertex])


# Número máximo de episodio que comparten dos personajes y los pares de personajes que coinciden con dicho número
max_episodes, matching_pairs = mcu_graph.max_shared_episodes()
print("\nNúmero máximo de episodios compartidos:", max_episodes)
print("Pares de personajes que coinciden:")
for pair in matching_pairs:
    print(pair[0], "-", pair[1])

# Personajes que aparecieron en nueve episodios de la saga
characters_in_nine_episodes = mcu_graph.characters_in_episodes(9)
print("\nPersonajes que aparecieron en nueve episodios de la saga:")
for character in characters_in_nine_episodes:
    print(character)

