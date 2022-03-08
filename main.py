import matplotlib.pyplot as plt

from Maze import *
from Graph import *


def maze2graph(maze) -> Graph:
    """ changes a maze to a graph object """
    row, col = maze.shape
    graph = Graph()

    for r in range(row):
        for c in range(col):
            x = maze[r][c].x
            y = maze[r][c].y

            if not maze[r][c].up:
                graph.add_edge((x, y), (x, y - 1))
            if not maze[r][c].left:
                graph.add_edge((x, y), (x - 1, y))
            if not maze[r][c].right:
                graph.add_edge((x, y), (x + 1, y))
            if not maze[r][c].bottom:
                graph.add_edge((x, y), (x, y + 1))
    return graph


def plot_graph(graph: Graph, offset=0.5):
    """ This function is used to visualize the graph """

    vx = list()
    vy = list()

    lx = list()
    ly = list()

    for vertex, edges in graph.gdict.items():
        x, y = vertex
        vx.append(x + offset)
        vy.append(y + offset)

        for ex, ey in edges:
            plt.plot([x + offset, ex + offset], [y + offset, ey + offset], color='blue')

    plt.scatter(vx, vy)


if __name__ == "__main__":
    m = Maze(20, 20)
    m.dfs()

    g = maze2graph(m.grid)

    plot_graph(g, 0.5)
    
    plt.show()
    # m.show(2)
