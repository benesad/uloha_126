from vertex import Vertex

class Graph:

    def __init__(self, lines):
        self.vertices = {}
        self.first_vertex = None

        for line in lines:
            [label1, label2] = line.split(" ")
            if label1 not in self.vertices: # add label1 to the list in Vertex class if its not there yet 
                self.vertices[label1] = Vertex(label1)
                if self.first_vertex == None:
                    self.first_vertex = self.vertices[label1]
            if label2 not in self.vertices: # add label2 to the list in Vertex class if its not there yet
                self.vertices[label2] = Vertex(label2)
            self.vertices[label1].add_neighbour(self.vertices[label2])
            self.vertices[label2].add_neighbour(self.vertices[label1])