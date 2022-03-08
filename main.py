from Maze import *
from Maze_Solver import *


m = Maze(10, 10)
m.dfs()
# m.show(3)

ms = MazeSolver(m)
ms.maze2graph()
