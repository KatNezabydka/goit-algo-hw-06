import networkx as nx
import matplotlib.pyplot as plt


def print_table(distances, visited):
    # Верхній рядок таблиці
    print("{:<10} {:<10} {:<10}".format("Вершина", "Відстань", "Перевірено"))
    print("-" * 30)

    # Вивід даних для кожної вершини
    for vertex in distances:
        distance = distances[vertex]
        if distance == float('infinity'):
            distance = "∞"
        else:
            distance = str(distance)

        status = "Так" if vertex in visited else "Ні"
        print("{:<10} {:<10} {:<10}".format(vertex, distance, status))
    print("\\n")


def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())
    visited = []

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        visited.append(current_vertex)
        unvisited.remove(current_vertex)

        # Вивід таблиці після кожного кроку
        print_table(distances, visited)

    return distances


# Приклад графа у вигляді словника
graph = {
    'Kate': {'Nick': 5, 'Charlie': 10},
    'Nick': {'David': 5, 'Kate': 5},
    'Charlie': {'David': 10, 'Natalia': 2, 'Kate': 10},
    'David': {'Natalia': 3, 'Charlie': 10, 'Nick': 5},
    'Natalia': {'Frank': 4, 'Mike': 10, 'Charlie': 2, 'David': 3},
    'Frank': {'Mike': 4, 'Natalia': 4},
    'Mike': {'Frank': 4, 'Natalia': 10}
}

# Створення графа
G = nx.Graph()
# Додавання міст і доріг
G.add_edge('Kate', 'Nick', weight=5)
G.add_edge('Kate', 'Charlie', weight=10)
G.add_edge('Nick', 'David', weight=5)
G.add_edge('Charlie', 'David', weight=10)
G.add_edge('Charlie', 'Natalia', weight=2)
G.add_edge('David', 'Natalia', weight=3)
G.add_edge('Natalia', 'Frank', weight=4)
G.add_edge('Natalia', 'Mike', weight=10)
G.add_edge('Frank', 'Mike', weight=4)

# Візуалізація графа
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=15, width=2)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Виклик функції для вершини Kate
dijkstra(graph, 'Kate')

plt.show()