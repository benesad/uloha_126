class Vertex:

    def __init__(self, label):
        self.label = label
        self.neighbours = []

    def add_neighbour (self, v):
        if v not in self.neighbours:
            self.neighbours.append(v)