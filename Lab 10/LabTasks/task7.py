class Vertex:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

    def add_neighbor(self, vertex):
        self.neighbors.append(vertex)

    def __str__(self):
        return f"Vertex({self.value})"


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, value):
        if value not in self.vertices:
            new_vertex = Vertex(value)
            self.vertices[value] = new_vertex
        else:
            print(f"Vertex {value} already exists.")

    def add_vertices(self, values):
        for value in values:
            self.add_vertex(value)

    def add_edge(self, value1, value2):
        if value1 not in self.vertices:
            self.add_vertex(value1)
        if value2 not in self.vertices:
            self.add_vertex(value2)

        self.vertices[value1].add_neighbor(self.vertices[value2])
        self.vertices[value2].add_neighbor(self.vertices[value1])

    def add_neighbors(self, value, neighbors):
        if value not in self.vertices:
            self.add_vertex(value)
        for neighbor in neighbors:
            if neighbor not in self.vertices:
                self.add_vertex(neighbor)
            self.vertices[value].add_neighbor(self.vertices[neighbor])

    def display_graph(self):
        for vertex in self.vertices.values():
            neighbors = [neighbor.value for neighbor in vertex.neighbors]
            print(f"{vertex.value}: {neighbors}")


graph = Graph()


graph.add_vertex(1)
graph.add_vertices([2, 3, 4])


graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)

graph.add_neighbors(3, [4, 2])

graph.display_graph()
