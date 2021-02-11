class Vertex:
    indexes = 0

    def __init__(self, label):
        self.label = label
        self.index = Vertex.indexes
        Vertex.indexes += 1
        self.neighbours = []

    def add_neighbour (self, v):
        if v not in self.neighbours:
            self.neighbours.append(v)