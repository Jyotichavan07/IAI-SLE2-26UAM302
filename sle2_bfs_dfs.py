from collections import deque
import timeit


# ==========================================================
# SLE-2: BFS vs DFS Empirical Performance Analysis
# ==========================================================

# ----------------------------------------------------------
# 1. Graph Definition
# ----------------------------------------------------------

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


# ----------------------------------------------------------
# 2. BFS Algorithm
# ----------------------------------------------------------

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
                queue.append((neighbour, path + [neighbour]))

    return None, nodes_expanded


# ----------------------------------------------------------
# 3. DFS Algorithm
# ----------------------------------------------------------

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
                stack.append((neighbour, path + [neighbour]))

    return None, nodes_expanded


# ----------------------------------------------------------
# 4. Experiment Settings
# ----------------------------------------------------------

START_NODE = 'A'
GOAL_NODE = 'I'

NUMBER_OF_RUNS = 10

# Number of times the algorithm is executed
# inside each timing measurement.
REPETITIONS_PER_RUN = 10000


# ----------------------------------------------------------
# 5. Measure BFS
# ----------------------------------------------------------

bfs_times = []

for _ in range(NUMBER_OF_RUNS):

    elapsed_time = timeit.timeit(
        lambda: bfs(graph, START_NODE, GOAL_NODE),
        number=REPETITIONS_PER_RUN
    )

    # Average time for one BFS execution
    average_time = (elapsed_time / REPETITIONS_PER_RUN) * 1000

    bfs_times.append(average_time)


# Get BFS result and node count
bfs_path, bfs_nodes = bfs(
    graph,
    START_NODE,
    GOAL_NODE
)

bfs_average_time = sum(bfs_times) / NUMBER_OF_RUNS


# ----------------------------------------------------------
# 6. Measure DFS
# ----------------------------------------------------------

dfs_times = []

for _ in range(NUMBER_OF_RUNS):

    elapsed_time = timeit.timeit(
        lambda: dfs(graph, START_NODE, GOAL_NODE),
        number=REPETITIONS_PER_RUN
    )

    # Average time for one DFS execution
    average_time = (elapsed_time / REPETITIONS_PER_RUN) * 1000

    dfs_times.append(average_time)


# Get DFS result and node count
dfs_path, dfs_nodes = dfs(
    graph,
    START_NODE,
    GOAL_NODE
)

dfs_average_time = sum(dfs_times) / NUMBER_OF_RUNS


# ----------------------------------------------------------
# 7. Determine Which Used Less Time
# ----------------------------------------------------------

if bfs_average_time < dfs_average_time:
    faster_algorithm = "BFS"
elif dfs_average_time < bfs_average_time:
    faster_algorithm = "DFS"
else:
    faster_algorithm = "Same"


# ----------------------------------------------------------
# 8. Display Results
# ----------------------------------------------------------

print("=" * 65)
print("SLE-2: BFS vs DFS Empirical Performance Analysis")
print("=" * 65)

print("\nEXPERIMENT DETAILS")
print("-" * 65)
print("Problem              : Small graph search")
print(f"Start Node            : {START_NODE}")
print(f"Goal Node             : {GOAL_NODE}")
print(f"Experimental Runs     : {NUMBER_OF_RUNS}")
print(f"Repetitions per Run   : {REPETITIONS_PER_RUN}")

print("\n" + "=" * 65)

print("BFS RESULTS")
print("=" * 65)

print("Path Found            :", " -> ".join(bfs_path))
print("Nodes Expanded        :", bfs_nodes)
print(f"Average Time (ms)     : {bfs_average_time:.6f}")

print("\n" + "=" * 65)

print("DFS RESULTS")
print("=" * 65)

print("Path Found            :", " -> ".join(dfs_path))
print("Nodes Expanded        :", dfs_nodes)
print(f"Average Time (ms)     : {dfs_average_time:.6f}")

print("\n" + "=" * 65)

print("FINAL COMPARISON")
print("=" * 65)

print(
    f"{'Metric':<25}"
    f"{'BFS':<18}"
    f"{'DFS':<18}"
)

print("-" * 65)

print(
    f"{'Average Time (ms)':<25}"
    f"{bfs_average_time:<18.6f}"
    f"{dfs_average_time:<18.6f}"
)

print(
    f"{'Nodes Expanded':<25}"
    f"{bfs_nodes:<18}"
    f"{dfs_nodes:<18}"
)

print("-" * 65)

print(f"Lower Execution Time : {faster_algorithm}")

print("=" * 65)
