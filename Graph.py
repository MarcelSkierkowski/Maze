from collections import defaultdict


class Graph:
    def __init__(self, directed=False):
        self.gdict = defaultdict(set)
        self.directed = directed

    def get_vertices(self):
        """Return all vertices"""
        return self.gdict.keys()

    def add_vertex(self, vertex):
        """ Add vertex without connection """
        if vertex not in self.gdict:
            self.gdict[vertex] = set()

    def edges(self):
        """ Return list of edges in graph """
        edgename = []

        for vertex in self.gdict:
            for nextvertex in self.gdict[vertex]:
                if {nextvertex, vertex} not in edgename:
                    edgename.append({vertex, nextvertex})
        return edgename

    def add_edge(self, vertex1, vertex2):
        """ Add connection between vertex1 and vertex2 """

        self.gdict[vertex1].add(vertex2)
        if not self.directed:
            self.gdict[vertex2].add(vertex1)

    def remove_vertex(self, vertex):
        """ Remove all connections with vertex and them destroy itself """
        for _, edges in self.gdict.items():
            try:
                edges.remove(vertex)
            except KeyError:
                pass

        try:
            self.gdict.pop(vertex)
        except KeyError:
            pass

    def is_connected(self, vertex1, vertex2):
        """ Vertex1 is directly connected with vertex2 """

        return vertex1 in self.gdict and vertex2 in self.gdict[vertex1]
