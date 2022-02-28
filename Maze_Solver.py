import collections
from Graph import *


class Maze_solver:
    def __init__(self):
        self.graph = Graph()

    def maze2graph(self):
        pass

    # Depth First Traversal
    def DFS(self, start, stop, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)

        if start is stop:
            return visited

        for next in self.graph[start] - visited:
            self.DFS(next, stop, visited)
        return visited

    # Breadth First Traversal
    def BFS(self, start, stop):
        seen, queue = set([start]), collections.deque([start])
        while queue:
            vertex = queue.popleft()
            for node in self.graph[vertex]:
                if node is not seen:
                    seen.add(node)
                    queue.append(node)
                    if node is stop:
                        return seen
