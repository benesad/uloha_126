from vertex import Vertex

class Graph:

    def __init__(self, lines):
        self.vertices = {}

        for line in lines:
            [label1, label2] = line.split(" ")
            if label1 not in self.vertices:
                self.vertices[label1] = Vertex(label1)
            if label2 not in self.vertices:
                self.vertices[label2] = Vertex(label2)
            self.vertices[label1].add_neighbour(self.vertices[label2])
            self.vertices[label2].add_neighbour(self.vertices[label1])