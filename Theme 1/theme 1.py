from collections import defaultdict

class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

    def __repr__(self):
        return f"Edge({self.src} -> {self.dest}, weight={self.weight})"

class Graph:
    def __init__(self):
        # Список ребер
        self.edges = []
        # Список дуг (аналогично списку ребер, но дуги - это ориентированные ребра)
        self.arcs = []
        # Список смежности
        self.adjacency_list = defaultdict(list)
        # Список пучков дуг (группировка дуг по источнику)
        self.arc_bundles = defaultdict(list)

    def add_vertex(self, vertex):
        """Добавление вершины в граф."""
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, src, dest, weight):
        """Добавление ребра в граф."""
        self.add_vertex(src)
        self.add_vertex(dest)

        edge = Edge(src, dest, weight)
        self.edges.append(edge)
        self.arcs.append(edge)
        self.adjacency_list[src].append((dest, weight))
        self.arc_bundles[src].append(edge)

    def remove_vertex(self, vertex):
        """Удаление вершины из графа."""
        if vertex in self.adjacency_list:
            # Удаление всех ребер, связанных с вершиной
            self.edges = [e for e in self.edges if e.src != vertex and e.dest != vertex]
            self.arcs = [e for e in self.arcs if e.src != vertex and e.dest != vertex]
            del self.adjacency_list[vertex]
            # Удаление вершины из списка смежности других вершин
            for v in self.adjacency_list:
                self.adjacency_list[v] = [(d, w) for d, w in self.adjacency_list[v] if d != vertex]
            # Удаление пучков дуг
            del self.arc_bundles[vertex]

    def remove_edge(self, src, dest):
        """Удаление ребра из графа."""
        self.edges = [e for e in self.edges if not (e.src == src and e.dest == dest)]
        self.arcs = [e for e in self.arcs if not (e.src == src and e.dest == dest)]
        self.adjacency_list[src] = [(d, w) for d, w in self.adjacency_list[src] if d != dest]
        self.arc_bundles[src] = [e for e in self.arc_bundles[src] if e.dest != dest]

    def find_vertex(self, vertex):
        """Поиск вершины в графе."""
        return vertex in self.adjacency_list

    def find_edge(self, src, dest):
        """Поиск ребра в графе."""
        for edge in self.edges:
            if edge.src == src and edge.dest == dest:
                return edge
        return None

    def get_adjacency_list(self):
        """Получение списка смежности."""
        return dict(self.adjacency_list)

    def get_edges(self):
        """Получение списка ребер."""
        return self.edges

    def get_arcs(self):
        """Получение списка дуг."""
        return self.arcs

    def get_arc_bundles(self):
        """Получение списка пучков дуг."""
        return dict(self.arc_bundles)

# Пример использования
graph = Graph()

# Добавление вершин и ребер
graph.add_edge(0, 1, 5)
graph.add_edge(0, 2, 3)
graph.add_edge(1, 2, 2)
graph.add_edge(2, 3, 1)

# Вывод структур данных
print("Список ребер:", graph.get_edges())
print("Список дуг:", graph.get_arcs())
print("Список смежности:", graph.get_adjacency_list())
print("Список пучков дуг:", graph.get_arc_bundles())

# Удаление ребра
graph.remove_edge(0, 2)
print("\nПосле удаления ребра 0 -> 2:")
print("Список ребер:", graph.get_edges())
print("Список дуг:", graph.get_arcs())
print("Список смежности:", graph.get_adjacency_list())
print("Список пучков дуг:", graph.get_arc_bundles())

# Удаление вершины
graph.remove_vertex(1)
print("\nПосле удаления вершины 1:")
print("Список ребер:", graph.get_edges())
print("Список дуг:", graph.get_arcs())
print("Список смежности:", graph.get_adjacency_list())
print("Список пучков дуг:", graph.get_arc_bundles())

# Поиск вершины и ребра
print("\nПоиск вершины 2:", graph.find_vertex(2))
print("Поиск ребра 2 -> 3:", graph.find_edge(2, 3))