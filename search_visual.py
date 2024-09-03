from typing import List, Tuple
from queue import Queue
from search_problem import SearchProblem
from maze import Maze
import matplotlib.pyplot as plt
import numpy as np

def bfs(problem: SearchProblem[Tuple[int, int]], ax):
    queue = Queue()
    queue.put((problem.get_start_state(), [problem.get_start_state()]))
    visited = set()

    while not queue.empty():
        current, path = queue.get()
        problem.visualize_path(path, ax, "BFS")
        if problem.is_goal_state(current):
            
            return path
        for successor, cost in problem.get_successors(current).items():
            if successor not in visited:
                visited.add(successor)
                queue.put((successor, path + [successor]))
    return []

def dfs(problem: SearchProblem[Tuple[int, int]], ax):
    stack = [(problem.get_start_state(), [problem.get_start_state()])]
    visited = set()

    while stack:
        current, path = stack.pop()
        problem.visualize_path(path, ax, "DFS")
        if current not in visited:
            visited.add(current)
            if problem.is_goal_state(current):
                return path
            for successor, cost in problem.get_successors(current).items():
                if successor not in visited:
                    stack.append((successor, path + [successor]))
    return []

def main():
    maze = Maze(10, 20)  
    fig, ax = plt.subplots(figsize=(12, 8))
    plt.ion()

    print("BFS Path:")
    bfs_path = bfs(maze, ax)
    print(bfs_path)

    print("DFS Path:")
    dfs_path = dfs(maze, ax)
    print(dfs_path)
    plt.ioff()
    plt.show()

if __name__ == "__main__":
    main()

