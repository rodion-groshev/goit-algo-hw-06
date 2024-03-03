from bfs_iterative import bfs_iterative
from dfs_iteration import dfs_iterative
from hw_6_task_1 import main_roads

G = main_roads()
print("BFS:")
bfs_iterative(G, "Lviv")
print("\nDFS:")
dfs_iterative(G, "Lviv")


