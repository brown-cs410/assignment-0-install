from typing import List, Tuple, Dict
from queue import Queue  
from search_problem import SearchProblem, State
from maze import Maze

def bfs(problem: SearchProblem[State]) -> Tuple[List[State], Dict[str, int]]:
    """
    Performs Breadth-First Search (BFS) on the given problem.

    Args:
        problem (SearchProblem[State]): The search problem to solve.

    Returns:
        Tuple[Optional[List[State]], Dict[str, int]]:
            - A list of states representing the solution path, or None if no solution was found.
            - A dictionary of search statistics, including:
                a. 'path_length': The length of the final path.
                b. 'states_expanded': The number of states expanded during the search.
                c. 'max_frontier_size': The maximum size of the frontier during the search.
    """
    # TODO: Update these values
    stats = {"path_length": 0, "states_expanded": 0, "max_frontier_size": 0} 
    
    pass

def dfs(problem: SearchProblem[State]) -> Tuple[List[State], Dict[str, int]]:
    """
    Performs Breadth-First Search (DFS) on the given problem.

    Args:
        problem (SearchProblem[State]): The search problem to solve.

    Returns:
        Tuple[Optional[List[State]], Dict[str, int]]:
            - A list of states representing the solution path, or None if no solution was found.
            - A dictionary of search statistics, including:
                a. 'path_length': The length of the final path.
                b. 'states_expanded': The number of states expanded during the search.
                c. 'max_frontier_size': The maximum size of the frontier during the search.
    """
    # TODO: Update these values
    stats = {"path_length": 0, "states_expanded": 0, "max_frontier_size": 0}
    
    pass

############### SANDBOX ###############
def main():
    # Initialize the maze and generate it based on given dimensions
    print("Generated Maze:")
    width, height = 30, 30
    maze = Maze(width, height)

    # Run BFS and DFS to find paths
    print("BFS Path:")
    bfs_path, bfs_stats = bfs(maze)
    print(bfs_path)
    maze.visualize_maze(path=bfs_path, algorithm_name="bfs")
    
    print("DFS Path:")
    dfs_path, dfs_stats = dfs(maze)
    print(dfs_path)
    maze.visualize_maze(path=dfs_path, algorithm_name="dfs")

if __name__ == "__main__":
    main()
