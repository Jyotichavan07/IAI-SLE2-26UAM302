
from collections import deque
import argparse

# ==========================================================
# SLE-2: BFS vs DFS using py-spy
# ==========================================================

# 1. Graph Definition

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': ['I'],
    'F': ['J'],
    'G': ['K'],
    'H': [],
    'I': [],
    'J': [],
    'K': []
}


# 2. BFS Algorithm

def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set()
    nodes_expanded = 0

    while queue:
        current, path = queue.popleft()

        if current in visited:
            continue

        visited.add(current)
        nodes_expanded += 1

        if current == goal:
            return path, nodes_expanded

        for neighbour in graph[current]:
            if neighbour not in visited:
                queue.append(
                    (neighbour, path + [neighbour])
                )

    return None, nodes_expanded


# 3. DFS Algorithm

def dfs(graph, start, goal):
    stack = [(start, [start])]
    visited = set()
    nodes_expanded = 0

    while stack:
        current, path = stack.pop()

        if current in visited:
            continue

        visited.add(current)
        nodes_expanded += 1

        if current == goal:
            return path, nodes_expanded

        for neighbour in reversed(graph[current]):
            if neighbour not in visited:
                stack.append(
                    (neighbour, path + [neighbour])
                )

    return None, nodes_expanded


# 4. Experiment Settings

START_NODE = 'A'
GOAL_NODE = 'I'

# Repeat searches to give py-spy enough work to sample.
REPETITIONS = 100_000


# 5. Workload to Profile

def run_bfs_workload():
    for _ in range(REPETITIONS):
        bfs(graph, START_NODE, GOAL_NODE)


def run_dfs_workload():
    for _ in range(REPETITIONS):
        dfs(graph, START_NODE, GOAL_NODE)


# 6. Display Results

def display_results(algorithm_name, search_function):
    path, nodes_expanded = search_function(
        graph, START_NODE, GOAL_NODE
    )

    print("=" * 60)
    print("SLE-2: BFS vs DFS using py-spy")
    print("=" * 60)

    print("Algorithm            :", algorithm_name)
    print("Start Node            :", START_NODE)
    print("Goal Node             :", GOAL_NODE)
    print("Search Repetitions    :", REPETITIONS)
    print("Path Found            :", " -> ".join(path)
          if path else "No path found")
    print("Nodes Expanded        :", nodes_expanded)

    print("-" * 60)
    print("Execution-time profiling is performed by py-spy.")
    print("Inspect the generated profile for sampled activity.")
    print("=" * 60)


# 7. Select Which Algorithm to Profile

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Profile BFS or DFS using py-spy"
    )

    parser.add_argument(
        "algorithm",
        choices=["bfs", "dfs"],
        help="Choose bfs or dfs"
    )

    args = parser.parse_args()

    if args.algorithm == "bfs":
        display_results("BFS", bfs)
        run_bfs_workload()

    else:
        display_results("DFS", dfs)
        run_dfs_workload()

    print("Profiling workload completed.")
