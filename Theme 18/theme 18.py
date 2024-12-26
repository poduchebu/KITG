from collections import deque

class Edge:
    def __init__(self, to, capacity, reverse_edge=None):
        self.to = to
        self.capacity = capacity
        self.flow = 0
        self.reverse_edge = reverse_edge

class Dinic:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.graph = [[] for _ in range(num_nodes)]
        self.level = [0] * num_nodes

    def add_edge(self, u, v, capacity):
        forward_edge = Edge(v, capacity)
        reverse_edge = Edge(u, 0, forward_edge)
        forward_edge.reverse_edge = reverse_edge
        self.graph[u].append(forward_edge)
        self.graph[v].append(reverse_edge)

    def bfs(self, source, sink):
        self.level = [-1] * self.num_nodes
        queue = deque()
        queue.append(source)
        self.level[source] = 0

        while queue:
            u = queue.popleft()
            for edge in self.graph[u]:
                if self.level[edge.to] == -1 and edge.capacity > edge.flow:
                    self.level[edge.to] = self.level[u] + 1
                    queue.append(edge.to)

        return self.level[sink] != -1

    def dfs(self, u, sink, flow):
        if u == sink:
            return flow

        for edge in self.graph[u]:
            if self.level[edge.to] == self.level[u] + 1 and edge.capacity > edge.flow:
                min_flow = min(flow, edge.capacity - edge.flow)
                result = self.dfs(edge.to, sink, min_flow)
                if result > 0:
                    edge.flow += result
                    edge.reverse_edge.flow -= result
                    return result

        return 0

    def max_flow(self, source, sink):
        max_flow = 0
        while self.bfs(source, sink):
            while True:
                flow = self.dfs(source, sink, float('inf'))
                if flow == 0:
                    break
                max_flow += flow
        return max_flow

# Пример использования:
if __name__ == "__main__":
    num_nodes = 6
    dinic = Dinic(num_nodes)

    dinic.add_edge(0, 1, 16)
    dinic.add_edge(0, 2, 13)
    dinic.add_edge(1, 2, 10)
    dinic.add_edge(1, 3, 12)
    dinic.add_edge(2, 1, 4)
    dinic.add_edge(2, 4, 14)
    dinic.add_edge(3, 2, 9)
    dinic.add_edge(3, 5, 20)
    dinic.add_edge(4, 3, 7)
    dinic.add_edge(4, 5, 4)

    source = 0
    sink = 5
    print("Максимальный поток:", dinic.max_flow(source, sink))