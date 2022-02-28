
class Graph:
    def __init__(self, gdict = None):
        if gdict is None:
            gdict = []

        self.gdict = gdict

    # Get the keys of the dictionary
    def getVertices(self):
        return list(self.gdict.keys())

    # Add the vertex as a key
    def addVertex(self, vertex):
        if vertex not in self.gdict:
            self.gdict[vertex] = []

    # List the edge names
    def edges(self):
        edgename = []

        for vertex in self.gdict:
            for nextvertex in self.gdict[vertex]:
                if {nextvertex, vertex} not in edgename:
                    edgename.append({vertex, nextvertex})
        return edgename

    # Add the new edge
    def addEdge(self, edge):
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.gdict:
            self.gdict[vertex1].append(vertex2)
        else:
            self.gdict[vertex1] = [vertex2]
